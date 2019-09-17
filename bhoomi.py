#this code was written as a part of ESD L1
#It is a simple GUI built to display values stored in a csv file
#the storage and obtaining of relevant values shall take place in the atmel studios code

from PyQt5.QtWidgets import QLabel,QPushButton,QMainWindow,QApplication,QVBoxLayout,QHBoxLayout,QComboBox,QWidget
import sys
from PyQt5.QtCore import QTimer
import serial


def read_serial():
    m = '2'
    i = 0
    print('9')
    return m


class Main_Window(QWidget):

    def __init__(self):

        self.cnt=1

        QMainWindow.__init__(self)

        self.widget=QWidget()

        self.i=0 #instance counter of sorts

        self.av=0

        temp_av_lb = QLabel("Average Temperature")

        self.temp_av = QLabel(self)
        self.temp_av.setText('uninitiated')

        temp_curr_lb = QLabel("Current Temperature")

        self.temp_curr = QLabel(self)
        self.temp_curr.setText('uninitiated')

        self.temp_curr.move(12,12)

        self.temp_av.move(12,42)

        self.setGeometry(150, 150,80,100)

        self.qTimer=QTimer()

        self.qTimer.setInterval(1000)

        self.qTimer.timeout.connect(self.getSensorValue)

        self.qTimer.start()





    def getSensorValue(self):
        self.cnt+=1

        m=read_serial()
        #print ("in func")
        self.prev = self.i
        self.i = int(m)
        self.av = (self.av*self.prev + self.i)/self.i
        #print("incremented")

        self.temp_curr.setText('%f'%self.av)
        self.temp_av.setText('%f'%self.i)



app = QApplication(sys.argv)
#s=serial.Serial('COM11')
win=Main_Window()
win.show()
sys.exit(app.exec_())







