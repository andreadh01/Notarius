# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar-usuario-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(923, 868)
        Dialog.setStyleSheet("QDialog {\n"
"background-color: white;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 847, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_iconousuario = QtWidgets.QLabel(Dialog)
        self.label_iconousuario.setText("")
        self.label_iconousuario.setObjectName("label_iconousuario")
        self.horizontalLayout_3.addWidget(self.label_iconousuario)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.lineEdit_contrasenausuario = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_contrasenausuario.setStyleSheet("QLineEdit {\n"
"border-radius: 6px;\n"
"border: 1px solid rgb(166,164, 180);\n"
"background-color:white;\n"
"color: rgb(103,80,41);\n"
"padding: 5px;\n"
"}")
        self.lineEdit_contrasenausuario.setText("")
        self.lineEdit_contrasenausuario.setObjectName("lineEdit_contrasenausuario")
        self.verticalLayout_4.addWidget(self.lineEdit_contrasenausuario)
        self.lineEdit_nombreusuario = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nombreusuario.setStyleSheet("QLineEdit {\n"
"border-radius: 6px;\n"
"border: 1px solid rgb(166,164, 180);\n"
"background-color:white;\n"
"color: rgb(103,80,41);\n"
"padding: 5px;\n"
"}")
        self.lineEdit_nombreusuario.setObjectName("lineEdit_nombreusuario")
        self.verticalLayout_4.addWidget(self.lineEdit_nombreusuario)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_tabla = QtWidgets.QLabel(Dialog)
        self.label_tabla.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_tabla.setObjectName("label_tabla")
        self.gridLayout.addWidget(self.label_tabla, 0, 0, 1, 1)
        self.label_acceso = QtWidgets.QLabel(Dialog)
        self.label_acceso.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_acceso.setObjectName("label_acceso")
        self.gridLayout.addWidget(self.label_acceso, 0, 2, 1, 1)
        self.checkBox_acceso_8 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_acceso_8.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.checkBox_acceso_8.setObjectName("checkBox_acceso_8")
        self.gridLayout.addWidget(self.checkBox_acceso_8, 8, 2, 1, 1)
        self.checkBox_acceso_9 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_acceso_9.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.checkBox_acceso_9.setObjectName("checkBox_acceso_9")
        self.gridLayout.addWidget(self.checkBox_acceso_9, 9, 2, 1, 1)
        self.comboBox_tablas = QtWidgets.QComboBox(Dialog)
        self.comboBox_tablas.setStyleSheet("QComboBox{\n"
"border: 1px solid #95753d;\n"
"background-color: #white;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);\n"
"}")
        self.comboBox_tablas.setObjectName("comboBox_tablas")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.comboBox_tablas.addItem("")
        self.gridLayout.addWidget(self.comboBox_tablas, 1, 0, 1, 1)
        self.checkBox_acceso1 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_acceso1.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.checkBox_acceso1.setObjectName("checkBox_acceso1")
        self.gridLayout.addWidget(self.checkBox_acceso1, 1, 2, 1, 1)
        self.label_acciones = QtWidgets.QLabel(Dialog)
        self.label_acciones.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";\n"
"color: rgb(141, 110, 58);")
        self.label_acciones.setObjectName("label_acciones")
        self.gridLayout.addWidget(self.label_acciones, 0, 1, 1, 1)
        self.checkBox_acceso_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_acceso_6.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.checkBox_acceso_6.setObjectName("checkBox_acceso_6")
        self.gridLayout.addWidget(self.checkBox_acceso_6, 6, 2, 1, 1)
        self.checkBox_acceso_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_acceso_2.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.checkBox_acceso_2.setObjectName("checkBox_acceso_2")
        self.gridLayout.addWidget(self.checkBox_acceso_2, 2, 2, 1, 1)
        self.checkBox_acceso_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_acceso_3.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.checkBox_acceso_3.setObjectName("checkBox_acceso_3")
        self.gridLayout.addWidget(self.checkBox_acceso_3, 3, 2, 1, 1)
        self.checkBox_acceso_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_acceso_4.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.checkBox_acceso_4.setObjectName("checkBox_acceso_4")
        self.gridLayout.addWidget(self.checkBox_acceso_4, 4, 2, 1, 1)
        self.checkBox_acceso_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_acceso_5.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.checkBox_acceso_5.setObjectName("checkBox_acceso_5")
        self.gridLayout.addWidget(self.checkBox_acceso_5, 5, 2, 1, 1)
        self.checkBox_acceso_7 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_acceso_7.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.checkBox_acceso_7.setObjectName("checkBox_acceso_7")
        self.gridLayout.addWidget(self.checkBox_acceso_7, 7, 2, 1, 1)
        self.comboBox_acciones = QtWidgets.QComboBox(Dialog)
        self.comboBox_acciones.setStyleSheet("QComboBox{\n"
"border: 1px solid #95753d;\n"
"background-color: #white;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);\n"
"}")
        self.comboBox_acciones.setObjectName("comboBox_acciones")
        self.comboBox_acciones.addItem("")
        self.comboBox_acciones.addItem("")
        self.comboBox_acciones.addItem("")
        self.gridLayout.addWidget(self.comboBox_acciones, 1, 1, 1, 1)
        self.checkBox_acceso_10 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_acceso_10.setStyleSheet("\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(149, 117, 61);")
        self.checkBox_acceso_10.setObjectName("checkBox_acceso_10")
        self.gridLayout.addWidget(self.checkBox_acceso_10, 10, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton_cancelar = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancelar.setStyleSheet("QPushButton {\n"
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
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.horizontalLayout_2.addWidget(self.pushButton_cancelar)
        self.pushButton_confirmar = QtWidgets.QPushButton(Dialog)
        self.pushButton_confirmar.setStyleSheet("QPushButton {\n"
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
        self.pushButton_confirmar.setObjectName("pushButton_confirmar")
        self.horizontalLayout_2.addWidget(self.pushButton_confirmar)
        self.horizontalLayout_2.setStretch(0, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 847, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_contrasenausuario.setPlaceholderText(_translate("Dialog", "Usuario..."))
        self.lineEdit_nombreusuario.setPlaceholderText(_translate("Dialog", "Contraseña del usuario..."))
        self.label_tabla.setText(_translate("Dialog", "Tabla"))
        self.label_acceso.setText(_translate("Dialog", "Acceso a"))
        self.checkBox_acceso_8.setText(_translate("Dialog", "Columna 8"))
        self.checkBox_acceso_9.setText(_translate("Dialog", "Columna 9"))
        self.comboBox_tablas.setItemText(0, _translate("Dialog", "Tabla 1"))
        self.comboBox_tablas.setItemText(1, _translate("Dialog", "Tabla 2"))
        self.comboBox_tablas.setItemText(2, _translate("Dialog", "Tabla 3"))
        self.comboBox_tablas.setItemText(3, _translate("Dialog", "Tabla 4"))
        self.comboBox_tablas.setItemText(4, _translate("Dialog", "Tabla 5"))
        self.comboBox_tablas.setItemText(5, _translate("Dialog", "Tabla 6"))
        self.comboBox_tablas.setItemText(6, _translate("Dialog", "Tabla 7"))
        self.comboBox_tablas.setItemText(7, _translate("Dialog", "Tabla 8"))
        self.comboBox_tablas.setItemText(8, _translate("Dialog", "Tabla 9"))
        self.comboBox_tablas.setItemText(9, _translate("Dialog", "Tabla 10"))
        self.comboBox_tablas.setItemText(10, _translate("Dialog", "Tabla 11"))
        self.comboBox_tablas.setItemText(11, _translate("Dialog", "Tabla 12"))
        self.comboBox_tablas.setItemText(12, _translate("Dialog", "Tabla 13"))
        self.comboBox_tablas.setItemText(13, _translate("Dialog", "Tabla 14"))
        self.comboBox_tablas.setItemText(14, _translate("Dialog", "Tabla 15"))
        self.comboBox_tablas.setItemText(15, _translate("Dialog", "Tabla 16"))
        self.comboBox_tablas.setItemText(16, _translate("Dialog", "Tabla 17"))
        self.checkBox_acceso1.setText(_translate("Dialog", "Columna 1"))
        self.label_acciones.setText(_translate("Dialog", "Acciones"))
        self.checkBox_acceso_6.setText(_translate("Dialog", "Columna 6"))
        self.checkBox_acceso_2.setText(_translate("Dialog", "Columna 2"))
        self.checkBox_acceso_3.setText(_translate("Dialog", "Columna 3"))
        self.checkBox_acceso_4.setText(_translate("Dialog", "Columna 4"))
        self.checkBox_acceso_5.setText(_translate("Dialog", "Columna 5"))
        self.checkBox_acceso_7.setText(_translate("Dialog", "Columna 7"))
        self.comboBox_acciones.setItemText(0, _translate("Dialog", "Agregar"))
        self.comboBox_acciones.setItemText(1, _translate("Dialog", "Modificar"))
        self.comboBox_acciones.setItemText(2, _translate("Dialog", "Eliminar"))
        self.checkBox_acceso_10.setText(_translate("Dialog", "Columna 10"))
        self.pushButton_cancelar.setText(_translate("Dialog", "Cancelar"))
        self.pushButton_confirmar.setText(_translate("Dialog", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

