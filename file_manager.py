from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog, QDialogButtonBox,QListWidget, QVBoxLayout
import pyqtgraph as pg
import pandas as pd

class FileManager:
    def __init__(self):
        self.plot_widget = None
        self.parent_window = None

    def set_plot_widget(self, plot_widget):
        self.plot_widget = plot_widget

    def set_parent_window(self, parent_window):
        self.parent_window = parent_window

    def load_csv(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self.parent_window, "Load CSV File", "", "CSV Files (*.csv)", options=options)
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                
                # Extract columns for y-axes
                columns = self.data.columns.tolist()
                
                # Create a dialog box for selecting multiple columns
                dialog = QDialog()
                dialog.setWindowTitle("Select Y-Axis Data Columns")
                layout = QVBoxLayout()
                list_widget = QListWidget()
                
                # Add an option to select all columns together
                all_columns_label = "Select All Columns"
                list_widget.addItem(all_columns_label)
                
                list_widget.addItems(columns)
                layout.addWidget(list_widget)
                buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                buttons.accepted.connect(dialog.accept)
                buttons.rejected.connect(dialog.reject)
                layout.addWidget(buttons)
                dialog.setLayout(layout)
                
                if dialog.exec_():
                    selected_columns = [item.text() for item in list_widget.selectedItems()]
                    self.plot_widget.clear()
                    x_data = range(len(self.data))  # Use the number of rows as x-axis
                    
                    if self.legend:
                        self.legend.clear()  # Clear the legend before adding new labels
                    
                    legend = []
                    if all_columns_label in selected_columns:
                        selected_columns.remove(all_columns_label)
                        for idx, col in enumerate(selected_columns):
                            if pd.api.types.is_numeric_dtype(self.data[col]):
                                color = pg.intColor(idx, hues=len(selected_columns))
                                plot = self.plot_widget.plot(x_data, self.data[col], pen=color, name=f"y{idx+1} - {col}")
                                legend.append(plot)
                            else:
                                QMessageBox.warning(self, "Warning", f"Column '{col}' contains non-numeric data and cannot be plotted.")
                        if not selected_columns:  # If no specific columns selected, plot all numeric columns
                            for idx, col in enumerate(columns):
                                if pd.api.types.is_numeric_dtype(self.data[col]):
                                    color = pg.intColor(idx, hues=len(columns))
                                    plot = self.plot_widget.plot(x_data, self.data[col], pen=color, name=f"y{idx+1} - {col}")
                                    legend.append(plot)
                    else:
                        for idx, col in enumerate(selected_columns):
                            if pd.api.types.is_numeric_dtype(self.data[col]):
                                color = pg.intColor(idx, hues=len(selected_columns))
                                plot = self.plot_widget.plot(x_data, self.data[col], pen=color, name=col)
                                legend.append(plot)
                            else:
                                QMessageBox.warning(self, "Warning", f"Column '{col}' contains non-numeric data and cannot be plotted.")
                    
                    # Add legend to the plot at bottom-right corner
                    self.legend = self.plot_widget.addLegend()
                    self.legend.setParentItem(self.plot_widget.graphicsItem())
                    self.legend.anchor((1, 1), (1, 1), offset=(-10, -10))  # Position the legend at bottom-right corner
                    
                    # Add labels only for displayed axes
                    for idx, plot in enumerate(legend):
                        if plot.isVisible():
                            self.legend.addItem(plot, plot.name())

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load CSV file: {str(e)}")
                return
        pass

    def export_graph(self):
        if self.plot_widget.plotItem.curves:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "Export Graph", "", "PNG Files (*.png)", options=options)
            if file_path:
                # Get the plot widget as an image
                img = self.plot_widget.grab().toImage()
                img.save(file_path)