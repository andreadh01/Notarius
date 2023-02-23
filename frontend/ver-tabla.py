# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver-tabla-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(764, 591)
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
        self.button_importar_excel = QtWidgets.QPushButton(Dialog)
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
        self.button_logout = QtWidgets.QPushButton(Dialog)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        self.button_agregar_registro = QtWidgets.QPushButton(Dialog)
        self.button_agregar_registro.setStyleSheet("QPushButton {\n"
"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: white;\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(179, 179, 179);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid  rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(103, 80, 41);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid  rgb(103, 80, 41);\n"
"}")
        self.button_agregar_registro.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("add-circle-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_agregar_registro.setIcon(icon5)
        self.button_agregar_registro.setIconSize(QtCore.QSize(20, 20))
        self.button_agregar_registro.setObjectName("button_agregar_registro")
        self.verticalLayout_2.addWidget(self.button_agregar_registro)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_exportar = QtWidgets.QPushButton(Dialog)
        self.button_exportar.setStyleSheet("QPushButton {\n"
"border-radius: 11px;\n"
"border: 2px solid #95753d;\n"
"background-color: #white;\n"
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
        self.button_exportar.setObjectName("button_exportar")
        self.horizontalLayout_3.addWidget(self.button_exportar)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.lineEdit_search = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_search.setStyleSheet("QLineEdit {\n"
"border-radius: 6px;\n"
"border: 1px solid #d3c393;\n"
"background-color: #white;\n"
"color:  #95753d;\n"
"height: 20px;\n"
"}")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_3.addWidget(self.lineEdit_search)
        self.button_search = QtWidgets.QPushButton(Dialog)
        self.button_search.setStyleSheet("QPushButton {\n"
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
        self.button_search.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("search-line (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_search.setIcon(icon6)
        self.button_search.setObjectName("button_search")
        self.horizontalLayout_3.addWidget(self.button_search)
        self.button_filtro = QtWidgets.QPushButton(Dialog)
        self.button_filtro.setStyleSheet("QPushButton {\n"
"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
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
        self.button_filtro.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("filter-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_filtro.setIcon(icon7)
        self.button_filtro.setObjectName("button_filtro")
        self.horizontalLayout_3.addWidget(self.button_filtro)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.full_table = QtWidgets.QTableWidget(Dialog)
        self.full_table.setShowGrid(True)
        self.full_table.setGridStyle(QtCore.Qt.SolidLine)
        self.full_table.setWordWrap(True)
        self.full_table.setCornerButtonEnabled(True)
        self.full_table.setRowCount(50)
        self.full_table.setColumnCount(10)
        self.full_table.setObjectName("full_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(149, 117, 61))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 117, 61))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.full_table.setItem(0, 0, item)
        self.verticalLayout.addWidget(self.full_table)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem16 = QtWidgets.QSpacerItem(20, 570, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem16)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_notarius.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">....</span><span style=\" font-size:24pt;\">Notarius</span><span style=\" font-size:24pt; color:#ffffff;\">....</span></p></body></html>"))
        self.button_tabla.setText(_translate("Dialog", "Tabla"))
        self.button_importar_excel.setText(_translate("Dialog", "Importar Excel"))
        self.button_agregar_usuario.setText(_translate("Dialog", "Agregar Usuario"))
        self.button_editar_privilegios.setText(_translate("Dialog", "Editar Privilegios"))
        self.button_logout.setText(_translate("Dialog", "Cerrar Sesión"))
        self.button_exportar.setText(_translate("Dialog", "     Exportar     "))
        self.full_table.setSortingEnabled(False)
        __sortingEnabled = self.full_table.isSortingEnabled()
        self.full_table.setSortingEnabled(False)
        self.full_table.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

