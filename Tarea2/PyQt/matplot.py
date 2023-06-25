

import sys
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLayout
from PyQt5.QtCore import QTimer, QObject

class MatPlot(QWidget):
    def __init__(self):
        super().__init__()

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0,0,0,0)

        self.setLayout(layout)

        # Initialize empty data
        self.x_data = []
        self.y_data = []

        self.plot_data()

    def plot_data(self):
        self.figure.clear()  # Clear the previous plot

        # Plot the data
        x_data = self.x_data[-10:]  # Retrieve the 10 most recent x data points
        y_data = self.y_data[-10:]  # Retrieve the corresponding y data points
        plt.plot(x_data, y_data)

        # Set plot title, labels, etc. if needed
        plt.title("Real-time Plot")
        plt.xlabel("X")
        plt.ylabel("Y")

        # Redraw the plot on the canvas
        self.canvas.draw()

    def add_data(self, data):
        # Generate random data for demonstration purposes
        x = len(self.x_data) + 1  # Increment x value
        y = data                  # Random y value

        self.x_data.append(x)
        self.y_data.append(y)

        self.plot_data()