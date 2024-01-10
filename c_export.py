from PyQt5.QtWidgets import QFileDialog
def export_graph(csv_viewer, plot_widget):
    if plot_widget.plotItem.curves:
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(csv_viewer, "Export Graph", "", "PNG Files (*.png)", options=options)
        if file_path:
            img = plot_widget.grab().toImage()
            img.save(file_path)