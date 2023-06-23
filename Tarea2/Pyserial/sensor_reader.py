import serial as ser
import pprint
import time
pprinter = pprint.PrettyPrinter()
class SensorReader:
    def __init__(self, path2read, baud=115200):
        self.path = path2read
        self.baud = baud
        self.reader = ser.Serial()
        self.reader.port = path2read
        self.reader.baudrate = baud
        self.data = []
    
    def read_every_t_seconds(self, t):
        print(f"Reading every {t}sec ... use ctrl+c to get all the data")
        self.reader.open()
        try:
            while True:
                str_data = self.reader.readline()
                str_data = str_data.decode().rstrip()
                self.data.append(str_data)
                print(str_data)
                time.sleep(t)
        except KeyboardInterrupt:
            self.reader.close()
            print()
            pprinter.pprint(self.data)
            


if __name__ == '__main__':
    reader = SensorReader('/dev/ttyUSB0')
    reader.read_every_t_seconds(1)
    del reader.reader
    del reader
    
