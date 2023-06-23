import serial as ser
import pprint
import time
from PyQt5.QtCore import QObject, pyqtSignal

pprinter = pprint.PrettyPrinter()

class SensorReader(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int, int)
    running = True

    def __init__(self, path2read, time, baud=115200) -> None:
        super().__init__()
        self.path = path2read
        self.baud = baud
        self.reader = ser.Serial()
        self.reader.port = path2read
        self.reader.baudrate = baud
        self.data = []
        self.t = time
    
    def run(self):
        print(f"Reading every {self.t}sec ... use ctrl+c to get all the data")
        self.reader.open()
        try:
            while self.running:
                str_data = self.reader.readline()
                str_data = str_data.decode().rstrip()
                self.data.append(str_data)
                print(str_data)
                self.emit(str_data)
                time.sleep(self.t)

        except KeyboardInterrupt:
            self.reader.close()
            print()
            pprinter.pprint(self.data)
        self.finished.emit()
    
    def end(self):
        self.running = False
    
    def emit(self, dat):
        data_id = 0
        self.progress.emit(dat, data_id)
            


if __name__ == '__main__':
    reader = SensorReader('/dev/ttyUSB0', 1)
    del reader.reader
    del reader
    
