import pandas as pd


#import dependencies
from flask import Flask
from flask import render_template 
from flask import jsonify
from flask import json


#############################################################
#          Function for Predictive Model                    #
#############################################################


#############################################################
#                       FLASK SETUP                        #
#############################################################

#create an app
app = Flask(__name__)

# Effectively disables page caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 

#Define what to do when a user hits the index route
@app.route("/")
def home():

    return render_template("index.html") 

# about route is used to show our information.
@app.route("/about")
def about():
    
    webpage = render_template("about.html")
    return webpage

@app.route("/charts")
def charts():

     webpage = render_template("charts.html")
     return webpage

@app.route("/data")
def data():

     webpage = render_template("data.html")
     return webpage

@app.route('/stroke_predictor', methods = ['POST'])
def stroke_predictor():

    
     prediction_labels = ['No Stroke', 'Stroke']

     stroke_features_init = [float(x) for x in request.form.values()]
     print(len(stroke_features_init))
     print(stroke_features)

     webpage = render_template("stroke_predictor.html")
     return webpage

#run the app
if __name__ == "__main__":
    app.run(debug=True)
