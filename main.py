from flask import Flask, request
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0',	debug=True,	port=8080)
