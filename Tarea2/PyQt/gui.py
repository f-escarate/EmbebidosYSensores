# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(774, 798)
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(110, 80, 101, 21))
        self.label_30.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_30.setObjectName("label_30")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(220, 80, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.selectSensor = QtWidgets.QComboBox(Dialog)
        self.selectSensor.setGeometry(QtCore.QRect(120, 110, 181, 31))
        self.selectSensor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selectSensor.setObjectName("selectSensor")
        self.selectSensor.addItem("")
        self.selectSensor.addItem("")
        self.selectSensor.addItem("")
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(250, 10, 221, 41))
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setFrameShape(QtWidgets.QFrame.Box)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Plot1 = QtWidgets.QGraphicsView(Dialog)
        self.Plot1.setGeometry(QtCore.QRect(60, 370, 291, 181))
        self.Plot1.setFrameShape(QtWidgets.QFrame.Box)
        self.Plot1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Plot1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Plot1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Plot1.setObjectName("Plot1")
        self.Plot2 = QtWidgets.QGraphicsView(Dialog)
        self.Plot2.setGeometry(QtCore.QRect(390, 370, 291, 181))
        self.Plot2.setFrameShape(QtWidgets.QFrame.Box)
        self.Plot2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Plot2.setObjectName("Plot2")
        self.Plot3 = QtWidgets.QGraphicsView(Dialog)
        self.Plot3.setGeometry(QtCore.QRect(60, 590, 291, 181))
        self.Plot3.setFrameShape(QtWidgets.QFrame.Box)
        self.Plot3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Plot3.setObjectName("Plot3")
        self.Plot4 = QtWidgets.QGraphicsView(Dialog)
        self.Plot4.setGeometry(QtCore.QRect(390, 590, 291, 181))
        self.Plot4.setFrameShape(QtWidgets.QFrame.Box)
        self.Plot4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Plot4.setObjectName("Plot4")
        self.label_datos1 = QtWidgets.QLabel(Dialog)
        self.label_datos1.setGeometry(QtCore.QRect(120, 340, 151, 21))
        self.label_datos1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_datos1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_datos1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_datos1.setObjectName("label_datos1")
        self.label_datos2 = QtWidgets.QLabel(Dialog)
        self.label_datos2.setGeometry(QtCore.QRect(440, 340, 151, 21))
        self.label_datos2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_datos2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_datos2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_datos2.setObjectName("label_datos2")
        self.label_datos3 = QtWidgets.QLabel(Dialog)
        self.label_datos3.setGeometry(QtCore.QRect(120, 560, 151, 21))
        self.label_datos3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_datos3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_datos3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_datos3.setObjectName("label_datos3")
        self.label_datos4 = QtWidgets.QLabel(Dialog)
        self.label_datos4.setGeometry(QtCore.QRect(440, 560, 151, 21))
        self.label_datos4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_datos4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_datos4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_datos4.setObjectName("label_datos4")
        self.initConfigButton = QtWidgets.QPushButton(Dialog)
        self.initConfigButton.setGeometry(QtCore.QRect(140, 150, 141, 31))
        self.initConfigButton.setObjectName("initConfigButton")
        self.readDataButton = QtWidgets.QPushButton(Dialog)
        self.readDataButton.setGeometry(QtCore.QRect(160, 260, 111, 41))
        self.readDataButton.setObjectName("readDataButton")
        self.BMI270Box = QtWidgets.QGroupBox(Dialog)
        self.BMI270Box.setGeometry(QtCore.QRect(420, 60, 251, 261))
        self.BMI270Box.setObjectName("BMI270Box")
        self.text_acc_sampling = QtWidgets.QTextEdit(self.BMI270Box)
        self.text_acc_sampling.setGeometry(QtCore.QRect(120, 50, 104, 31))
        self.text_acc_sampling.setObjectName("text_acc_sampling")
        self.text_acc_sensibity = QtWidgets.QTextEdit(self.BMI270Box)
        self.text_acc_sensibity.setGeometry(QtCore.QRect(120, 100, 104, 31))
        self.text_acc_sensibity.setObjectName("text_acc_sensibity")
        self.labelAcc = QtWidgets.QLabel(self.BMI270Box)
        self.labelAcc.setGeometry(QtCore.QRect(70, 20, 121, 21))
        self.labelAcc.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.labelAcc.setObjectName("labelAcc")
        self.labelAccSens = QtWidgets.QLabel(self.BMI270Box)
        self.labelAccSens.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.labelAccSens.setObjectName("labelAccSens")
        self.labelAccSampleRate = QtWidgets.QLabel(self.BMI270Box)
        self.labelAccSampleRate.setGeometry(QtCore.QRect(20, 100, 91, 31))
        self.labelAccSampleRate.setObjectName("labelAccSampleRate")
        self.LabelGyro = QtWidgets.QLabel(self.BMI270Box)
        self.LabelGyro.setGeometry(QtCore.QRect(70, 140, 121, 21))
        self.LabelGyro.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.LabelGyro.setObjectName("LabelGyro")
        self.labelGyroSens = QtWidgets.QLabel(self.BMI270Box)
        self.labelGyroSens.setGeometry(QtCore.QRect(20, 170, 91, 31))
        self.labelGyroSens.setObjectName("labelGyroSens")
        self.text_gyro_sampling = QtWidgets.QTextEdit(self.BMI270Box)
        self.text_gyro_sampling.setGeometry(QtCore.QRect(120, 170, 104, 31))
        self.text_gyro_sampling.setObjectName("text_gyro_sampling")
        self.labelGyroSampleRate = QtWidgets.QLabel(self.BMI270Box)
        self.labelGyroSampleRate.setGeometry(QtCore.QRect(20, 220, 91, 31))
        self.labelGyroSampleRate.setObjectName("labelGyroSampleRate")
        self.text_gyro_sensibity = QtWidgets.QTextEdit(self.BMI270Box)
        self.text_gyro_sensibity.setGeometry(QtCore.QRect(120, 220, 104, 31))
        self.text_gyro_sensibity.setObjectName("text_gyro_sensibity")
        self.BME688Box = QtWidgets.QGroupBox(Dialog)
        self.BME688Box.setEnabled(True)
        self.BME688Box.setGeometry(QtCore.QRect(420, 60, 251, 261))
        self.BME688Box.setObjectName("BME688Box")
        self.label_31 = QtWidgets.QLabel(self.BME688Box)
        self.label_31.setGeometry(QtCore.QRect(40, 50, 181, 21))
        self.label_31.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_31.setObjectName("label_31")
        self.selectMode = QtWidgets.QComboBox(self.BME688Box)
        self.selectMode.setGeometry(QtCore.QRect(30, 80, 181, 31))
        self.selectMode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selectMode.setObjectName("selectMode")
        self.selectMode.addItem("")
        self.selectMode.addItem("")
        self.BME688Box.raise_()
        self.BMI270Box.raise_()
        self.label_30.raise_()
        self.progressBar.raise_()
        self.selectSensor.raise_()
        self.Title.raise_()
        self.Plot1.raise_()
        self.Plot2.raise_()
        self.Plot3.raise_()
        self.Plot4.raise_()
        self.label_datos1.raise_()
        self.label_datos2.raise_()
        self.label_datos3.raise_()
        self.label_datos4.raise_()
        self.initConfigButton.raise_()
        self.readDataButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_30.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Sensor activo</span></p></body></html>"))
        self.selectSensor.setCurrentText(_translate("Dialog", "<Ninguno>"))
        self.selectSensor.setItemText(0, _translate("Dialog", "<Ninguno>"))
        self.selectSensor.setItemText(1, _translate("Dialog", "BMI270"))
        self.selectSensor.setItemText(2, _translate("Dialog", "BMI688"))
        self.Title.setText(_translate("Dialog", "Configuracion Sensor"))
        self.label_datos1.setText(_translate("Dialog", "Datos 1: <Datos>"))
        self.label_datos2.setText(_translate("Dialog", "Datos 2: <Datos>"))
        self.label_datos3.setText(_translate("Dialog", "Datos 3: <Datos>"))
        self.label_datos4.setText(_translate("Dialog", "Datos 4: <Datos>"))
        self.initConfigButton.setText(_translate("Dialog", "Iniciar configuración"))
        self.readDataButton.setText(_translate("Dialog", "Iniciar captación \n"
" de datos"))
        self.BMI270Box.setTitle(_translate("Dialog", "BMI270"))
        self.labelAcc.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">Acelerómetro</span></p></body></html>"))
        self.labelAccSens.setText(_translate("Dialog", "Sensibilidad"))
        self.labelAccSampleRate.setText(_translate("Dialog", "Frecuencia de \n"
" muestro"))
        self.LabelGyro.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">Giroscopio</span></p></body></html>"))
        self.labelGyroSens.setText(_translate("Dialog", "Sensibilidad"))
        self.labelGyroSampleRate.setText(_translate("Dialog", "Frecuencia de \n"
" muestro"))
        self.BME688Box.setTitle(_translate("Dialog", "BME688"))
        self.label_31.setText(_translate("Dialog", "Modo de Funcionamiento"))
        self.selectMode.setItemText(0, _translate("Dialog", "Paralelo"))
        self.selectMode.setItemText(1, _translate("Dialog", "Forzado"))
