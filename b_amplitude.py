def increase_amplitude(csv_viewer, plot_widget):
    """
    Increase the amplitude (Y-axis range) of the plot by 20%.
    
    Parameters:
    - csv_viewer: The CSVDataViewer instance.
    - plot_widget: The PlotWidget instance to adjust.
    """
    if csv_viewer.data is not None:
        # Get the current Y-axis range
        y_range = plot_widget.viewRange()[1]
        
        # Increase the range by 20%
        new_min = y_range[0] * 1.2
        new_max = y_range[1] * 1.2
        
        # Set the new Y-axis range
        plot_widget.setYRange(new_min, new_max)

def decrease_amplitude(csv_viewer, plot_widget):
    """
    Decrease the amplitude (Y-axis range) of the plot by 20%.
    
    Parameters:
    - csv_viewer: The CSVDataViewer instance.
    - plot_widget: The PlotWidget instance to adjust.
    """
    if csv_viewer.data is not None:
        # Get the current Y-axis range
        y_range = plot_widget.viewRange()[1]
        
        # Decrease the range by 20%
        new_min = y_range[0] * 0.8
        new_max = y_range[1] * 0.8
        
        # Set the new Y-axis range
        plot_widget.setYRange(new_min, new_max)
