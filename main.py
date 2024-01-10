from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from csv_data_viewer import CSVDataViewer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chara Technologies Assignment')
        self.setGeometry(100, 100, 800, 600)

        self.setup_ui()

    def setup_ui(self):
        self.csv_viewer = CSVDataViewer(self)
        self.setCentralWidget(self.csv_viewer)
        self.add_export_option()

    def add_export_option(self):
        export_action = QAction('Export Graph as PNG', self)
        export_action.triggered.connect(self.csv_viewer.export_graph)

        file_menu = self.menuBar().addMenu('File')
        file_menu.addAction(export_action)

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
