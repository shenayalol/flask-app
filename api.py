import csv

from flask import Flask, jsonify, request
 
app = Flask(__name__)


data = [
    {
        'name': 'shenaya',
        'grade': 8,
        'age': 13
    },
    {
        'height': 65,
        'state': 'massachusetts',
        'town': 'northreading'


    }
]
 
 
@app.route("/")
def api():

    return "hello my name is shenaya this is my first api link with data" 


@app.route("/shenayasData")
def function():
    return jsonify({
         'data': data,
         'status':'success'

    })

    
if __name__ == "__main__":
    app.run()





