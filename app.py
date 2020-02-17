from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import layout_labjack
from ljm_wrapper import labjack_wrapper as lm
import time, math
import pyqtgraph as pg

class LabJackApp(QtWidgets.QMainWindow, layout_labjack.Ui_MainWindow):
    def __init__(self, parent=None):

        # ui component setup
        super(LabJackApp, self).__init__(parent)
        self.setupUi(self)
        self.ljm = lm.ljmWrapper()
        self.StartButton.clicked.connect(self.StartButtonClick)
        self.StopButton.clicked.connect(self.StopButtonClick)
        self.AnalogChannelDropDownList.addItems(self.ljm.ADCeNames)
        self.AnalogChannelDropDownList.activated[str].connect(self.AnalogChannelDropDownListOption)
        self.SampleRateSpinBox.valueChanged.connect(self.SampleRateChanged)
        
        # labjack setup
        self.timer = pg.QtCore.QTimer(self)
        self.prev_i = 0
        self.sampleRate = 1000
        self.isStartClicked = False
        self.isStopClicked = True
        self.AnalogChannelSelected = 0

    # GUI logic
    def CheckButtonState(self):
        if self.isStartClicked == True and self.isStopClicked == False:
            return True

        elif self.isStartClicked == False and self.isStopClicked == True:
            return False
    
    def StartButtonClick(self):
        print("Start clicked")
        self.isStartClicked = True
        self.isStopClicked = False
        self.ljm.analog_read_stream_setup([self.AnalogChannelSelected], self.sampleRate)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(0)
    

    def StopButtonClick(self):
        print("Stop clicked")
        self.ljm.analog_read_stream_stop()
        self.isStartClicked = False
        self.isStopClicked = True
        self.timer.stop()

    def AnalogChannelDropDownListOption(self, text):
        self.AnalogChannelSelected = int(str(text)[3:])
        print(f"{self.AnalogChannelSelected} option selected")

    def SampleRateChanged(self, text):
        self.sampleRate = int(text)*2
        print(f"Sample Rate Changed: {int(text)}")

    def update_plot(self):
        value = self.ljm.analog_read_stream()
        print(value)

        X = [float(i/0.01) for i in range(self.prev_i, self.prev_i+int(self.sampleRate/2))]
        self.prev_i = self.prev_i + int(self.sampleRate/2)
        # Y = [math.sin(X[i]) for i in range(2000)]
        Y = value[0]
        # Y1 = [math.cos(X[i]) for i in range(2000)]
        CenterPoint = self.prev_i - int(self.sampleRate/4)

        self.PlotWidget.setXRange(float(CenterPoint-5)/0.01, float(CenterPoint+5)/0.01)
        self.PlotWidget.plot(X,Y, clear=True)

def main():
    app = QApplication(sys.argv)
    form = LabJackApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
