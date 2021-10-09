from flask import Flask, request
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

# app.run(host='0.0.0.0',	debug=True,	port=8080)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn.metrics

data = pd.read_csv("stonks.csv")
print(data)
