import numpy as np
import pandas as pd
from os.path import dirname, join

from bokeh.io import output_notebook, show
from bokeh.plotting import figure
import bokeh.sampledata

from bokeh.layouts import column, grid
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure, output_file, show


output_file("sent_analysis.html")
headlines = pd.read_csv(join(dirname(__file__), '/Users/rich/dev/Sentiment.Analysis/news_api_20200514', 'headlines2.csv'))


def sent_tab():
    """plot for sentiment change on a day to day"""

    source = ColumnDataSource(data=dict(
        x=headlines['date'],
        y=headlines['score'],
        # name=headlines['headlines'],
    ))
    p = figure(x_axis_type="datetime", x_axis_label='Date', y_axis_label='sentiment score', xplot_width=400, plot_height=400, title="Sent. Analysis of Headlines")

# add a circle renderer with x and y coordinates, size, color, and alpha
    p.line('x', 'y', size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)

# show the results
    show(p)


if __name__ == '__main__':
    sent_tab()
