from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton
import pyqtgraph as pg
from a_load_csv import load_csv
from b_amplitude import increase_amplitude, decrease_amplitude
from c_export import export_graph

class CSVDataViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.plot_widget = pg.PlotWidget()
        self.load_button = QPushButton("Load CSV File")
        self.load_button.clicked.connect(self.load_csv)

        self.increase_button = QPushButton("Increase Amplitude")
        self.increase_button.clicked.connect(self.increase_amplitude)

        self.decrease_button = QPushButton("Decrease Amplitude")
        self.decrease_button.clicked.connect(self.decrease_amplitude)

        self.export_button = QPushButton("Export Graph")
        self.export_button.clicked.connect(self.export_graph)

        amp_layout = QHBoxLayout()
        amp_layout.addWidget(self.increase_button)
        amp_layout.addWidget(self.decrease_button)
        
        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.plot_widget)
        layout.addLayout(amp_layout) 
        layout.addWidget(self.export_button)
        self.setLayout(layout)

        self.legend = None  # Store legend reference
        self.data = None

    def load_csv(self):
        load_csv(self)

    def increase_amplitude(self):
        increase_amplitude(self, self.plot_widget)  

    def decrease_amplitude(self):
        decrease_amplitude(self, self.plot_widget)
        
    def export_graph(self):
        export_graph(self, self.plot_widget)
