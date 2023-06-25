from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
import sys
from PyQt.gui import Ui_Dialog
from PyQt.plot import RealTimePlot
from Pyserial.sensor_reader import SensorReader


class Controller:
    def __init__(self, parent):
        self.ui = Ui_Dialog()
        self.parent = parent
        self.maxSize = 10
        self.mode = 0
        self.pltWdgts = None

    def setupUI(self):
        self.ui.setupUi(self.parent)
        self.ui.BMI270Box.setVisible(False)
        self.ui.BME688Box.setVisible(False)        

        # Showing the QDialog
        self.parent.show()
    
    def setupPlots(self):
        if self.pltWdgts != None:
            for w in self.pltWdgts:
                w.deleteLater()
        
        match self.mode:
            case 0:
                self.pltWdgts = None
                return
            case 1:
                self.pltWdgts = [RealTimePlot(), RealTimePlot()]
                y_labels = ["Acc []",  "Gyro []"]
                titles = ["Aceleración", "Giro"]
            case 2:
                self.pltWdgts = [RealTimePlot(), RealTimePlot(), RealTimePlot(), RealTimePlot()]
                y_labels = ["Temp [C]", "Press [Pa]", "Hum []", "Gas []"]
                titles = ["Temperatura", "Presión", "Humedad", "Gas"]
        
        plots = [self.ui.Plot1, self.ui.Plot2, self.ui.Plot3, self.ui.Plot4]
        for i in range(len(self.pltWdgts)):
            self.pltWdgts[i].set_config(plots[i], y_labels[i], titles[i])

    def setSignals(self):
        self.ui.selectSensor.currentIndexChanged.connect(self.selectMode)
        self.ui.initConfigButton.clicked.connect(self.initConfig)
        self.ui.readDataButton.clicked.connect(self.readDataTask)

    # Initialize the configuration depending on the selected sensor
    def initConfig(self):
        conf = dict()
        match self.mode:
            case 0:
                popup = QtWidgets.QMessageBox(parent= self.parent)
                popup.setWindowTitle('Configuración')
                popup.setText('Selecciona un sensor primero')
                popup.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                popup.exec()
                return
            case 1:
                conf['AccSamp'] = self.ui.text_acc_sampling.toPlainText()
                conf['AccSen'] = self.ui.text_acc_sensibity.toPlainText()
                conf['GyroSamp'] = self.ui.text_gyro_sampling.toPlainText()
                conf['GyroSen'] = self.ui.text_gyro_sensibity.toPlainText()
            case 2:
                conf['Mode'] = self.ui.selectMode.currentIndex()


        popup = QtWidgets.QMessageBox(parent= self.parent)
        popup.setWindowTitle('Configuración')
        popup.setText('Configuración enviada a ESP-32')
        popup.setIcon(QtWidgets.QMessageBox.Icon.Information)
        popup.exec()

        print (conf)

    # Gets the sensor that has been selected
    def selectMode(self):
        index = self.ui.selectSensor.currentIndex()
        match index:
            case 0:
                self.ui.BMI270Box.setVisible(False)
                self.ui.BME688Box.setVisible(False)
            case 1:
                self.ui.BMI270Box.setVisible(True)
                self.ui.BME688Box.setVisible(False)
            case 2:
                self.ui.BMI270Box.setVisible(False)
                self.ui.BME688Box.setVisible(True)

        texto = self.ui.selectSensor.itemText(index)
        print("Sensor:", texto)
        self.mode = index
        self.setupPlots()

    def stop(self):
        print('Mori')
        return
    
    # Receives the new data and plots it
    def newData(self, x, data, plot_idx):
        self.pltWdgts[plot_idx].add_data(x, data)
    
    # Invokes a task in order to read the sensor data
    def readDataTask(self):
        # QThread object
        self.thread = QtCore.QThread()
        self.worker = SensorReader('/dev/ttyUSB0', 1, self.mode)
        self.worker.moveToThread(self.thread)
        # Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Plots the data received by the worker
        self.worker.progress.connect(self.newData)
        # Start the thread
        self.thread.start()

        self.ui.readDataButton.clicked.disconnect()
        self.ui.readDataButton.clicked.connect(self.endRead)
    
    # Stops the readData task
    def endRead(self):
        self.worker.end()
        self.ui.readDataButton.clicked.disconnect()
        self.ui.readDataButton.clicked.connect(self.readDataTask)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    cont = Controller(parent=Dialog)
    cont.setupUI()
    cont.setSignals() 
    sys.exit(app.exec_())
