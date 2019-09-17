from PyQt5 import QtCore
from design import *
from datetime import date,time,datetime
from time import sleep
import serial
import threading
import os

loopTimeInSeconds = 10
last_count = 0
last_light = 0.0
last_temp = 0.0

isViewOpen = False

#View Class
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.getData(self,last_temp,last_light)

    def updateView(self):
        self.ui.retranslateUi(self)

#Function Definations
def UpdateDB_Thread():
    count = getLastCount()
    while True:
        #Get your data here

        #Save your data here
        updateDB(count,last_temp,54,34)
       
        #Updation
        count += 1
        sleep(loopTimeInSeconds)

       
def OpenView_Thread():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())

    
#Threads to call the 2 methods
thread1 = threading.Thread(target = UpdateDB_Thread, args = ())
thread1.start()

thread2 = threading.Thread(target = OpenView_Thread,args=())
thread2.start()
