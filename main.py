
from design import *
from datetime import date,time,datetime
from time import sleep
import serial

'''
ser = serial.Serial(port='COM15', baudrate=115200)
'''
while True:
    '''
    bytes_data = ser.read(size = 3)
    print(bytes_data)

    encoding = 'utf-8'
    sting_data = str(bytes_data, encoding)
    print(string_data)

    values = string_data.strip().split(',')
    last_count, last_light, last_temp = [str(s) for s in values]

    ser.write('a')
    '''
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
        '''   
        def updateView(self):
            self.ui.retranslateUi(self)
        '''

    app = QtWidgets.QApplication([])
    application = mywindow()

    application.show()
    sys.exit(app.exec())

    last_count += 1
    last_light += 1
    last_temp += 1

    sleep(10)
