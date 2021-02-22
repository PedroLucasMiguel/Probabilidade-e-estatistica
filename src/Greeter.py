from PyQt5 import QtCore, QtGui, QtWidgets


# GUI que inicia o programa
class Greeter_UI(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(34, 34, 34);")

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Horizontal Layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Grid Layout
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")

        # Spacer
        spacerItem = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)

        # Spacer 1
        spacerItem1 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)

        # Spacer 2
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)

        # Spacer 3
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)

        # Title Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(228, 228, 228);\n"
"background-color: rgb(67, 67, 67); \n"
"border-radius: 15px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        # Vertical Layout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Button Experiment 1
        self.btn_exp1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exp1.setMaximumSize(QtCore.QSize(16777215, 80))
        self.btn_exp1.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        self.btn_exp1.setFont(font)
        self.btn_exp1.setStyleSheet("background-color: rgb(118, 62, 153);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.btn_exp1.setObjectName("btn_exp1")
        self.verticalLayout.addWidget(self.btn_exp1)

        # Button Experiment 2
        self.btn_exp2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exp2.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        self.btn_exp2.setFont(font)
        self.btn_exp2.setStyleSheet("background-color: rgb(118, 62, 153);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.btn_exp2.setObjectName("btn_exp2")
        self.verticalLayout.addWidget(self.btn_exp2)

        # Grid Layout
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)

        # Spacer 4
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)

        # Spacer 5
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu Principal"))
        self.label.setText(_translate("MainWindow", "Selecione o experimento"))
        self.btn_exp1.setText(_translate("MainWindow", "Experimento 1"))
        self.btn_exp2.setText(_translate("MainWindow", "Experimento 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Greeter_UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
