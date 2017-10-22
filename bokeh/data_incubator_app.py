#data incubator build the app:
#url: https://blog.thedataincubator.com/2015/09/painlessly-deploying-data-apps-with-bokeh-flask-and-heroku/


# A couple tricks that came in handy were adding in some retries to the API call:
import requests

#Set the stock we are interested in, AAPL is Apple stock code
stock = 'AAPL'

api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
#api_url = 'https://www.quandl.com/api/v3/datasets/EOD/AAPL.csv?api_key=YOURAPIKEY'1
session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
raw_data = session.get(api_url)

# Probably want to check that requests.Response is 200 - OK here 
# to make sure we got the content successfully.

# requests.Response has a function to return json file as python dict
aapl_stock = raw_data.json()

x = [] #dates 
y = [] #prices

for i in aapl_stock['data'][:]:
	x.append(i[1])
	y.append(i[4])

# and making sure to let Bokeh know it’s dealing with a DateTime index:

from bokeh.plotting import figure, show
plot = figure(tools="pan,wheel_zoom,box_zoom,box_select,lasso_select",
              title='Data from Quandle WIKI set',
              y_axis_label='Close price',
              x_axis_label='Open')
              #x_axis_type='datetime')
plot.circle(x, y, legend="test", line_color="red")


show(plot)





