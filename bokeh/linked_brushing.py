#Linked Brushing
#To link plots together at a data level, we can explicitly wrap the data in a ColumnDataSource. This allows us to reference columns by name.
#We can use a "select" tool to select points on one plot, and the linked points on the other plots will highlight.

from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
from bokeh.sampledata.autompg import autompg
from bokeh.plotting import figure 
from bokeh.io import output_notebook, show


source = ColumnDataSource(autompg)

options = dict(plot_width=300, plot_height=300,
               tools="pan,wheel_zoom,box_zoom,box_select,lasso_select")

p1 = figure(title="MPG by Year", **options)
p1.circle("yr", "mpg", color="blue", source=source)

p2 = figure(title="HP vs. Displacement", **options)
p2.circle("hp", "displ", color="green", source=source)

p3 = figure(title="MPG vs. Displacement", **options)
p3.circle("mpg", "displ", size="cyl", line_color="red", fill_color=None, source=source)

p = gridplot([[ p1, p2, p3]], toolbar_location="right")

show(p)