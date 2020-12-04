import pandas as pd


#import dependencies
from flask import Flask
from flask import render_template 
from flask import jsonify
from flask import json
from flask import request
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
#tensorflow.keras.__version__
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import classification_report


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.metrics import classification_report
from joblib import dump, load
from tensorflow.keras.utils import to_categorical


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


# mlm route shows info about Machine Learning Models
@app.route("/mlm")
def mlm():

     webpage = render_template("mlm.html")
     return webpage

# data route shows charting from raw data
@app.route("/resources")
def resources():

     webpage = render_template("resources.html")
     return webpage

#stroke predictor route allows input of health to predict stroke risk
@app.route("/strokePredictor")
def strokePredictor():
     
     webpage = render_template("strokePredictor.html", bunny_link = '/static/blank_default.png')
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

#KNN modeling
     features = [stroke_features_order]
     model_KNN = joblib.load('knn_model.sav')
     result = model_KNN.predict(features)

#Random Forest model
     model_RF = joblib.load('RF_model.sav')
     result_RF = model_RF.predict(features)

#Neural Network Model
     model_NN = load_model('NNM-SMOTE.h5')
     NeuralNet_scaler = load('NN_minmaxscaler.bin')
     features_scaled = NeuralNet_scaler.transform(features)
     result_NN = model_NN.predict_classes(features_scaled)

     print(f"KNN Model Result {result}")
     print(f"RF Model Result {result_RF}")
     print(f"NN Model Result {result_NN}")

     if result_RF == [0]:
          printed_result = 'No Risk of Stroke'
     elif result_RF == [1]:
          printed_result = 'Risk of Stroke'
     else:
          printed_result = 'ERROR: Fill out all forms for stroke prediction'

     
     if printed_result == 'No Risk of Stroke':
          gif = '/static/happy_bunny.gif'
     elif printed_result == 'Risk of Stroke':
          gif = '/static/sad_bunny.png'
     else:
          gif = '/static/blank_default.png'

     webpage = render_template("strokePredictor.html", prediction_text = printed_result, bunny_link = gif) #returning desired result to strokePredictor page
     return webpage

#run the app
if __name__ == "__main__":
    app.run(debug=True)
