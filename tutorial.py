"""
INSTALL PyQt:
-------------
    pip install pyqt5
    pip install pyqt5-tools # installs the designer UI

Qt Designer UI:
----------------
    - Find the executable in Python installation 
        eg: C:\Program Files\Python39\Lib\site-packages\qt5_applications\Qt\bin
    - Basically find in "\Lib\site-packages\" folder
    - Create a desktop Shortcut and launch....
    - Designer saves as '.ui' file...
    - convert the UI file to a py code
        " pyuic5 -x tutorials.ui -o tutMainWin.py "

"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Use class to arrange all the required
# functionality in one container
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        
        # main window coords
        # parms: x, y, width, height
        self.setGeometry(200,200,300,300) 

        # set window title
        self.setWindowTitle("Tutorial Py Qt5")
        self.initUI()

    # ---------------------------------------------
    # a main function for our class
    def initUI(self):
    
        # init a label control (set its parent)
        # bind to class instance
        self.label = QtWidgets.QLabel(self) 

        # set properties
        self.label.setText("My test Label")  # text
        self.label.move(50,25)               # position
        # ---------------------------------------------
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Click Me")
        self.button1.move(50, 75)

        # assign button click event handler
        self.button1.clicked.connect(self.button1_Clicked)

    # ---------------------------------------------
    # Button event handler
    def button1_Clicked(self):
        self.label.setText("You pressed the button")
        # call update to refresh controls
        self.update() 
    
    # ---------------------------------------------
    # Update Window controls
    def update(self):
        self.label.adjustSize()


# ------------------------------------------------------------
# MAIN APPLICATION FUNCTION
# we need to have an application to run
def window():

    # init application
    app = QApplication(sys.argv)

    # option 2
    # init main window
    #win = QMainWindow()

    # option 2
    # instantiate MyWindow Class
    win = MyWindow() 

    # display window to user
    win.show()

    # cleanly exit the application
    # this waits for app to end 
    # and allows a clean exit
    sys.exit(app.exec_())
# ------------------------------------------------------------

# Call the main function
window()
# ------------------------------------------------------------