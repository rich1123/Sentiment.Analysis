import pandas as pd
from os.path import dirname, join

from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

from b_graphs.histogram import histogram_tab
from b_graphs.density import density_tab
from b_graphs.table import table_tab
from b_graphs.draw_map import map_tab
from b_graphs.routes import route_tab

# Using included state data from Bokeh for map
from bokeh.sampledata.us_states import data as states

# Read data into dataframes
headlines = pd.read_csv(join(dirname(__file__), 'news_api_20200514', 'headlines2.csv')
                        ,
                      # index_col=0).dropna()

# Create each of the tabs
tab1 = histogram_tab(tweets)
tab2 = density_tab(flights)
tab3 = table_tab(flights)
tab4 = map_tab(map_data, states)
tab5 = route_tab(flights)

# Put all the tabs into one application
tabs = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5])

# Put the tabs in the current document for display
curdoc().add_root(tabs)
