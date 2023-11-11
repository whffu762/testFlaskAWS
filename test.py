from flask import Flask
import os
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app, resources={r'*':{ 'origins' : 'http://localhost:8080'}}) client와 통신 안해서 이거 필요없음


@app.route('/')
def home() :
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

