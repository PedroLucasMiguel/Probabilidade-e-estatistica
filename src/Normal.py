from PyQt5 import QtCore, QtGui, QtWidgets


# GUI para informar os dados da distribuição normal
class Normal_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 646)
        MainWindow.setStyleSheet("background-color: rgb(34, 34, 34);\n")

        # Central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Grid Layout 2
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Grid layout
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # Vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Label 2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(228, 228, 228);\n"
                                    "background-color: rgb(67, 67, 67); \n"
                                    "border-radius: 15px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        # Radio just random
        self.radio_justRandom = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(11)
        self.radio_justRandom.setFont(font)
        self.radio_justRandom.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                            "color: rgb(255, 255, 255);")
        self.radio_justRandom.clicked.connect(self.onJustRandomClicked)
        self.radio_justRandom.setObjectName("radio_justRandom")
        self.verticalLayout.addWidget(self.radio_justRandom)

        # Radio and file
        self.radio_RandomAndFile = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(11)
        self.radio_RandomAndFile.setFont(font)
        self.radio_RandomAndFile.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                               "color: rgb(255, 255, 255);")
        self.radio_RandomAndFile.clicked.connect(self.onRandomAndFileClicked)
        self.radio_RandomAndFile.setObjectName("radio_RandomAndFile")
        self.verticalLayout.addWidget(self.radio_RandomAndFile)

        # Spacer item
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)

        # Label 6
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(228, 228, 228);\n"
                                   "background-color: rgb(67, 67, 67); \n")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        # Spinbox population
        self.spinBox_population = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.spinBox_population.setFont(font)
        self.spinBox_population.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                              "color: rgb(255, 255, 255);")
        self.spinBox_population.setMinimum(1)
        self.spinBox_population.setMaximum(9999)
        self.spinBox_population.setValue(25)
        self.spinBox_population.setEnabled(False)
        self.spinBox_population.setObjectName("spinBox_population")
        self.verticalLayout.addWidget(self.spinBox_population)

        # Spacer item 1
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)

        # Spacer 3
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(228, 228, 228);\n"
                                   "background-color: rgb(67, 67, 67); \n"
                                   "border-radius: 20px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        # Spinbox sample size
        self.spinBox_SampleSize = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.spinBox_SampleSize.setFont(font)
        self.spinBox_SampleSize.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                              "color: rgb(255, 255, 255);")
        self.spinBox_SampleSize.setMinimum(1)
        self.spinBox_SampleSize.setMaximum(49999)
        self.spinBox_SampleSize.setValue(1000)
        self.spinBox_SampleSize.setEnabled(False)
        self.spinBox_SampleSize.setObjectName("spinBox_SampleSize")
        self.verticalLayout.addWidget(self.spinBox_SampleSize)

        # Spacer item 2
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        # Label 5
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(228, 228, 228);\n"
                                   "background-color: rgb(67, 67, 67); \n"
                                   "border-radius: 15px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        # DoubleSpinBox alpha
        self.doubleSpinBox_alpha = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.doubleSpinBox_alpha.setFont(font)
        self.doubleSpinBox_alpha.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                               "color: rgb(255, 255, 255);")
        self.doubleSpinBox_alpha.setDecimals(3)
        self.doubleSpinBox_alpha.setMinimum(-99999.0)
        self.doubleSpinBox_alpha.setMaximum(99999.0)
        self.doubleSpinBox_alpha.setSingleStep(0.001)
        self.doubleSpinBox_alpha.setEnabled(False)
        self.doubleSpinBox_alpha.setObjectName("doubleSpinBox_alpha")
        self.verticalLayout.addWidget(self.doubleSpinBox_alpha)

        # Spacer 3
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)

        # Spacer 7
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(228, 228, 228);\n"
                                   "background-color: rgb(67, 67, 67); \n"
                                   "border-radius: 15px;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)

        # DoubleSpinBox standart deviation
        self.doubleSpinBox_std = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.doubleSpinBox_std.setFont(font)
        self.doubleSpinBox_std.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                               "color: rgb(255, 255, 255);")
        self.doubleSpinBox_std.setDecimals(3)
        self.doubleSpinBox_std.setMaximum(9999.0)
        self.doubleSpinBox_std.setSingleStep(0.001)
        self.doubleSpinBox_std.setValue(1)
        self.doubleSpinBox_std.setEnabled(False)
        self.doubleSpinBox_std.setObjectName("doubleSpinBox_std")
        self.verticalLayout.addWidget(self.doubleSpinBox_std)

        # Spacer item 4
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)

        # Lavbel 4
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(228, 228, 228);\n"
                                   "background-color: rgb(67, 67, 67); \n"
                                   "border-radius: 15px;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        # Button load file
        self.btn_loadFile = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.btn_loadFile.setFont(font)
        self.btn_loadFile.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;")
        self.btn_loadFile.setEnabled(False)
        self.btn_loadFile.setObjectName("btn_loadFile")
        self.verticalLayout.addWidget(self.btn_loadFile)

        # Label file and path
        self.label_fileAndPath = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.label_fileAndPath.setFont(font)
        self.label_fileAndPath.setStyleSheet("color: rgb(228, 228, 228);\n"
                                             "background-color: rgb(67, 67, 67); \n"
                                             "border-radius: 15px;\n")
        self.label_fileAndPath.setObjectName("label_fileAndPath")
        self.verticalLayout.addWidget(self.label_fileAndPath)

        # Spacer item 5
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)

        # Button calculate
        self.btn_calculate = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.btn_calculate.setFont(font)
        self.btn_calculate.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;")
        self.btn_calculate.setEnabled(False)
        self.btn_calculate.setObjectName("btn_calculate")
        self.verticalLayout.addWidget(self.btn_calculate)

        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(228, 228, 228);\n"
                                 "background-color: rgb(67, 67, 67); \n"
                                 "border-radius: 15px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Como deseja analisar o modelo?"))
        self.radio_justRandom.setText(_translate("MainWindow", "Gerando apenas números pseudo aleatórios"))
        self.radio_RandomAndFile.setText(_translate("MainWindow", "Gerando números pseudo aleatórios e comparando com dados carregados"))
        self.label_6.setToolTip(_translate("MainWindow",
                                           """<html><head/><body><p style=\"color: black\">
                                           Número de elementos amostrados para estudo do Teorema do Limite Central.
                                           Um número maior de elementos requer tempo computacional maior para amostrar.
                                           </p></body></html>"""))
        self.label_6.setText(_translate("MainWindow",
                                        """<html><head/><body><p>
                                        Tamanho da população para amostragem (n)
                                        <span style=\" font-weight:600; text-decoration: underline;\">
                                        ?</span></p></body></html>"""))
        #self.spinBox_population.setToolTip(_translate("MainWindow", "<html><head/><body><p>Número de elementos amostrados para calcular a média para cada valor na amostra final. Um maior número de elementos faz a distribuição final melhor se aproximar de uma verdadeira distribuição normal, ao custo de um tempo computacional maior. Recomendado: entre 250 e 350.</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Quantos números você deseja gerar?"))
        self.label_5.setText(_translate("MainWindow", u"Digite o valor da média (μ)"))
        self.label_7.setText(_translate("MainWindow", u"Desvio padrão (σ)"))
        self.label_4.setText(_translate("MainWindow", "Clique no Botão para carregar o arquivo"))
        self.btn_loadFile.setText(_translate("MainWindow", "Carregar arquivo"))
        self.label_fileAndPath.setText(_translate("MainWindow", "Nenhum arquivo selecionado"))
        self.btn_calculate.setText(_translate("MainWindow", "Calcular"))
        self.label.setText(_translate("MainWindow", "Distribuição amostral média e normal"))

    def onJustRandomClicked(self):
        self.spinBox_SampleSize.setEnabled(True)
        self.spinBox_SampleSize.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                              "color: rgb(255, 255, 255);")
        self.spinBox_population.setEnabled(True)
        self.spinBox_population.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                              "color: rgb(255, 255, 255);")


        self.btn_loadFile.setEnabled(False)
        self.btn_loadFile.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;")

        self.doubleSpinBox_alpha.setEnabled(True)
        self.doubleSpinBox_alpha.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                               "color: rgb(255, 255, 255);")

        self.doubleSpinBox_std.setEnabled(True)
        self.doubleSpinBox_std.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                               "color: rgb(255, 255, 255);")

        self.btn_calculate.setEnabled(True)
        self.btn_calculate.setStyleSheet("background-color: rgb(118, 62, 153);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;")

    def onRandomAndFileClicked(self):
        self.spinBox_SampleSize.setEnabled(False)
        self.spinBox_SampleSize.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                              "color: rgb(255, 255, 255)")

        self.spinBox_population.setEnabled(True)
        self.spinBox_population.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                               "color: rgb(255, 255, 255);")

        self.btn_loadFile.setEnabled(True)
        self.btn_loadFile.setStyleSheet("background-color: rgb(118, 62, 153);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;")

        self.doubleSpinBox_alpha.setEnabled(True)
        self.doubleSpinBox_alpha.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                               "color: rgb(255, 255, 255);")

        self.doubleSpinBox_std.setEnabled(True)
        self.doubleSpinBox_std.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                               "color: rgb(255, 255, 255);")

        self.btn_calculate.setEnabled(True)
        self.btn_calculate.setStyleSheet("background-color: rgb(118, 62, 153);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Normal_UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
