from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton
import pyqtgraph as pg
from a_load_csv import load_csv
from b_amplitude import increase_amplitude, decrease_amplitude
from c_export import export_graph

class CSVDataViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize attributes for UI components and data storage
        self.parent_window = parent
        self.plot_widget = pg.PlotWidget()
        self.load_button = QPushButton("Load CSV File")
        self.increase_button = QPushButton("Increase Amplitude")
        self.decrease_button = QPushButton("Decrease Amplitude")
        self.export_button = QPushButton("Export Graph")

        # Set up connections between buttons and their respective actions
        self.load_button.clicked.connect(self.load_csv)
        self.increase_button.clicked.connect(self.increase_amplitude)
        self.decrease_button.clicked.connect(self.decrease_amplitude)
        self.export_button.clicked.connect(self.export_graph)

        # Set up the layout for the user interface
        amp_layout = QHBoxLayout()
        amp_layout.addWidget(self.increase_button)
        amp_layout.addWidget(self.decrease_button)
        
        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.plot_widget)
        layout.addLayout(amp_layout) 
        layout.addWidget(self.export_button)
        self.setLayout(layout)

        # Initialize variables for storing legend reference and loaded data
        self.legend = None  # Reference to the legend associated with the plot
        self.data = None  # Store loaded CSV data

    # Callback method to load CSV file data
    def load_csv(self):
        load_csv(self)  # Invokes the load_csv function from a_load_csv module

    # Callback method to increase amplitude of the plot
    def increase_amplitude(self):
        increase_amplitude(self, self.plot_widget)  # Invokes increase_amplitude function from b_amplitude module

    # Callback method to decrease amplitude of the plot
    def decrease_amplitude(self):
        decrease_amplitude(self, self.plot_widget)  # Invokes decrease_amplitude function from b_amplitude module
        
    # Callback method to export the graph as a PNG file
    def export_graph(self):
        export_graph(self, self.plot_widget)  # Invokes export_graph function from c_export module
