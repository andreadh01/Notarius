# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from functools import partial
import importlib
import re
from usuarios import getAllPermisos, getUsuarioLogueado
from main import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

lista_botones = []
def centerOnScreen (self):
        '''centerOnScreen()
Centers the window on the screen.'''
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2)) 
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.appMargins.setContentsMargins(0, 0, 0, 0)
            self.maximizeRestoreAppBtn.setToolTip("Restore")
            self.maximizeRestoreAppBtn.setIcon(
                QIcon(u":/icons/images/icons/icon_restore.png"))
            self.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.appMargins.setContentsMargins(0, 0, 0, 0)
            self.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.maximizeRestoreAppBtn.setIcon(
                QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.leftMenuBg.width()
            maxExtend = 240
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(
                self.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.extraLeftBox.width()
            widthRightBox = self.extraRightBox.width()
            maxExtend = 240
            color = 'background-color: white;'
            standard = 0

            # GET BTN STYLE
            style = self.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.settingsTopBtn.styleSheet()
                    self.settingsTopBtn.setStyleSheet(
                        style.replace('background-color: #e3ddcc;', ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.toggleLeftBox.setStyleSheet(style.replace(color, ''))

        start_box_animation(self, width, widthRightBox, "left")

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    # def toggleRightBox(self, enable):
    #     if enable:
    #         # GET WIDTH
    #         width = self.extraRightBox.width()
    #         widthLeftBox = self.extraLeftBox.width()
    #         maxExtend = Settings.RIGHT_BOX_WIDTH
    #         color = Settings.BTN_RIGHT_BOX_COLOR
    #         standard = 0

    #         # GET BTN STYLE
    #         style = self.settingsTopBtn.styleSheet()

    #         # SET MAX WIDTH
    #         if width == 0:
    #             widthExtended = maxExtend
    #             # SELECT BTN
    #             self.settingsTopBtn.setStyleSheet(style + color)
    #             if widthLeftBox != 0:
    #                 style = self.toggleLeftBox.styleSheet()
    #                 self.toggleLeftBox.setStyleSheet(
    #                     style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
    #         else:
    #             widthExtended = standard
    #             # RESET BTN
    #             self.settingsTopBtn.setStyleSheet(style.replace(color, ''))

    #         UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0

        # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(
            self.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(500)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(
            self.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(500)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
def selectMenu(getStyle):
    select = getStyle + """
border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgb(116, 91, 47), stop:0.5 rgba(85, 170, 255, 0));
background-color: #e3ddcc;
color:rgb(116, 91, 47) ;
"""
    return select
# DESELECT
def deselectMenu(getStyle):
    deselect = getStyle.replace("""
border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgb(116, 91, 47), stop:0.5 rgba(85, 170, 255, 0));
background-color: #e3ddcc;
color:rgb(116, 91, 47) ;
""", "")
    return deselect
# START SELECTION
def selectStandardMenu(self, widget):
    for w in self.topMenu.findChildren(QPushButton):
        if w.objectName() == widget:
            w.setStyleSheet(selectMenu(w.styleSheet()))
# RESET SELECTION
def resetStyle(self, widget):
    for w in self.topMenu.findChildren(QPushButton):
        if w.objectName() != widget:
            w.setStyleSheet(deselectMenu(w.styleSheet()))
# IMPORT THEMES FILES QSS/CSS
# ///////////////////////////////////////////////////////////////
def theme(self, file, useCustomTheme):
    if useCustomTheme:
        str = open(file, 'r').read()
        self.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
def uiDefinitions(self):
        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

def checarPermisos(self):
        lista_botones.clear()
        permisos_usuario = getAllPermisos()
        for tabla, permisos in permisos_usuario.items():
            if permisos['read'] != '': 
                if ['Tablas','cells'] not in lista_botones:
                    lista_botones.append(['Tablas','cells'])
            if permisos['write'] != '': 
                if ['AgregarRegistro','add'] not in lista_botones:
                    lista_botones.append(['AgregarRegistro','add'])
            if tabla == 'usuario':
                lista_botones.clear() 
                lista_botones.extend([['Tablas','cells'],['AgregarRegistro','add'],['VerUsuarios','group'],['EditarPrivilegios','edit'], ['RegistrarUsuario','add-user']])
                return

def createButtons(self):
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)

        for button in lista_botones:
            name = button[0]
            icon = button[1]
            
            setattr(self, f"btn_{name.lower()}", QPushButton(self.topMenu))
            btn = getattr(self, f"btn_{name.lower()}")
            btn.setObjectName(f"btn_{name.lower()}")
            sizePolicy.setHeightForWidth(
            btn.sizePolicy().hasHeightForWidth())
            btn.setSizePolicy(sizePolicy)
            btn.setMinimumSize(QSize(0, 45))
            btn.setFont(font)
            btn.setCursor(QCursor(Qt.PointingHandCursor))
            btn.setLayoutDirection(Qt.LeftToRight)
            btn.setStyleSheet(f"background-image: url(:/resources/resources/icons/{icon}.png);")
            btn.setText(QCoreApplication.translate("MainWindow",re.sub(r"(\w)([A-Z])", r"\1 \2",name).capitalize(),None))
            self.verticalLayout_8.addWidget(btn)

            createWidget(self, name)
            btn.clicked.connect(partial(buttonClick,self, btn))
            
def getListaBotones():
    return lista_botones
def buttonClick(self, btn):
        # GET BUTTON CLICKED
        btnName = btn.objectName()
        print('clicked'+btnName)

        # SHOW HOME PAGE
        if btnName == "btn_tablas":
            self.stackedWidget.setCurrentWidget(self.tablas)
            resetStyle(self, btnName)
            btn.setStyleSheet(selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_agregarregistro":
            self.stackedWidget.setCurrentWidget(self.agregarregistro)
            resetStyle(self, btnName)
            btn.setStyleSheet(selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_registrarusuario":
            self.stackedWidget.setCurrentWidget(
                self.registrarusuario)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            resetStyle(self, btnName)
            btn.setStyleSheet(selectMenu(
                btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_verusuarios":
            self.stackedWidget.setCurrentWidget(self.verusuarios)
            resetStyle(self, btnName)
            btn.setStyleSheet(selectMenu(btn.styleSheet()))

        if btnName == "btn_editarprivilegios":
            self.stackedWidget.setCurrentWidget(self.editarprivilegios)
            resetStyle(self, btnName)
            btn.setStyleSheet(selectMenu(btn.styleSheet()))
            
def createWidget(self, name):
        module = importlib.import_module(f"pages.{name}")
        instance = getattr(module, name)()
        setattr(self, name.lower(), instance)
        widget = getattr(self, name.lower())
        self.stackedWidget.addWidget(widget)
    