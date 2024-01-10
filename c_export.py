from PyQt5.QtWidgets import QFileDialog

def export_graph(csv_viewer, plot_widget):
    # Check if there are curves to export in the plot widget
    if plot_widget.plotItem.curves:
        # Define options for the file dialog
        options = QFileDialog.Options()

        # Open a file dialog to get the save file path
        file_path, _ = QFileDialog.getSaveFileName(
            csv_viewer, "Export Graph", "", "PNG Files (*.png)", options=options
        )

        # Check if a file path is selected
        if file_path:
            # Grab the plot widget content as an image
            img = plot_widget.grab().toImage()

            # Save the image to the specified file path as a PNG file
            img.save(file_path)
