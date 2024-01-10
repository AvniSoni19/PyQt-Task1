import sys
from PyQt5.QtWidgets import QApplication
from csv_data_viewer import CSVDataViewer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = CSVDataViewer()
    mainWindow.show()
    sys.exit(app.exec_())
