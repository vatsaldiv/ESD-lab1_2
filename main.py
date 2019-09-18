from PyQt5 import QtCore
from design import *
from utilities import *
from datetime import date,time,datetime
from time import sleep
import serial
import threading
import os

ser = serial.Serial(port='COM17', baudrate=9600)
ser.write('U'.encode())

#loopTimeInSeconds = 5


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
    
    while True:
        today = date.today()
        now = datetime.now()

        current_date = today.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")
        current_datetime = current_date + "_" + current_time

        #Get your data here
        bytes_data = ser.read(3)
        last_count = int.from_bytes([bytes_data[0]], byteorder='big', signed=False)
        print(last_count)
        last_light = int.from_bytes([bytes_data[1]], byteorder='big', signed=False)
        last_light = 255-last_light
        last_light = round(last_light, 2)
        print(last_light)
        last_temp = int.from_bytes([bytes_data[2]], byteorder='big', signed=False)
        last_temp = last_temp*(85/172)
        last_temp = round(last_temp, 2)
        print(last_temp)

        ser.write('U'.encode())

        #sleep(loopTimeInSeconds)

        #calibrate your data here


        #Save your data here
        updateDB(last_count, last_temp, last_light, current_datetime)

       
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
