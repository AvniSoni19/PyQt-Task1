def increase_amplitude(csv_viewer, plot_widget):
    if csv_viewer.data is not None:
        y_range = plot_widget.viewRange()[1]  # Get the Y-axis range
        new_min = y_range[0] * 1.2  # Increase the range by 20%
        new_max = y_range[1] * 1.2
        plot_widget.setYRange(new_min, new_max)

def decrease_amplitude(csv_viewer, plot_widget):
    if csv_viewer.data is not None:
        y_range = plot_widget.viewRange()[1]  # Get the Y-axis range
        new_min = y_range[0] * 0.8  # Decrease the range by 20%
        new_max = y_range[1] * 0.8
        plot_widget.setYRange(new_min, new_max)
