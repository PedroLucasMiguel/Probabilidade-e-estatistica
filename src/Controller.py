from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem

from View import View
from Model import Model
from PyQt5 import QtWidgets
from CSVReader import CSV_Reader
import os.path
from os import path
import sys


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()
        self.mainWindow = None
        self.activeWindow = None

        # Guarda só as GUIs para fácil manipulação
        self.experiment1GUI = None
        self.experiment2GUI = None
        self.resultsGUI = None

        # Guarda o path do arquivo que vamos trabalhar :p
        self.user_data_path = None

        # Guarda o output das contas
        self.results = None

        self.csv_reader = CSV_Reader()
        self.callAndConfigGreeter()

    def callAndConfigGreeter(self):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        greeter = self.view.get_raw_gui("Greeter")
        greeter.setupUi(window)
        greeter.btn_exp1.clicked.connect(self.callAndConfigExp1)
        greeter.btn_exp2.clicked.connect(self.callAndConfigExp2)
        self.mainWindow = window
        self.mainWindow.show()
        sys.exit(app.exec_())

    ###################################################################################################################
    # ----------------------------------------------Greeter Config-----------------------------------------------------#
    ###################################################################################################################
    def callAndConfigExp1(self):
        experiment1Window = QtWidgets.QMainWindow()
        ui = self.view.get_raw_gui("Exponential")
        self.experiment1GUI = ui
        ui.setupUi(experiment1Window)
        self.experiment1GUI.btn_calculate.clicked.connect(self.exponentialGetData)
        self.experiment1GUI.btn_loadFile.clicked.connect(self.openFileDialog_EXP1)
        self.activeWindow = experiment1Window
        self.activeWindow.show()

    def callAndConfigExp2(self):
        experiment2Window = QtWidgets.QMainWindow()
        ui = self.view.get_raw_gui("Normal")
        self.experiment2GUI = ui
        ui.setupUi(experiment2Window)
        self.experiment2GUI.btn_calculate.clicked.connect(self.normalGetData)
        self.experiment2GUI.btn_loadFile.clicked.connect(self.openFileDialog_EXP2)
        self.activeWindow = experiment2Window
        self.activeWindow.show()

    ###################################################################################################################
    # ------------------------------------------Exponential Config-----------------------------------------------------#
    ###################################################################################################################
    def exponentialGetData(self):
        error = False

        requestData = {
            'generation': {
                'alpha': None,
                'sample_size': None
            },
            'user_data': None
        }

        requestData['generation']['alpha'] = float(self.experiment1GUI.doubleSpinBox_alpha.value())

        if self.experiment1GUI.radio_RandomAndFile.isChecked():
            if self.user_data_path is None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Nenhum arquivo selecionado!")
                msg.setWindowTitle("ERRO!")
                msg.exec_()
                error = True
            else:
                requestData['user_data'] = self.csv_reader.read_user_data(self.user_data_path)
                #print(len(requestData['user_data']))

        else:
            requestData['generation']['sample_size'] = int(self.experiment1GUI.spinBox_SampleSize.value())

        if not error:
            # print("REQUEST DATA!!!!!!!",requestData)
            self.model.sendRequest(requestData)
            #print("Request sended")
            self.results = self.model.getResults()
            #print("Did i returned?")
            self.callAndConfigResult()

    def openFileDialog_EXP1(self):
        file_path = QFileDialog().getOpenFileName(filter="Arquivos csv (*.csv)")
        self.user_data_path = file_path[0]
        self.experiment1GUI.label_fileAndPath.setText(self.user_data_path)
        #print(self.user_data_path)

    ###################################################################################################################
    # ------------------------------------------Normal Config---------------------------------------------------------#
    ###################################################################################################################
    def normalGetData(self):
        error = False

        requestData = {
            'generation': {
                'mean': None,
                'sample_size': None,
                'std_deviation': None,
                'population': None
            },
            'user_data': None
        }

        requestData['generation']['mean'] = float(self.experiment2GUI.doubleSpinBox_alpha.value())
        requestData['generation']['std_deviation'] = float(self.experiment2GUI.doubleSpinBox_std.value())
        requestData['generation']['population'] = int(self.experiment2GUI.spinBox_population.value())

        if self.experiment2GUI.radio_RandomAndFile.isChecked():
            if self.user_data_path is None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRO!")
                msg.setText("Nenhum arquivo selecionado!")
                msg.exec_()
                error = True
            else:
                requestData['user_data'] = self.csv_reader.read_user_data(self.user_data_path)

                if requestData['generation']['population'] > len(requestData['user_data']):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("ERRO!")
                    msg.setText("População > Quantidade de amostras!")
                    msg.exec_()
                    error = True

        else:
            requestData['generation']['sample_size'] = int(self.experiment2GUI.spinBox_SampleSize.value())

            if requestData['generation']['population'] > requestData['generation']['sample_size']:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRO!")
                msg.setText("População > Quantidade de amostras!")
                msg.exec_()
                error = True

        if not error:
            #print(requestData)
            self.model.sendRequest(requestData)
            self.results = self.model.getResults()
            self.callAndConfigResult()

    def openFileDialog_EXP2(self):
        file_path = QFileDialog().getOpenFileName(filter="Arquivos csv (*.csv)")
        self.user_data_path = file_path[0]
        self.experiment2GUI.label_fileAndPath.setText(self.user_data_path)
        #print(self.user_data_path)

    ###################################################################################################################
    # ------------------------------------------After calculation-----------------------------------------------------#
    ###################################################################################################################

    def callAndConfigResult(self):
        resultsGUI = QtWidgets.QMainWindow()
        ui = self.view.get_raw_gui("Results")
        self.resultsGUI = ui
        ui.setupUi(resultsGUI)

        # Colocar os resultados aqui

        # Graficos

        if os.path.exists('Graph'):
            self.results["Graph"].savefig("Graph/graph.png")
        else:
            os.mkdir("Graph")
            self.results["Graph"].savefig("Graph/graph.png")

        pixmap = QPixmap("Graph/graph.png")
        ui.graphic_label.setPixmap(pixmap)

        # Tabela
        # Dicionário de tradução

        translation_dict = {
            'min': 'Mínimo',
            'max': 'Máximo',
            'mean': 'Média',
            'median': 'Mediana',
            'lower_quartile': 'Quartil inferior',
            'upper_quartile': 'Quartil superior',
            'amplitude': 'Amplitude',
            'average_deviation': 'Desvio médio',
            'variance': 'Variância',
            'standard_deviation': 'Desvio padrão',
            'interquartile_range': 'Distancia entre quartis',
            'mode': 'Moda',
            'percentage_within_one_std_dev': 'Porcentagem em 1 desvio padrão',
            'percentage_within_two_std_dev': 'Porcentagem em 2 desvios padrões',
            'percentage_within_three_std_dev': 'Porcentagem em 3 desvios padrões',
            'percentage_of_outliers': 'Porcentagem de ponto discrepante',
            'coefficient_of_variation': 'Coeficiente de variação',
            'pearson_asymmetry_coefficient': 'Coeficiente de assimetria de Pearson',
            'skewness': 'Obliquidade',
            'kurtosis': 'Curtose'
        }

        # Linhas
        number_of_rows = len(self.results["Report"].keys())
        rows_labels = self.results["Report"].keys()
        ui.results_table.setRowCount(number_of_rows)
        ui.results_table.setVerticalHeaderLabels(rows_labels)
        #print(self.results)

        # Colunas
        keys = list(self.results['Report'].keys())
        columns_labels = []

        for key in self.results['Report'][keys[0]].keys():
            if key in translation_dict:
                columns_labels.append(translation_dict[key])
            else:
                columns_labels.append(key)

        #print(columns_labels)
        number_of_columns = len(columns_labels)
        ui.results_table.setColumnCount(number_of_columns)
        ui.results_table.setHorizontalHeaderLabels(columns_labels)

        for column in range(number_of_columns):
            ui.results_table.setColumnWidth(column, 300)

        column = 0
        row = 0
        for i in self.results['Report'].keys():
            for j in self.results['Report'][i].keys():
                ui.results_table.setItem(row, column, QTableWidgetItem(str(self.results['Report'][i][j])))
                column += 1
            column = 0
            row += 1


        squared_chi = self.results['Squared_Chi']
        #print("AAAAAAAAA ", squared_chi)

        text = ""

        if squared_chi is not None:
            observed_value, tabled_value, has_surpassed = squared_chi
            text = f"""X² Observado: {observed_value}, X² Tabulado: {tabled_value}\n"""+\
                f"""Por critério convencional, essa diferença {'não ' if not has_surpassed else ""}é considerada significativa. """
        else:
            text = """Teste de aderência qui quadrado indisponível para amostras"""

        ui.xi_label.setText(text)

        self.activeWindow = resultsGUI
        #self.activeWindow.show()
        self.activeWindow.showMaximized()
