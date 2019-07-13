'''
Main file to launch GUI and control for sewer anti-blast project.
Working and tested 7.5 for basic functionality
Buttons with no actions disabled from UI file.

Edit: Tested with GitHub Desktop integration.
'''

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtWidgets, QtGui,  QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,  QInputDialog, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from labjack import ljm
import time, math, random, datetime
import numpy as np
from SWBmainwindow import Ui_MainWindow
import sys

# Define globals and session variables
headerList = ['Time', 'P1 (PSI)', 'P2 (PSI)']
global sampleRate

sampleRate = 0.25



class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.centralWidget.setStyleSheet("background-image: url(C:/Users/chris.antle/Documents/Anti-Blast/background.jpg);background-position: center;")
        #self.startSessionPrompt()

        try:
            self.labJackSetUp()
        except:
            self.LJMerrorPrompt()

        self.ui.plotWidget.setBackground(background=[0, 0, 0, 80])
        self.ui.plotWidget.setTitle(title="Real Time Pressure")
        self.ui.plotWidget.showGrid(True, True, 0.5)
        #self.ui.plotWidget.enableAutoRange('horizontal', True)
        #self.ui.plotWidget.addLegend()
        self.ui.plotWidget.setLabel('bottom', 'Elapsed Time', 's')
        self.ui.plotWidget.setLabel('left', 'Pressure', 'PSI')

        self.ui.sampleLCD.display(sampleRate)


        self.ui.setFileBTN.clicked.connect(lambda:self.saveFile())
        self.ui.startSessionBTN.clicked.connect(lambda:self.runSession())
        self.ui.saveSessionBTN.clicked.connect(lambda:self.saveFile(sessionData))
        self.ui.newSessionBTN.clicked.connect(lambda:self.clearAll())


    def labJackSetUp(self):
        global handle
        handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier
        # Get info and print settings
        info = ljm.getHandleInfo(handle)
        print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
              "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
              (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))
        print("  ")

    def sampleData(self):
        #test = datetime.datetime.now().strftime("%H:%M:%S")
        #print(test)
        timeStamp = datetime.datetime.now().strftime("%H:%M:%S")
        V1 = ljm.eReadName(handle, "AIN0") # Sample labjack analog input 1
        V2 = ljm.eReadName(handle, "AIN1") # Sample labjack analog input 2
        P1 = 61.121*V1-43.622
        P2 = 61.121*V2-43.622

        pressureSample = [timeStamp, P1, P2] # add data to local list

        self.ui.pressureLCD1.display(P1) # display data on GUI
        self.ui.pressureLCD2.display(P2) # display data on GUI

        # Print for debug
        # print("P1 Voltage Reading: " + str(P1))
        # print("P2 Voltage Reading: " + str(P2))

        return pressureSample

    def runSession(self):
        sessionActive = self.ui.startSessionBTN.isChecked() # Check initial state
        global sessionData
        if sessionActive:
            sessionData = []  # Generate empty list for local session data
            self.ui.startSessionBTN.setText("STOP")

            while sessionActive:
                QApplication.processEvents()  # Check to see if session ended
                sessionActive = self.ui.startSessionBTN.isChecked() # Check that session is running
                #print("While Loop Parameter: " + str(sessionActive))
                # Dummy data for debug
                #data1 = random.randint(0,100)
                #data2 = random.randint(0,100)
                #sessionData.append([data1,data2]) # Add sampled data to session as 2D component

                sessionData.append(self.sampleData()) # sample data and write to session list
                self.plotSessionData(sessionData)

                time.sleep(sampleRate)
        else:
            self.ui.startSessionBTN.setText("START")

    def plotSessionData(self, sessionData):
        self.ui.plotWidget.clear()
        self.ui.plotWidget.addLegend()
        curve1 = self.ui.plotWidget.plot(pen='r', name="P1")
        curve2 = self.ui.plotWidget.plot(pen='g', name="P2")
        P1 = []
        P2 = []
        i = 0

        for set in sessionData: #grab invidudal data points and make a list of just pressure values
            P1.append(sessionData[i][1])
            P2.append(sessionData[i][2])
            i+=1

        curve1.setData(P1)
        curve2.setData(P2)
        #app.processEvents()
        timer = QtCore.QTimer()
        P1A = np.array(P1)
        P2A = np.array(P2)

        def update():
            global curve1, curve2, P1A
            curve1.setData(P1A)
            curve2.setData(P2A)
        timer.timeout.connect(update)
        timer.start(100)

    def checkFile(self):
        print ("Checking file path and name")

    def clearAll(self):
        self.ui.pressureLCD1.display(0.00)  # display data on GUI
        self.ui.pressureLCD2.display(0.00)  # display data on GUI
        self.ui.plotWidget.clear()

    def saveFile(self, data):
        savePrompt = QMessageBox.information(self, 'Save Session', 'Save Data?',
                                             QMessageBox.Save | QMessageBox.Cancel)
        if savePrompt == QMessageBox.Save:
            print("Saving File")
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self, "Test Session Output File)", "",
                                                      "All Files (*);;Text Files (*.txt)", options=options)

            with open(fileName + ".txt", 'w') as txtfile:
                txtfile.write(', '.join(str(headers) for headers in headerList) + '\n')
                for line in data:
                    #print(str(line))
                    txtfile.write(", ".join(map(str, line)) + '\n')

                self.ui.fileNameEdit.setText(fileName + ".txt")
                #self.ui.filePathEdit.setText("N/A")

                print("File Saved")
                print(" ")

        elif savePrompt == QMessageBox.Cancel:
            print("Data not saved")

        else:
            print("Default")

    def startSessionPrompt(self):
        startPrompt = QMessageBox.information(self, 'New Session Started','New Test Session Started, Data File Name and Path Needed',
                                              QMessageBox.Ok | QMessageBox.Cancel)
        if startPrompt == QMessageBox.Ok:
            self.saveFile()
        else:
            sys.exit(app.exec_())

    def LJMerrorPrompt(self):
        errorPrompt = QMessageBox.information(self, 'ERROR','LabJack Device Not Detected - Connect and Re-open Application',
                                              QMessageBox.Ok | QMessageBox.Cancel)
        if errorPrompt == QMessageBox.Ok:
            sys.exit(app.exec_())
        else:
            sys.exit(app.exec_())

class LJMError(Exception):
    def __init__(self):
        self.errorMSG = "LabJack Not Found Error"

    def __str__(self):
        return(repr(self.value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    w.show()
    sys.exit(app.exec_())