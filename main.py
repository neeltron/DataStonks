from flask import Flask, request, render_template

import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import json

from sklearn.model_selection import train_test_split
import sklearn.metrics

data = pd.read_csv("stonks.csv")

app = Flask('app', template_folder = 'templates', static_folder = 'static')

@app.route('/')
def hello_world():
  return render_template('hello_world.html')

@app.route('/', methods = ["POST"])
def fetch():
  stock = request.form.get('stock')
  data_stonks = data[(data["Index"] == stock)]
  len_col = len(data_stonks)
  calamities = pd.read_csv("disasters.csv").tail(len_col)
  calamities["declaration_date"] = calamities["declaration_date"].str.slice(0, 10, 1)
  calamities['declaration_date'] = pd.to_datetime(calamities['declaration_date']).dt.strftime('%d-%m-%Y')
  # calamities_date = calamities[(calamities['declaration_date'])]
  print(calamities["declaration_date"])
  data_stonks = [calamities["declaration_date"], data_stonks["Date"]]
  data_stonks_y = data[(data["Index"] == stock)]
  data_stonks_y = data_stonks_y["Open"]
  fig = px.line(data, x= data_stonks, y=data_stonks_y)
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('index.html', graphJSON = graphJSON)

app.run(host='0.0.0.0',	debug=True,	port=8080)
