from PyQt5 import QtCore
from design import *
from datetime import date,time,datetime
from time import sleep
import serial
import threading
import os

'''
ser = serial.Serial(port='COM15', baudrate=115200)

while True:
    
    bytes_data = ser.read(size = 3)
    print(bytes_data)

    encoding = 'utf-8'
    sting_data = str(bytes_data, encoding)
    print(string_data)

    values = string_data.strip().split(',')
    last_count, last_light, last_temp = [str(s) for s in values]

    ser.write('a')
    
    last_count = 1
    last_light = 20.3
    last_temp = 25.2

    today = date.today()
    now = datetime.now()

    current_date = today.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M:%S")
    current_datetime = current_date + "_" + current_time



    updateDB(last_count, last_temp, last_light, current_datetime)

    class mywindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(mywindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.getData(self,last_temp,last_light)
          
        def updateView(self):
            self.ui.retranslateUi(self)
        

    app = QtWidgets.QApplication([])
    application = mywindow()

    application.show()
    sys.exit(app.exec())

    last_count += 1
    last_light += 1
    last_temp += 1

    sleep(10)
'''

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
