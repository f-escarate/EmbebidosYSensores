from gui import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets

class Controller:

    def __init__(self, parent):
        self.ui = Ui_Dialog()
        self.parent = parent

    def setupUI(self):
        self.ui.setupUi(self.parent)
        self.ui.BMI270Box.setVisible(False)
        self.ui.BME688Box.setVisible(False)
        self.parent.show()
        

    def setSignals(self):
        self.ui.selectSensor.currentIndexChanged.connect(self.leerModoOperacion)
        #self.ui.boton_detener.clicked.connect(self.criticalError)
        #self.ui.boton_configuracion.clicked.connect(self.leerConfiguracion)

    def leerConfiguracion(self):
        conf = dict()
        conf['AccSamp'] = self.ui.text_acc_sampling.toPlainText()
        conf['AccSen'] = self.ui.text_acc_sensibity.toPlainText()
        print (conf)
        return conf

    def leerModoOperacion(self):
        index = self.ui.selectSensor.currentIndex()
        texto = self.ui.selectSensor.itemText(index)
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


        print(texto)
        return texto

    def criticalError(self):
        popup = QtWidgets.QMessageBox(parent= self.parent)
        popup.setWindowTitle('ERROR MASIVO')
        popup.setText('QUE HAS APRETADO, NOS HAS CONDENADO A TODOS')
        popup.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        popup.exec()
        return

    def stop(self):
        print('Mori')
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    cont = Controller(parent=Dialog)
    cont.setupUI()
    cont.setSignals()
    sys.exit(app.exec_())
