from PyQt5 import QtCore, QtGui, QtWidgets


# GUI para informar os dados da distribuição exponencial
class Exponential_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(34, 34, 34);\n")

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Grid Layout 2
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Grid Layout
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # Vertical Layout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Title Label
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

        # Spacer
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)

        # Label 3
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

        # Spacer
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)

        # Label
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
        self.doubleSpinBox_alpha.setMinimum(0.001)
        self.doubleSpinBox_alpha.setMaximum(9999.0)
        self.doubleSpinBox_alpha.setSingleStep(0.001)
        self.doubleSpinBox_alpha.setValue(1.0)
        self.doubleSpinBox_alpha.setEnabled(False)
        self.doubleSpinBox_alpha.setObjectName("doubleSpinBox_alpha")
        self.verticalLayout.addWidget(self.doubleSpinBox_alpha)

        # Spacer 2
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        # Label 4
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

        # Button Load File
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
                                             "border-radius: 15px;\n"
                                             "")
        self.label_fileAndPath.setObjectName("label_fileAndPath")
        self.verticalLayout.addWidget(self.label_fileAndPath)

        # Spacer 3
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)

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

        # Grid Layout
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        # Spacer 4
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)

        # Label
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

        # Resto
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
        self.radio_RandomAndFile.setText(
            _translate("MainWindow", "Gerando números pseudo aleatórios e comparando com dados carregados"))
        self.label_3.setText(_translate("MainWindow", "Quantos números você deseja gerar?"))
        self.label_5.setText(_translate("MainWindow", u"Digite o valor do alfa (α)"))
        self.label_4.setText(_translate("MainWindow", "Clique no Botão para carregar o arquivo"))
        self.btn_loadFile.setText(_translate("MainWindow", "Carregar arquivo"))
        self.label_fileAndPath.setText(_translate("MainWindow", "Nenhum arquivo selecionado"))
        self.btn_calculate.setText(_translate("MainWindow", "Calcular"))
        self.label.setText(_translate("MainWindow", "Distribuição Exponencial"))

    def onJustRandomClicked(self):
        self.spinBox_SampleSize.setEnabled(True)
        self.spinBox_SampleSize.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                              "color: rgb(255, 255, 255);")

        self.btn_loadFile.setEnabled(False)
        self.btn_loadFile.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;")

        self.doubleSpinBox_alpha.setEnabled(True)
        self.doubleSpinBox_alpha.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                               "color: rgb(255, 255, 255);")

        self.btn_calculate.setEnabled(True)
        self.btn_calculate.setStyleSheet("background-color: rgb(118, 62, 153);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;")

    def onRandomAndFileClicked(self):
        self.spinBox_SampleSize.setEnabled(False)
        self.spinBox_SampleSize.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                              "color: rgb(255, 255, 255)")

        self.btn_loadFile.setEnabled(True)
        self.btn_loadFile.setStyleSheet("background-color: rgb(118, 62, 153);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;")

        self.doubleSpinBox_alpha.setEnabled(True)
        self.doubleSpinBox_alpha.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                               "color: rgb(255, 255, 255);")

        self.btn_calculate.setEnabled(True)
        self.btn_calculate.setStyleSheet("background-color: rgb(118, 62, 153);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Exponential_UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
