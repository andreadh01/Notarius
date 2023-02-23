# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar-registros.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 539)
        MainWindow.setStyleSheet("QMainWindow {\n"
"background-color:white;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 26pt \"Arial Black\";\n"
"color: rgb(149, 117, 61);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.button_tabla = QtWidgets.QPushButton(self.centralwidget)
        self.button_tabla.setStyleSheet("QPushButton {\n"
"    color: rgb(141, 110, 58);\n"
"    border: none;\n"
"    font: 10pt \"Arial Rounded MT Bold\";\n"
"    height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bar-chart-box-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_tabla.setIcon(icon)
        self.button_tabla.setAutoDefault(False)
        self.button_tabla.setFlat(False)
        self.button_tabla.setObjectName("button_tabla")
        self.verticalLayout_6.addWidget(self.button_tabla)
        self.button_importar_excel = QtWidgets.QPushButton(self.centralwidget)
        self.button_importar_excel.setStyleSheet("QPushButton {\n"
"    color: rgb(141, 110, 58);\n"
"    border: none;\n"
"    font: 10pt \"Arial Rounded MT Bold\";\n"
"    height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("file-excel-2-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_importar_excel.setIcon(icon1)
        self.button_importar_excel.setObjectName("button_importar_excel")
        self.verticalLayout_6.addWidget(self.button_importar_excel)
        self.button_agregar_usuario = QtWidgets.QPushButton(self.centralwidget)
        self.button_agregar_usuario.setStyleSheet("QPushButton {\n"
"    color: rgb(141, 110, 58);\n"
"    border: none;\n"
"    font: 10pt \"Arial Rounded MT Bold\";\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("user-add-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_agregar_usuario.setIcon(icon2)
        self.button_agregar_usuario.setObjectName("button_agregar_usuario")
        self.verticalLayout_6.addWidget(self.button_agregar_usuario)
        self.button_editar_privilegios = QtWidgets.QPushButton(self.centralwidget)
        self.button_editar_privilegios.setStyleSheet("QPushButton {\n"
"    color: rgb(141, 110, 58);\n"
"    border: none;\n"
"    font: 10pt \"Arial Rounded MT Bold\";\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("edit-2-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_editar_privilegios.setIcon(icon3)
        self.button_editar_privilegios.setObjectName("button_editar_privilegios")
        self.verticalLayout_6.addWidget(self.button_editar_privilegios)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.button_logout = QtWidgets.QPushButton(self.centralwidget)
        self.button_logout.setStyleSheet("QPushButton {\n"
"    color: rgb(141, 110, 58);\n"
"    border: none;\n"
"    font: 10pt \"Arial Rounded MT Bold\";\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(149, 117, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("logout-box-r-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_logout.setIcon(icon4)
        self.button_logout.setObjectName("button_logout")
        self.verticalLayout_5.addWidget(self.button_logout)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem13)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem15)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem16)
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_id.setObjectName("label_id")
        self.verticalLayout_7.addWidget(self.label_id)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"border-radius: 6px;\n"
"border: 1px solid #d3c393;\n"
"background-color: white;\n"
"color:  #95753d;\n"
"height: 20px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_7.addWidget(self.lineEdit)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem17)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"border-radius: 6px;\n"
"border: 1px solid #d3c393;\n"
"background-color: white;\n"
"color:  #95753d;\n"
"height: 20px;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_7.addWidget(self.lineEdit_2)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem18)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"border-radius: 6px;\n"
"border: 1px solid #d3c393;\n"
"background-color: white;\n"
"color:  #95753d;\n"
"height: 20px;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_7.addWidget(self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("color: rgb(141, 110, 58);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem19)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"border-radius: 6px;\n"
"border: 1px solid #d3c393;\n"
"background-color: white;\n"
"color:  #95753d;\n"
"height: 20px;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_7.addWidget(self.lineEdit_4)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("color: rgb(141, 110, 58);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem20)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"border-radius: 6px;\n"
"border: 1px solid #d3c393;\n"
"background-color: white;\n"
"color:  #95753d;\n"
"height: 20px;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_7.addWidget(self.lineEdit_5)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem21)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancel.setStyleSheet("QPushButton {\n"
"border-radius: 6px;\n"
"border: 2px solid #95753d;\n"
"background-color: white;\n"
"color: #95753d;\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(116, 91, 47);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid  rgb(116, 91, 47);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(103, 80, 41);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid  rgb(103, 80, 41);\n"
"}")
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_4.addWidget(self.button_cancel)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem22)
        self.button_guardar = QtWidgets.QPushButton(self.centralwidget)
        self.button_guardar.setStyleSheet("QPushButton {\n"
"border-radius: 6px;\n"
"border: 3px solid #95753d;\n"
"background-color: #95753d;\n"
"color: white;\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(116, 91, 47);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid  rgb(116, 91, 47);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(103, 80, 41);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid  rgb(103, 80, 41);\n"
"}")
        self.button_guardar.setObjectName("button_guardar")
        self.horizontalLayout_4.addWidget(self.button_guardar)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem23)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem24)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem25)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">....</span><span style=\" font-size:24pt;\">Notarius</span><span style=\" font-size:24pt; color:#ffffff;\">....</span></p></body></html>"))
        self.button_tabla.setText(_translate("MainWindow", "Tabla"))
        self.button_importar_excel.setText(_translate("MainWindow", "Importar Excel"))
        self.button_agregar_usuario.setText(_translate("MainWindow", "Agregar Usuario"))
        self.button_editar_privilegios.setText(_translate("MainWindow", "Editar Privilegios"))
        self.button_logout.setText(_translate("MainWindow", "Cerrar Sesión"))
        self.label_id.setText(_translate("MainWindow", "ID"))
        self.label_4.setText(_translate("MainWindow", "Input"))
        self.label_5.setText(_translate("MainWindow", "Input"))
        self.label_6.setText(_translate("MainWindow", "Your password is between 4 and 12 characters"))
        self.label_7.setText(_translate("MainWindow", "Input Text Label"))
        self.label_8.setText(_translate("MainWindow", "Error message informing me of a problem"))
        self.label_9.setText(_translate("MainWindow", "Input"))
        self.button_cancel.setText(_translate("MainWindow", "     Cancel     "))
        self.button_guardar.setText(_translate("MainWindow", "     Guardar     "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
