
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from App.BackEnd.Date import Date
from App.BackEnd.DateManager import DateManager
from App.BackEnd.ExtractData import ExtractData
from App.FrontEnd.popup import Ui_Form


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(230, 320, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_download.setFont(font)
        self.btn_download.setObjectName("btn_download")
        self.btn_download.clicked.connect(self.pressed)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 90, 601, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(25, 10, 25, 10)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_estacao = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_estacao.setFont(font)
        self.lbl_estacao.setObjectName("lbl_estacao")
        self.horizontalLayout.addWidget(self.lbl_estacao)
        self.tf_estacao = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tf_estacao.setFont(font)
        self.tf_estacao.setObjectName("tf_estacao")
        self.horizontalLayout.addWidget(self.tf_estacao)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 150, 601, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(25, 0, 25, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_inicial = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_inicial.setFont(font)
        self.lbl_inicial.setObjectName("lbl_inicial")
        self.horizontalLayout_2.addWidget(self.lbl_inicial)
        self.dt_inicial = QtWidgets.QDateEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dt_inicial.setFont(font)
        self.dt_inicial.setCalendarPopup(True)
        self.dt_inicial.setDate(QtCore.QDate(2020, 1, 1))
        self.dt_inicial.setObjectName("dt_inicial")
        self.horizontalLayout_2.addWidget(self.dt_inicial)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_final = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_final.setFont(font)
        self.lbl_final.setObjectName("lbl_final")
        self.horizontalLayout_3.addWidget(self.lbl_final)
        self.dt_final = QtWidgets.QDateEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dt_final.setFont(font)
        self.dt_final.setCalendarPopup(True)
        self.dt_final.setDate(QtCore.QDate(2020, 1, 1))
        self.dt_final.setObjectName("dt_final")
        self.horizontalLayout_3.addWidget(self.dt_final)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 230, 601, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(25, 0, 25, 0)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_arquivos = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_arquivos.setFont(font)
        self.lbl_arquivos.setObjectName("lbl_arquivos")
        self.horizontalLayout_5.addWidget(self.lbl_arquivos)
        self.cb_arquivos = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_arquivos.setFont(font)
        self.cb_arquivos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_arquivos.setModelColumn(0)
        self.cb_arquivos.setObjectName("cb_arquivos")
        self.cb_arquivos.addItem("")
        self.cb_arquivos.addItem("")
        self.horizontalLayout_5.addWidget(self.cb_arquivos)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 601, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(25, 0, 25, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.popup = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.popup)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dados Climáticos"))
        self.btn_download.setText(_translate("MainWindow", "Download"))
        self.lbl_estacao.setText(_translate("MainWindow", "Estação de extração de dados"))
        self.lbl_inicial.setText(_translate("MainWindow", "Data Inicial"))
        self.lbl_final.setText(_translate("MainWindow", "Data Final"))
        self.lbl_arquivos.setText(_translate("MainWindow", "Deseja salvar em quantos arquivos"))
        self.cb_arquivos.setItemText(0, _translate("MainWindow", "1 Arquivo"))
        self.cb_arquivos.setItemText(1, _translate("MainWindow", "Vários Arquivos"))
        self.label_2.setText(_translate("MainWindow", "Insira o periodo de dias que você deseja extrair os dados"))

    def pressed(self):
        option = self.cb_arquivos.currentText()
        _translate = QtCore.QCoreApplication.translate

        date_initial = self.dt_inicial.date()
        date_final = self.dt_final.date()

        station = self.tf_estacao.toPlainText().upper()

        if date_initial != "" and date_final != "" and station != "":

            date = Date(date_initial.day(), date_initial.month(), date_initial.year())
            date2 = Date(date_final.day(), date_final.month(), date_final.year())

            dm = DateManager(date, date2, station)

            self.popup.show()

            if option == "1 Arquivo":
                ext = ExtractData(dm.generate_url(), True)
                ext.extract_and_save()

            elif option == "Vários Arquivos":
                ext = ExtractData(dm.generate_url(), False)
                ext.extract_and_save()

            exit()

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle("Fusion")
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
