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
        #self.ui.updateGUI(self)

    def updateInterface(self):
        self.ui.updateGUI(self)

#Function Definations
def UpdateDB_Thread():
    #count = getLastCount()
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
    application.populate()
'''
def UpdateGUI_Thread():
    sleep (5)
    mywindow().updateInterface()
'''
#Threads to call the 2 methods
thread1 = threading.Thread(target = UpdateDB_Thread, args = ())
thread1.start()

thread2 = threading.Thread(target = OpenView_Thread,args=())
thread2.start()
'''
thread3 = threading.Thread(target = UpdateGUI_Thread,args=())
thread3.start()
'''

'''
ser = serial.Serial(port='COM15', baudrate=115200)

bytes_data = ser.read(size = 3)
print(bytes_data)

encoding = 'utf-8'
sting_data = str(bytes_data, encoding)
print(string_data)

values = string_data.strip().split(',')
last_count, last_light, last_temp = [str(s) for s in values]

ser.write('a')
'''

