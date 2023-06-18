from PyQt5.QtCore import QObject, pyqtSignal
from time import sleep

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int, int)
    running = True

    def run(self):
        """Long-running task."""
        while self.running:
            sleep(0.3)
            # Acá se debería recibir los datos desde la esp32 con pyserial
            data = 3
            data_id = 2
            self.progress.emit(data, data_id)
        self.finished.emit()
    
    def end(self):
        self.running = False