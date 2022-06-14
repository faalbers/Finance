from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys
import yfinance as yf

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._main = QWidget()
        self.setCentralWidget(self._main)
        layout = QVBoxLayout(self._main)

        canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(NavigationToolbar(canvas, self))
        layout.addWidget(canvas)

        self.ax = canvas.figure.subplots()

        msft = yf.Ticker('msft')
        history = msft.history(period='max')

        self.ax.plot(history['Close'])

app = QApplication(sys.argv)

aw = AppWindow()
aw.show()

sys.exit(app.exec())
