from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from gui import Ui_Dialog
from worker import Worker


class Controller:
    def __init__(self, parent):
        self.ui = Ui_Dialog()
        self.parent = parent
        self.maxSize = 10
        self.data_arrays = [[],[],[],[]]
        self.mode = 0

    def setupUI(self):
        self.ui.setupUi(self.parent)
        self.ui.BMI270Box.setVisible(False)
        self.ui.BME688Box.setVisible(False)        
        self.setupPlots()

        # Showing the QDialog
        self.parent.show()
    
    def setupPlots(self):
        plots = [self.ui.Plot1, self.ui.Plot2, self.ui.Plot3, self.ui.Plot4]
        self.pltWdgts = [pg.PlotWidget(), pg.PlotWidget(), pg.PlotWidget(), pg.PlotWidget()]

        for i in range(4):
            # Getting plot width and heigth
            plot_rect = plots[i].geometry()
            width = plot_rect.width()
            height = plot_rect.height()
            # Setting the plot size
            scene = QtWidgets.QGraphicsScene()
            plots[i].setScene(scene)
            plots[i].setHorizontalScrollBarPolicy(1)            # Horizontal Scroll Bar off
            plots[i].setVerticalScrollBarPolicy(1)              # Vertical Scroll Bar off
            self.pltWdgts[i].setGeometry(0, 0, width, height)   # Setting Plot width and heigth
            scene.addWidget(self.pltWdgts[i])                   # Adding PlotWidget to scene

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

    def stop(self):
        print('Mori')
        return
    
    # Receives the new data and plots it
    def newData(self, data, plot_idx):
        self.data_arrays[plot_idx].append(data)
        if len(self.data_arrays[plot_idx])>self.maxSize:
            del self.data_arrays[plot_idx][0]
        self.pltWdgts[plot_idx].clear()
        self.pltWdgts[plot_idx].plot(self.data_arrays[plot_idx])
    
    # Invokes a task in order to read the sensor data
    def readDataTask(self):
        # QThread object
        self.thread = QtCore.QThread()
        self.worker = Worker()
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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    cont = Controller(parent=Dialog)
    cont.setupUI()
    cont.setSignals()

    cont.newData(1, 0)
    cont.newData(2, 0)
    cont.newData(3, 0)
    cont.newData(4, 0)
    cont.newData(5, 0)
    cont.newData(6, 0)
    cont.newData(7, 0)
    cont.newData(8, 0)
    cont.newData(9, 0)
    
    
    sys.exit(app.exec_())
