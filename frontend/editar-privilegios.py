# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editar-privilegios-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(892, 601)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.title_notarius = QtWidgets.QLabel(Dialog)
        self.title_notarius.setStyleSheet("font: 26pt \"Arial Black\";\n"
"color: rgb(149, 117, 61);")
        self.title_notarius.setObjectName("title_notarius")
        self.verticalLayout_5.addWidget(self.title_notarius)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.button_tabla = QtWidgets.QPushButton(Dialog)
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
        self.button_editar_privilegios = QtWidgets.QPushButton(Dialog)
        self.button_editar_privilegios.setStyleSheet("QPushButton {\n"
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
        self.button_editar_privilegios.setIcon(icon1)
        self.button_editar_privilegios.setObjectName("button_editar_privilegios")
        self.verticalLayout_6.addWidget(self.button_editar_privilegios)
        self.button_agregar_usuario = QtWidgets.QPushButton(Dialog)
        self.button_agregar_usuario.setStyleSheet("QPushButton {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("user-add-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_agregar_usuario.setIcon(icon2)
        self.button_agregar_usuario.setObjectName("button_agregar_usuario")
        self.verticalLayout_6.addWidget(self.button_agregar_usuario)
        self.button_exporatr_excel = QtWidgets.QPushButton(Dialog)
        self.button_exporatr_excel.setStyleSheet("QPushButton {\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("edit-2-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_exporatr_excel.setIcon(icon3)
        self.button_exporatr_excel.setObjectName("button_exporatr_excel")
        self.verticalLayout_6.addWidget(self.button_exporatr_excel)
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
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setIcon(icon4)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem13)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        spacerItem14 = QtWidgets.QSpacerItem(20, 580, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(20, 580, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem15)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem17)
        self.label_editar_privilegios = QtWidgets.QLabel(Dialog)
        self.label_editar_privilegios.setStyleSheet("font: 26pt \"Arial Black\";\n"
"color: rgb(149, 117, 61);")
        self.label_editar_privilegios.setObjectName("label_editar_privilegios")
        self.horizontalLayout_2.addWidget(self.label_editar_privilegios)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem18)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem19)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_tablas = QtWidgets.QLabel(Dialog)
        self.label_tablas.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_tablas.setObjectName("label_tablas")
        self.gridLayout.addWidget(self.label_tablas, 0, 1, 1, 1)
        self.acceso_8 = QtWidgets.QCheckBox(Dialog)
        self.acceso_8.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.acceso_8.setObjectName("acceso_8")
        self.gridLayout.addWidget(self.acceso_8, 7, 3, 1, 1)
        self.usuarioslist = QtWidgets.QComboBox(Dialog)
        self.usuarioslist.setStyleSheet("QComboBox{\n"
"border: 1px solid #95753d;\n"
"background-color: #white;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);\n"
"}")
        self.usuarioslist.setObjectName("usuarioslist")
        self.usuarioslist.addItem("")
        self.usuarioslist.addItem("")
        self.usuarioslist.addItem("")
        self.gridLayout.addWidget(self.usuarioslist, 1, 0, 1, 1)
        self.acceso_1 = QtWidgets.QCheckBox(Dialog)
        self.acceso_1.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.acceso_1.setObjectName("acceso_1")
        self.gridLayout.addWidget(self.acceso_1, 1, 3, 1, 1)
        self.acceso_2 = QtWidgets.QCheckBox(Dialog)
        self.acceso_2.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.acceso_2.setObjectName("acceso_2")
        self.gridLayout.addWidget(self.acceso_2, 10, 3, 1, 1)
        self.acceso_5 = QtWidgets.QCheckBox(Dialog)
        self.acceso_5.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.acceso_5.setObjectName("acceso_5")
        self.gridLayout.addWidget(self.acceso_5, 4, 3, 1, 1)
        self.acceso_6 = QtWidgets.QCheckBox(Dialog)
        self.acceso_6.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.acceso_6.setObjectName("acceso_6")
        self.gridLayout.addWidget(self.acceso_6, 5, 3, 1, 1)
        self.label_accesos = QtWidgets.QLabel(Dialog)
        self.label_accesos.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_accesos.setObjectName("label_accesos")
        self.gridLayout.addWidget(self.label_accesos, 0, 3, 1, 1)
        self.label_Usuarios = QtWidgets.QLabel(Dialog)
        self.label_Usuarios.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_Usuarios.setObjectName("label_Usuarios")
        self.gridLayout.addWidget(self.label_Usuarios, 0, 0, 1, 1)
        self.acceso_4 = QtWidgets.QCheckBox(Dialog)
        self.acceso_4.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.acceso_4.setObjectName("acceso_4")
        self.gridLayout.addWidget(self.acceso_4, 3, 3, 1, 1)
        self.acceso_9 = QtWidgets.QCheckBox(Dialog)
        self.acceso_9.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.acceso_9.setObjectName("acceso_9")
        self.gridLayout.addWidget(self.acceso_9, 8, 3, 1, 1)
        self.acceso_10 = QtWidgets.QCheckBox(Dialog)
        self.acceso_10.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.acceso_10.setObjectName("acceso_10")
        self.gridLayout.addWidget(self.acceso_10, 9, 3, 1, 1)
        self.acceso_3 = QtWidgets.QCheckBox(Dialog)
        self.acceso_3.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.acceso_3.setObjectName("acceso_3")
        self.gridLayout.addWidget(self.acceso_3, 2, 3, 1, 1)
        self.acceso_7 = QtWidgets.QCheckBox(Dialog)
        self.acceso_7.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.acceso_7.setObjectName("acceso_7")
        self.gridLayout.addWidget(self.acceso_7, 6, 3, 1, 1)
        self.label_acciones = QtWidgets.QLabel(Dialog)
        self.label_acciones.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_acciones.setObjectName("label_acciones")
        self.gridLayout.addWidget(self.label_acciones, 0, 2, 1, 1)
        self.tablaslist = QtWidgets.QComboBox(Dialog)
        self.tablaslist.setStyleSheet("QComboBox{\n"
"border: 1px solid #95753d;\n"
"background-color: #white;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);\n"
"}")
        self.tablaslist.setObjectName("tablaslist")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.tablaslist.addItem("")
        self.gridLayout.addWidget(self.tablaslist, 1, 1, 1, 1)
        self.accioneslist = QtWidgets.QComboBox(Dialog)
        self.accioneslist.setStyleSheet("QComboBox{\n"
"border: 1px solid #95753d;\n"
"background-color: #white;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);\n"
"}")
        self.accioneslist.setObjectName("accioneslist")
        self.accioneslist.addItem("")
        self.accioneslist.addItem("")
        self.accioneslist.addItem("")
        self.gridLayout.addWidget(self.accioneslist, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem20)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem21)
        self.button_guardar = QtWidgets.QPushButton(Dialog)
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
        self.horizontalLayout_3.addWidget(self.button_guardar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem22 = QtWidgets.QSpacerItem(20, 580, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem22)
        spacerItem23 = QtWidgets.QSpacerItem(20, 580, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem23)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_notarius.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">....</span><span style=\" font-size:24pt;\">Notarius</span><span style=\" font-size:24pt; color:#ffffff;\">....</span></p></body></html>"))
        self.button_tabla.setText(_translate("Dialog", "Tabla"))
        self.button_editar_privilegios.setText(_translate("Dialog", "Exportar Excel"))
        self.button_agregar_usuario.setText(_translate("Dialog", "Agregar Usuario"))
        self.button_exporatr_excel.setText(_translate("Dialog", "Editar Privilegios"))
        self.pushButton.setText(_translate("Dialog", "Cerrar Sesión"))
        self.label_editar_privilegios.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Editar privilegios</span></p></body></html>"))
        self.label_tablas.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Tabla</span></p></body></html>"))
        self.acceso_8.setText(_translate("Dialog", "Columna 7"))
        self.usuarioslist.setItemText(0, _translate("Dialog", "Usuario 1"))
        self.usuarioslist.setItemText(1, _translate("Dialog", "Usuario 2"))
        self.usuarioslist.setItemText(2, _translate("Dialog", "Usuario 3"))
        self.acceso_1.setText(_translate("Dialog", "Columna 1"))
        self.acceso_2.setText(_translate("Dialog", "Columna 10"))
        self.acceso_5.setText(_translate("Dialog", "Columna 4"))
        self.acceso_6.setText(_translate("Dialog", "Columna 5"))
        self.label_accesos.setText(_translate("Dialog", "<html><head/><body><p>Acceso a</p></body></html>"))
        self.label_Usuarios.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Usuarios</span></p></body></html>"))
        self.acceso_4.setText(_translate("Dialog", "Columna 3"))
        self.acceso_9.setText(_translate("Dialog", "Columna 8"))
        self.acceso_10.setText(_translate("Dialog", "Columna 9"))
        self.acceso_3.setText(_translate("Dialog", "Columna 2"))
        self.acceso_7.setText(_translate("Dialog", "Columna 6"))
        self.label_acciones.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Acciones</span></p></body></html>"))
        self.tablaslist.setItemText(0, _translate("Dialog", "Tabla 1"))
        self.tablaslist.setItemText(1, _translate("Dialog", "Tabla 2"))
        self.tablaslist.setItemText(2, _translate("Dialog", "Tabla 3"))
        self.tablaslist.setItemText(3, _translate("Dialog", "Tabla 4"))
        self.tablaslist.setItemText(4, _translate("Dialog", "Tabla 5"))
        self.tablaslist.setItemText(5, _translate("Dialog", "Tabla 6"))
        self.tablaslist.setItemText(6, _translate("Dialog", "Tabla 7"))
        self.tablaslist.setItemText(7, _translate("Dialog", "Tabla 8"))
        self.tablaslist.setItemText(8, _translate("Dialog", "Tabla 9"))
        self.tablaslist.setItemText(9, _translate("Dialog", "Tabla 10"))
        self.tablaslist.setItemText(10, _translate("Dialog", "Tabla 11"))
        self.tablaslist.setItemText(11, _translate("Dialog", "Tabla 12"))
        self.tablaslist.setItemText(12, _translate("Dialog", "Tabla 13"))
        self.tablaslist.setItemText(13, _translate("Dialog", "Tabla 14"))
        self.tablaslist.setItemText(14, _translate("Dialog", "Tabla 15"))
        self.tablaslist.setItemText(15, _translate("Dialog", "Tabla 16"))
        self.tablaslist.setItemText(16, _translate("Dialog", "Tabla 17"))
        self.accioneslist.setItemText(0, _translate("Dialog", "Agregar"))
        self.accioneslist.setItemText(1, _translate("Dialog", "Modificar"))
        self.accioneslist.setItemText(2, _translate("Dialog", "Eliminar"))
        self.button_guardar.setText(_translate("Dialog", "    Guardar    "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

