from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
import pyqtgraph as pg
from cplot_manager import PlotManager 
from file_manager import FileManager

class CSVDataViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Chara Technologies Assignment')
        self.setGeometry(100, 100, 800, 600)

        self.plot_manager = PlotManager()
        self.file_manager = FileManager()
        self.plot_widget = pg.PlotWidget()
        self.load_button = QPushButton("Load CSV File")
        self.load_button.clicked.connect(self.file_manager.load_csv)

        self.increase_button = QPushButton("Increase Amplitude")
        self.increase_button.clicked.connect(self.plot_manager.increase_amplitude)

        self.decrease_button = QPushButton("Decrease Amplitude")
        self.decrease_button.clicked.connect(self.plot_manager.decrease_amplitude)

        self.export_button = QPushButton("Export Graph")
        self.export_button.clicked.connect(self.file_manager.export_graph)

        amp_layout = QHBoxLayout()
        amp_layout.addWidget(self.increase_button)
        amp_layout.addWidget(self.decrease_button)
        
        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.plot_widget)
        layout.addLayout(amp_layout) 
        layout.addWidget(self.export_button)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.plot_manager.set_plot_widget(self.plot_widget)
        self.file_manager.set_plot_widget(self.plot_widget)
        self.file_manager.set_parent_window(self)

        self.legend = None  # Store legend reference

if __name__ == '__main__':
    pass  
