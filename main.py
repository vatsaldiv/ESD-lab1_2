from PyQt5 import QtCore
from design import *
from utilities import *
from datetime import date,time,datetime
from time import sleep
import serial
import threading
import os

loopTimeInSeconds = 5

#View Class
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def updateInterface(self):
        self.ui.updateGUI(self)

#Function Definations
def UpdateDB_Thread():
    last_count = 1
    last_light = 20.3
    last_temp = 25.2

    today = date.today()
    now = datetime.now()

    current_date = today.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M:%S")
    current_datetime = current_date + "_" + current_time
    while True:
        #Get your data here

        #Save your data here
        updateDB(last_count,last_temp,last_light,current_datetime)
       
        #Updation
        last_count += 1
        last_light += 1
        last_temp += 1

        today = date.today()
        now = datetime.now()

        current_date = today.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")
        current_datetime = current_date + "_" + current_time

        sleep(loopTimeInSeconds)
       
def OpenView_Thread():
    app = QtWidgets.QApplication([])
    application = mywindow()
    timer = QTimer()
    timer.timeout.connect(application.updateInterface)
    timer.start(1000)
    application.show()
    app.exec_()

#Threads to call the 2 methods
thread1 = threading.Thread(target = UpdateDB_Thread, args = ())
thread1.start()

thread2 = threading.Thread(target = OpenView_Thread,args=())
thread2.start()
