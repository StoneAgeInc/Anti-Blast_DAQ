# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SWBmainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 666)
        self.W1 = QtWidgets.QWidget(MainWindow)
        self.W1.setStyleSheet("QWidget#W1{\n"
"background-color: rgb(80,80,80);\n"
"background-image: url(\"C:/Users/chris.antle/Documents/Anti-Blast/backgroundDark.jpg\");\n"
"opacity: 0.5;\n"
"background-position: center;\n"
"}\n"
"\n"
"")
        self.W1.setObjectName("W1")
        self.gridLayout = QtWidgets.QGridLayout(self.W1)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.W1)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 5, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 6, 1, 1)
        self.controlWidget = QtWidgets.QWidget(self.W1)
        self.controlWidget.setStyleSheet("QWidget#controlWidget\n"
"{\n"
"  background-color: rgb(0, 0, 0,80);\n"
"  color: rgb(220,220,220);\n"
"  font-size: 11px;\n"
"  outline: none;\n"
"opacity: 0.5;\n"
"}\n"
"\n"
"/**** QWidget (disabled) ****/\n"
"QWidget:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}")
        self.controlWidget.setObjectName("controlWidget")
        self.controlLayout = QtWidgets.QVBoxLayout(self.controlWidget)
        self.controlLayout.setContentsMargins(11, 11, 11, 11)
        self.controlLayout.setSpacing(6)
        self.controlLayout.setObjectName("controlLayout")
        self.line_3 = QtWidgets.QFrame(self.controlWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.controlLayout.addWidget(self.line_3)
        self.label_7 = QtWidgets.QLabel(self.controlWidget)
        self.label_7.setObjectName("label_7")
        self.controlLayout.addWidget(self.label_7)
        self.line_6 = QtWidgets.QFrame(self.controlWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.controlLayout.addWidget(self.line_6)
        self.startSessionBTN = QtWidgets.QPushButton(self.controlWidget)
        self.startSessionBTN.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(230,230,230);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(150,95,15);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"}\n"
"\n"
"/**** QPushButton (disabled) ****/\n"
"QPushButton:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.startSessionBTN.setCheckable(True)
        self.startSessionBTN.setAutoDefault(False)
        self.startSessionBTN.setObjectName("startSessionBTN")
        self.controlLayout.addWidget(self.startSessionBTN)
        self.saveSessionBTN = QtWidgets.QPushButton(self.controlWidget)
        self.saveSessionBTN.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(230,230,230);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(150,95,15);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(40,150,200), stop: 1 rgb(90,200,255));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QPushButton (disabled) ****/\n"
"QPushButton:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.saveSessionBTN.setObjectName("saveSessionBTN")
        self.controlLayout.addWidget(self.saveSessionBTN)
        self.newSessionBTN = QtWidgets.QPushButton(self.controlWidget)
        self.newSessionBTN.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(230,230,230);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(150,95,15);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(40,150,200), stop: 1 rgb(90,200,255));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QPushButton (disabled) ****/\n"
"QPushButton:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.newSessionBTN.setObjectName("newSessionBTN")
        self.controlLayout.addWidget(self.newSessionBTN)
        self.line_14 = QtWidgets.QFrame(self.controlWidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.controlLayout.addWidget(self.line_14)
        self.label_12 = QtWidgets.QLabel(self.controlWidget)
        self.label_12.setObjectName("label_12")
        self.controlLayout.addWidget(self.label_12)
        self.line_13 = QtWidgets.QFrame(self.controlWidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.controlLayout.addWidget(self.line_13)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.setFileBTN = QtWidgets.QPushButton(self.controlWidget)
        self.setFileBTN.setEnabled(False)
        self.setFileBTN.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(230,230,230);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(150,95,15);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(40,150,200), stop: 1 rgb(90,200,255));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QPushButton (disabled) ****/\n"
"QPushButton:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.setFileBTN.setObjectName("setFileBTN")
        self.horizontalLayout_5.addWidget(self.setFileBTN)
        self.clearBTN = QtWidgets.QPushButton(self.controlWidget)
        self.clearBTN.setEnabled(False)
        self.clearBTN.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(230,230,230);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(150,95,15);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(40,150,200), stop: 1 rgb(90,200,255));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QPushButton (disabled) ****/\n"
"QPushButton:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.clearBTN.setObjectName("clearBTN")
        self.horizontalLayout_5.addWidget(self.clearBTN)
        self.controlLayout.addLayout(self.horizontalLayout_5)
        self.fileNameLayout = QtWidgets.QHBoxLayout()
        self.fileNameLayout.setSpacing(6)
        self.fileNameLayout.setObjectName("fileNameLayout")
        self.controlLayout.addLayout(self.fileNameLayout)
        self.filePathLayout = QtWidgets.QHBoxLayout()
        self.filePathLayout.setSpacing(6)
        self.filePathLayout.setObjectName("filePathLayout")
        self.label_14 = QtWidgets.QLabel(self.controlWidget)
        self.label_14.setObjectName("label_14")
        self.filePathLayout.addWidget(self.label_14)
        self.fileNameEdit = QtWidgets.QLineEdit(self.controlWidget)
        self.fileNameEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
"QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.fileNameEdit.setReadOnly(True)
        self.fileNameEdit.setObjectName("fileNameEdit")
        self.filePathLayout.addWidget(self.fileNameEdit)
        self.controlLayout.addLayout(self.filePathLayout)
        self.label = QtWidgets.QLabel(self.controlWidget)
        self.label.setObjectName("label")
        self.controlLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.controlWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.sampleLCD = QtWidgets.QLCDNumber(self.controlWidget)
        self.sampleLCD.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.sampleLCD.setObjectName("sampleLCD")
        self.horizontalLayout_2.addWidget(self.sampleLCD)
        self.label_9 = QtWidgets.QLabel(self.controlWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.motorDutyLCD = QtWidgets.QLCDNumber(self.controlWidget)
        self.motorDutyLCD.setEnabled(False)
        self.motorDutyLCD.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.motorDutyLCD.setObjectName("motorDutyLCD")
        self.horizontalLayout_2.addWidget(self.motorDutyLCD)
        self.controlLayout.addLayout(self.horizontalLayout_2)
        self.label_11 = QtWidgets.QLabel(self.controlWidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.controlLayout.addWidget(self.label_11)
        self.gridLayout.addWidget(self.controlWidget, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.W1)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 4, 1, 1)
        self.sensorWidget = QtWidgets.QWidget(self.W1)
        self.sensorWidget.setStyleSheet("QWidget#sensorWidget\n"
"{\n"
"  background-color: rgb(0, 0, 0,80);\n"
"  color: rgb(220,220,220);\n"
"  font-size: 11px;\n"
"  outline: none;\n"
"opacity: 0.5;\n"
"}\n"
"\n"
"/**** QWidget (disabled) ****/\n"
"QWidget:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}")
        self.sensorWidget.setObjectName("sensorWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sensorWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_15 = QtWidgets.QFrame(self.sensorWidget)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout.addWidget(self.line_15)
        self.label_8 = QtWidgets.QLabel(self.sensorWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.line_4 = QtWidgets.QFrame(self.sensorWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.label_15 = QtWidgets.QLabel(self.sensorWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.sensorWidget)
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"  background-color: transparent;\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"}\n"
"\n"
"/**** QLabel (disabled) ****/\n"
"QLabel\n"
"{\n"
"}")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.pressureLCD1 = QtWidgets.QLCDNumber(self.sensorWidget)
        self.pressureLCD1.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.pressureLCD1.setObjectName("pressureLCD1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pressureLCD1)
        self.label_3 = QtWidgets.QLabel(self.sensorWidget)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"  background-color: transparent;\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"}\n"
"\n"
"/**** QLabel (disabled) ****/\n"
"QLabel\n"
"{\n"
"}")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pressureLCD2 = QtWidgets.QLCDNumber(self.sensorWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pressureLCD2.setFont(font)
        self.pressureLCD2.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.pressureLCD2.setObjectName("pressureLCD2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pressureLCD2)
        self.label_5 = QtWidgets.QLabel(self.sensorWidget)
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"  background-color: transparent;\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"}\n"
"\n"
"/**** QLabel (disabled) ****/\n"
"QLabel\n"
"{\n"
"}")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.pressureLCD4 = QtWidgets.QLCDNumber(self.sensorWidget)
        self.pressureLCD4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressureLCD4.sizePolicy().hasHeightForWidth())
        self.pressureLCD4.setSizePolicy(sizePolicy)
        self.pressureLCD4.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.pressureLCD4.setObjectName("pressureLCD4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pressureLCD4)
        self.lcdNumber = QtWidgets.QLCDNumber(self.sensorWidget)
        self.lcdNumber.setEnabled(False)
        self.lcdNumber.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.lcdNumber.setObjectName("lcdNumber")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lcdNumber)
        self.label_10 = QtWidgets.QLabel(self.sensorWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet("QLabel\n"
"{\n"
"  background-color: transparent;\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"}\n"
"\n"
"/**** QLabel (disabled) ****/\n"
"QLabel\n"
"{\n"
"}")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.verticalLayout.addLayout(self.formLayout)
        self.line_16 = QtWidgets.QFrame(self.sensorWidget)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.verticalLayout.addWidget(self.line_16)
        self.label_16 = QtWidgets.QLabel(self.sensorWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setSpacing(6)
        self.formLayout_4.setObjectName("formLayout_4")
        self.s1MSLabel = QtWidgets.QLabel(self.sensorWidget)
        self.s1MSLabel.setObjectName("s1MSLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1MSLabel)
        self.s1MSLineEdit = QtWidgets.QLineEdit(self.sensorWidget)
        self.s1MSLineEdit.setEnabled(False)
        self.s1MSLineEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
"QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.s1MSLineEdit.setObjectName("s1MSLineEdit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1MSLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.verticalLayout.addLayout(self.formLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.line_11 = QtWidgets.QFrame(self.sensorWidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout.addWidget(self.line_11)
        self.gridLayout.addWidget(self.sensorWidget, 5, 5, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plotWidget = PlotWidget(self.W1)
        self.plotWidget.setStyleSheet("QWidget#plotWidget\n"
"{\n"
"  background-color: rgb(0, 0, 0,80);\n"
"  color: rgb(220,220,220);\n"
"  font-size: 11px;\n"
"  outline: none;\n"
"opacity: 0.5;\n"
"}\n"
"\n"
"/**** QWidget (disabled) ****/\n"
"QWidget:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}")
        self.plotWidget.setObjectName("plotWidget")
        self.verticalLayout_4.addWidget(self.plotWidget)
        self.gridLayout.addLayout(self.verticalLayout_4, 7, 1, 1, 5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 5)
        MainWindow.setCentralWidget(self.W1)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">CONTROL</span></p></body></html>"))
        self.startSessionBTN.setText(_translate("MainWindow", "START"))
        self.saveSessionBTN.setText(_translate("MainWindow", "SAVE SESSION"))
        self.newSessionBTN.setText(_translate("MainWindow", "NEW"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">FILE</span></p></body></html>"))
        self.setFileBTN.setText(_translate("MainWindow", "SET"))
        self.clearBTN.setText(_translate("MainWindow", "CLEAR"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Output File:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Test Parameters</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Fs (Hz)</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", ".."))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic; color:#ffffff;\">ANTI-BLAST DAQ</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">SENSORS</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\">PRESSURE</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">P1 (PSI)</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">P2 (PSI)</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">P3 (PSI)</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">P4 (PSI)</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\">AIR SPEED</span></p></body></html>"))
        self.s1MSLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">S1 (m/s)</span></p></body></html>"))


from pyqtgraph import PlotWidget
