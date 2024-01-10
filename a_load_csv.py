from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog, QVBoxLayout, QListWidget, QDialogButtonBox
import pandas as pd
import pyqtgraph as pg

def load_csv(csv_viewer):
    # Open file dialog to select a CSV file
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getOpenFileName(csv_viewer.parent_window, "Load CSV File", "", "CSV Files (*.csv)", options=options)
    
    if file_path:
        try:
            # Read the CSV file using pandas
            data = pd.read_csv(file_path)
            
            # Extract columns for y-axes
            columns = data.columns.tolist()
            
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
                # Get selected columns
                selected_columns = [item.text() for item in list_widget.selectedItems()]
                csv_viewer.plot_widget.clear()
                x_data = range(len(data))  # Use the number of rows as x-axis
                csv_viewer.data = data  # Store data in the viewer for future use
                legend = []  # Store legend items
                
                if all_columns_label in selected_columns:
                    selected_columns.remove(all_columns_label)
                    
                    # Plot selected columns if numeric
                    for idx, col in enumerate(selected_columns):
                        if pd.api.types.is_numeric_dtype(data[col]):
                            color = pg.intColor(idx, hues=len(selected_columns))
                            plot = csv_viewer.plot_widget.plot(x_data, data[col], pen=color, name=f"y{idx+1} - {col}")
                            legend.append(plot)
                        else:
                            QMessageBox.warning(csv_viewer, "Warning", f"Column '{col}' contains non-numeric data and cannot be plotted.")
                    
                    # If no specific columns selected, plot all numeric columns
                    if not selected_columns:
                        for idx, col in enumerate(columns):
                            if pd.api.types.is_numeric_dtype(data[col]):
                                color = pg.intColor(idx, hues=len(columns))
                                plot = csv_viewer.plot_widget.plot(x_data, data[col], pen=color, name=f"y{idx+1} - {col}")
                                legend.append(plot)
                else:
                    # Plot selected columns if numeric
                    for idx, col in enumerate(selected_columns):
                        if pd.api.types.is_numeric_dtype(data[col]):
                            color = pg.intColor(idx, hues=len(selected_columns))
                            plot = csv_viewer.plot_widget.plot(x_data, data[col], pen=color, name=col)
                            legend.append(plot)
                        else:
                            QMessageBox.warning(csv_viewer, "Warning", f"Column '{col}' contains non-numeric data and cannot be plotted.")
                
                # Add legend to the plot at bottom-right corner
                legend_item = csv_viewer.plot_widget.addLegend()
                legend_item.setParentItem(csv_viewer.plot_widget.graphicsItem())
                legend_item.anchor((1, 1), (1, 1), offset=(-10, -10))  # Position the legend at bottom-right corner
                
                # Add labels only for displayed axes
                for plot in legend:
                    legend_item.addItem(plot, plot.name())
                
                csv_viewer.plot_widget.repaint()

        except Exception as e:
            QMessageBox.critical(csv_viewer, "Error", f"Failed to load CSV file: {str(e)}")
            return
