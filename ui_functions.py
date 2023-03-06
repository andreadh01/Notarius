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
from main import *
from PyQt5 import QtGui,QtCore,QtWidgets
# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True


def centerOnScreen (self):
        '''centerOnScreen()
Centers the window on the screen.'''
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
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
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(
                QtGui.QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(
                QtGui.QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
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
            width = self.ui.leftMenuBg.width()
            maxExtend = 240
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QtCore.QPropertyAnimation(
                self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = 240
            color = 'background-color: white;'
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(
                        style.replace('background-color: #e3ddcc;', ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))

        start_box_animation(self, width, widthRightBox, "left")

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    # def toggleRightBox(self, enable):
    #     if enable:
    #         # GET WIDTH
    #         width = self.ui.extraRightBox.width()
    #         widthLeftBox = self.ui.extraLeftBox.width()
    #         maxExtend = Settings.RIGHT_BOX_WIDTH
    #         color = Settings.BTN_RIGHT_BOX_COLOR
    #         standard = 0

    #         # GET BTN STYLE
    #         style = self.ui.settingsTopBtn.styleSheet()

    #         # SET MAX WIDTH
    #         if width == 0:
    #             widthExtended = maxExtend
    #             # SELECT BTN
    #             self.ui.settingsTopBtn.setStyleSheet(style + color)
    #             if widthLeftBox != 0:
    #                 style = self.ui.toggleLeftBox.styleSheet()
    #                 self.ui.toggleLeftBox.setStyleSheet(
    #                     style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
    #         else:
    #             widthExtended = standard
    #             # RESET BTN
    #             self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

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
        self.left_box = QtCore.QPropertyAnimation(
            self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(500)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QtCore.QPropertyAnimation(
            self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(500)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QtCore.QParallelAnimationGroup()
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
    for w in self.ui.topMenu.findChildren(QtWidgets.QPushButton):
        if w.objectName() == widget:
            w.setStyleSheet(selectMenu(w.styleSheet()))
# RESET SELECTION
def resetStyle(self, widget):
    for w in self.ui.topMenu.findChildren(QtWidgets.QPushButton):
        if w.objectName() != widget:
            w.setStyleSheet(deselectMenu(w.styleSheet()))
# IMPORT THEMES FILES QSS/CSS
# ///////////////////////////////////////////////////////////////
def theme(self, file, useCustomTheme):
    if useCustomTheme:
        str = open(file, 'r').read()
        self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
def uiDefinitions(self):
#         def dobleClickMaximizeRestore(event):
#             # IF DOUBLE CLICK CHANGE STATUS
#             if event.type() == QEvent.MouseButtonDblClick:
#                 QTimer.singleShot(
#                     250, lambda: UIFunctions.maximize_restore(self))
#         #self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

#         if Settings.ENABLE_CUSTOM_TITLE_BAR:
#             # STANDARD TITLE BAR
#             self.setWindowFlags(Qt.FramelessWindowHint)
#             self.setAttribute(Qt.WA_TranslucentBackground)

#             # MOVE WINDOW / MAXIMIZE / RESTORE
#             def moveWindow(event):
#                 # IF MAXIMIZED CHANGE TO NORMAL
#                 if UIFunctions.returStatus(self):
#                     UIFunctions.maximize_restore(self)
#                 # MOVE WINDOW
#                 if event.buttons() == Qt.LeftButton:
#                     self.move(self.pos() + event.globalPos() - self.dragPos)
#                     self.dragPos = event.globalPos()
#                     event.accept()
#             #self.ui.titleRightInfo.mouseMoveEvent = moveWindow

#             # CUSTOM GRIPS
#             self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
#             self.right_grip = CustomGrip(self, Qt.RightEdge, True)
#             self.top_grip = CustomGrip(self, Qt.TopEdge, True)
#             self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

#         else:
#             
# #            self.ui.minimizeAppBtn.hide()
#  #           self.ui.maximizeRestoreAppBtn.hide()
#   #          self.ui.closeAppBtn.hide()
# #            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QtCore.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
#        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
#        self.sizegrip.setStyleSheet(
#            "width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
#        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
      #  self.ui.maximizeRestoreAppBtn.clicked.connect(
       #     lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
       # self.ui.closeAppBtn.clicked.connect(lambda: self.close())


    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS
