import os
import sys
#Obtener directorio base de programa, esto es util al momento de crear el instalador.
def getBaseDir():
    if getattr(sys, 'frozen', False):
        # we are running in a PyInstaller bundle
        basedir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        basedir = os.path.abspath(os.path.dirname(__file__))
    return basedir