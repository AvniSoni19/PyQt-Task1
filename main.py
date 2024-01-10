from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from csv_data_viewer import CSVDataViewer  # Importing the CSVDataViewer class

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chara Technologies Assignment')  # Setting the window title
        self.setGeometry(100, 100, 800, 600)  # Setting window geometry

        self.setup_ui()  # Setting up the user interface

    def setup_ui(self):
        # Creating an instance of CSVDataViewer and setting it as the central widget
        self.csv_viewer = CSVDataViewer(self)
        self.setCentralWidget(self.csv_viewer)

        self.add_export_option()  # Adding export option to the menu bar

    def add_export_option(self):
        # Creating an 'Export Graph as PNG' action in the File menu
        export_action = QAction('Export Graph as PNG', self)
        export_action.triggered.connect(self.csv_viewer.export_graph)  # Connecting action to export_graph method

        # Adding 'Export Graph as PNG' action to the File menu
        file_menu = self.menuBar().addMenu('File')
        file_menu.addAction(export_action)

if __name__ == '__main__':
    app = QApplication([])  # Creating a PyQt application instance
    main_window = MainWindow()  # Creating an instance of MainWindow
    main_window.show()  # Displaying the main window
    app.exec_()  # Executing the application
