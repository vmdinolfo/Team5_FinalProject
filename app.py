import pandas as pd


#import dependencies
from flask import Flask
from flask import render_template 
from flask import jsonify
from flask import json
from flask import request
import joblib


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

#Define what to do when a user hits the index route - home page
@app.route("/")
def home():

    return render_template("index.html") 

# about route is used to show our information.
@app.route("/about")
def about():
    
    webpage = render_template("about.html")
    return webpage

# charts route shows results of Machine Learning models
@app.route("/charts")
def charts():

     webpage = render_template("charts.html")
     return webpage

# data route shows charting from raw data
@app.route("/data")
def data():

     webpage = render_template("data.html")
     return webpage

#stroke predictor route allows input of health to predict stroke risk
@app.route("/strokePredictor")
def strokePredictor():

     webpage = render_template("strokePredictor.html")
     return webpage

#strokePredictorData route is used to transfer data from form on strokePredictor page and transfer back result using Jinja
@app.route('/strokePredictorData', methods = ['POST'])
def strokePredictorData():
    
   
     dataOrder = [0,7,1,2,3,6,5,9,8,4] #contains order of list required for machine learning model (different than form order)
     stroke_features_init = [float(x) for x in request.form.values()] #reading values from form
     
     stroke_features_order = [stroke_features_init[dataOrder[i]] for i in range(0,len(stroke_features_init))] #rearranging order into new list
     print(len(stroke_features_init)) #printing number of data elements on screen
     print(stroke_features_init) #printing original list of elements
     print(stroke_features_order) #printing newly ordered list

     webpage = render_template("strokePredictor.html", prediction_text = "hello") #returning desired result to strokePredictor page
     return webpage

#run the app
if __name__ == "__main__":
    app.run(debug=True)
