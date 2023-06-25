import serial as ser
import pprint
import time
from PyQt5.QtCore import QObject, pyqtSignal

pprinter = pprint.PrettyPrinter()

class SensorReader(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(float, float, int)
    running = True

    def __init__(self, path2read, time, mode, baud=115200) -> None:
        super().__init__()
        self.path = path2read
        self.baud = baud
        self.reader = ser.Serial()
        self.reader.port = path2read
        self.reader.baudrate = baud
        self.data = []
        self.t = time
        self.mode = mode
    
    def run(self):
        print(f"Reading every {self.t}sec ... use ctrl+c to get all the data")
        #self.reader.open()
        try:
            while self.running:
                #str_data = self.reader.readline()
                #str_data = str_data.decode().rstrip()
                #self.data.append(str_data)
                #print(str_data)
                self.emit("str_data")
                time.sleep(self.t)

        except KeyboardInterrupt:
            self.reader.close()
            print()
            pprinter.pprint(self.data)
        self.finished.emit()
    
    def end(self):
        self.running = False
    
    def emit(self, dat):
        dat = dat.split(', ')
        #dat = [1, 22.2, 2.3, 1, 43]
        
        match self.mode:
            case 1:
                self.progress.emit(float(dat[0]), float(dat[1]), 0)
                self.progress.emit(float(dat[0]), float(dat[2]), 1)
            case 2:
                self.progress.emit(float(dat[0]), float(dat[1]), 0)
                self.progress.emit(float(dat[0]), float(dat[2]), 1)
                self.progress.emit(float(dat[0]), float(dat[3]), 2)
                self.progress.emit(float(dat[0]), float(dat[4]), 3)
                


if __name__ == '__main__':
    reader = SensorReader('/dev/ttyUSB0', 1)
    del reader.reader
    del reader
    
