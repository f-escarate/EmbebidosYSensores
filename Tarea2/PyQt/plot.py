import pyqtgraph as pg
from PyQt5 import QtWidgets

class RealTimePlot(pg.PlotWidget):
    
    max_size = 10
    def __init__(self, parent=None, background='default', plotItem=None, **kargs):
        super().__init__(parent, background, plotItem, **kargs)
        self.data_array = [[],[]]

    def set_config(self, plot, y_label, title):
        # Getting plot width and heigth
        plot_rect = plot.geometry()
        width = plot_rect.width()
        height = plot_rect.height()
        # Setting the plot size
        scene = QtWidgets.QGraphicsScene()
        plot.setScene(scene)
        plot.setHorizontalScrollBarPolicy(1)    # Horizontal Scroll Bar off
        plot.setVerticalScrollBarPolicy(1)      # Vertical Scroll Bar off
        self.setGeometry(0, 0, width, height)   # Setting Plot width and heigth
        # Plot labels and title
        self.setLabel(axis='bottom', text='x_axis')
        self.setLabel(axis='left', text=y_label)
        self.plotItem.setTitle(title)
        scene.addWidget(self)                   # Adding PlotWidget to scene

    def add_data(self, x, data):
        #print(self.data_array)
        self.data_array[1].append(data)
        self.data_array[0].append(x)

        if len(self.data_array[1])>self.max_size:
            del self.data_array[1][0]
            del self.data_array[0][0]
            
        self.clear()
        self.plot(self.data_array[0], self.data_array[1])