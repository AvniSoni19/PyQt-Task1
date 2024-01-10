import pyqtgraph as pg

class PlotManager:
    def __init__(self):
        self.plot_widget = None

    def set_plot_widget(self, plot_widget):
        self.plot_widget = plot_widget

    def increase_amplitude(self):
        if self.plot_widget is not None:
            self.plot_widget.setYRange(self.plot_widget.getViewBox().viewRange()[1][0] * 1.2, self.plot_widget.getViewBox().viewRange()[1][1] * 1.2)

    def decrease_amplitude(self):
        if self.plot_widget is not None:
            self.plot_widget.setYRange(self.plot_widget.getViewBox().viewRange()[1][0] * 0.8, self.plot_widget.getViewBox().viewRange()[1][1] * 0.8)
