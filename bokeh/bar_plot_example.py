#Bar Plot Example

from bokeh.plotting import figure 
from bokeh.io import output_notebook, show

from bokeh.sampledata.autompg import autompg

grouped = autompg.groupby("yr")
mpg = grouped["mpg"]
avg = mpg.mean()
std = mpg.std()
years = list(grouped.groups.keys())

american = autompg[autompg["origin"]==1]
japanese = autompg[autompg["origin"]==3]

p = figure(title="MPG by Year (Japan and US)")

p.vbar(x=years, bottom=avg-std, top = avg+std, width=0.8, fill_alpha=0.2,line_color=None, legend="MPG 1 stddev")

p.circle(x=japanese["yr"], y=japanese["mpg"], size=10, alpha=0.5,
         color="red", legend="Japanese")

p.triangle(x=american["yr"], y=american["mpg"], size=10, alpha=0.3,
           color="blue", legend="American")

p.legend.location = "top_left"
show(p)

