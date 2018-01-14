from PyQt4 import QtCore,QtGui 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os
import bs4
import urllib
import threading
import time
import requests
import webbrowser

class MainWindow(QWidget):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.btc = ""
        

    def window(self):
        self.setGeometry(100,100,600,700)

        close = QPushButton(self)
        close.setGeometry(550,0,50,50)
        # close.setStyleSheet(".QPushButton{background-color:transparent;border:0;border-bottom:0px solid #34495e;} .QPushButton:hover{background-color:"+DEFAULT_COLOR_HOVER+";} .QPushButton:pressed{border-top:2px solid "+DEFAULT_COLOR_HOVER+";}")
        close.setIcon(QIcon(resource_path(r"Icons\close.png")))
        close.setIconSize(QSize(13,13))
        close.setCursor(Qt.PointingHandCursor)
        close.clicked.connect(self.close)
        
        minim = QPushButton(self)
        minim.setGeometry(500,0,50,50)
        # minim.setStyleSheet(".QPushButton{background-color:transparent;border:0;border-bottom:0px solid #34495e;} .QPushButton:hover{background-color:"+DEFAULT_COLOR_HOVER+";} .QPushButton:pressed{border-top:2px solid "+DEFAULT_COLOR_HOVER+";}")
        minim.setIcon(QIcon(resource_path(r"Icons\minim.png")))
        minim.setIconSize(QSize(15,15))
        minim.setCursor(Qt.PointingHandCursor)
        minim.clicked.connect(self.showMinimized)

        thread = threading.Thread(target=self.animate)
        thread.start()

        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        self.setWindowTitle("Tomos Mining")
        pos1 = self.x()
        pos2 = self.y()
        position_animator(self,pos1,900,pos1,pos2,duration=600)
        self.setWindowIcon(QIcon(resource_path(r"Icons\icon.png")))
        self.show()
    def animate(self):
        opcty = 0.0
        for i in range(11):
            time.sleep(0.06)
            self.setWindowOpacity(opcty)
            opcty+=0.1

def position_animator(obj = None,from_x = 0,from_y = 0,to_x = 0,to_y = 0,duration=500):
    animation = QPropertyAnimation(obj,"geometry",obj)
    animation.setStartValue(QRect(from_x,from_y,obj.width(),obj.height()))
    animation.setEndValue(QRect(to_x,to_y,obj.width(),obj.height()))
    animation.setDuration(duration)
    animation.setEasingCurve(QEasingCurve.OutQuart)
    animation.start()

def size_animator(obj = None,from_width = 0,from_height = 0,to_width = 0,to_height = 0,duration=500):
    animation = QPropertyAnimation(obj,"geometry",obj)
    animation.setStartValue(QRect(obj.x(),obj.y(),from_width,from_height))
    animation.setEndValue(QRect(obj.x(),obj.y(),to_width,to_height))
    animation.setDuration(duration)
    animation.setEasingCurve(QEasingCurve.OutQuart)
    animation.start()
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wndw = MainWindow()
    wndw.window()
    sys.exit(app.exec_())