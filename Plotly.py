import Pull
import Calc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import chart_studio.plotly as py
import chart_studio

username = 'marcomanoppo'
api_key= 'CsZIbUAdvRrdFO6HbH5v'

chart_studio.tools.set_credentials_file(username = username, api_key = api_key)

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter(x = Pull.hashrate['x'], y = Calc.price_MA, name = "BTC 17-period 3D MA", line = dict(color = 'yellow', dash = 'dash')), secondary_y = False)
fig.add_trace(go.Scatter(x = Pull.hashrate['x'], y = Calc.gp_ratio_MA, name = "GP Ratio", line_color = 'dimgray'), secondary_y = False)
fig.add_trace(go.Scatter(x = Pull.hashrate['x'], y = Pull.price['y'], name = "BTC Price", line_color = 'deepskyblue'), secondary_y = False)

fig.add_trace(go.Scatter(x = Pull.hashrate['x'], y = Calc.hashrate_revenue_ratio, name = "HRRV Ratio", line_color = 'green'), secondary_y = False)

fig.update_layout(title_text='<b>Bitcoin HRRV Ratio</b>',
                  yaxis_type = "log")

# Set x-axis title
fig.update_xaxes(title_text="Date")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Values</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>HRRV Ratio</b>", secondary_y=True)

hrrv = py.plot(fig, filename='HRRV_Ratio v3', auto_open = True)

fig.show()




