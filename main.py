from flask import Flask, request, render_template

import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import json

from sklearn.model_selection import train_test_split
import sklearn.metrics

data = pd.read_csv("stonks.csv")
# print(data)

data_stonks = data[(data["Index"] == "NYA")]
data_stonks = data_stonks["Date"]

data_stonks_y = data[(data["Index"] == "NYA")]
data_stonks_y = data_stonks_y["Open"]

print(data_stonks)

app = Flask('app', template_folder = 'templates', static_folder = 'static')

@app.route('/')
def hello_world():
  fig = px.line(data, x= data_stonks, y=data_stonks_y)
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('index.html', graphJSON = graphJSON)

app.run(host='0.0.0.0',	debug=True,	port=8080)
