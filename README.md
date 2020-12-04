# Do you know your stroke risk?

> 📌 DISCLAIMER: This project is used for demonstrative and illustrative purposes only and does not constitute an offering that has gone through regulatory review. It is not intended to serve as a medical application. There is no representation as to the accuracy of the output of this application and it is presented without warranty express or implied.


#### Team 5: Jeff Brown, Vincent Dinolfo, Emily Frels, Jeanine Vincent

## Project Description

#### Stroke Prediction and Analysis

Source of the data: https://www.sciencedirect.com/science/article/pii/S0933365719302295?via%3Dihub
Liu, Tianyu; Fan, Wenhui; Wu, Cheng (2019), “Data for: A hybrid machine learning approach to cerebral stroke prediction based on imbalanced medical-datasets”, Mendeley Data, V1, doi: 10.17632/x8ygrw87jw.1

The medical dataset contains 43,400 records of potential patients which includes 783 occurrences of stroke. 

Cerebral stroke has become a significant global public health issue. The ideal solution to this concern is to prevent in advance by controlling related metabolic factors. However, it is difficult for medical staff to decide whether special precautions are needed for a potential patient only based on the monitoring of physiological indicators unless they are obviously abnormal. This project builds a machine learning model to predict whether someone is at risk of having a stroke.

In this project we examined 43,400 rows of data pertaining to individuals, in order to build a machine learning model to predict whether someone is at risk of having a stroke. The data in each row includes numerical factors, such as age, average glucose levels and BMI (body mass index), and categorical factors, such as "has hypertension" (yes or no), "has heart disease" (yes or no), ever married, work type, and smoking status. We use this data to determine which factors contribute to having a stroke, and among those which hold the most weight.

### Data Dictionary
![](/static/images/data_dictionary.png)

### Machine Learning Technologies
#### Five models were compared to maximize stroke detection and minimize false alarm using Sklearn
1. Logistic Regression - Classify things as 1 vs. 0, yes vs. no, sick vs. well, cat vs. no cat, good credit risk vs. bad, etc.
2. Decision Trees & Random Forests - Classify things (as above).
3. K Nearest Neighbors (KNN) - Classify things (as above).
4. Support Vector Machines (SVM) - Classify things (as above).
5. Neural Networks / Deep Learning - A super powerful universal classifier. Quick recipe: properly scale, normalize, and encode your inputs/features (pd.get_dummies()) and your outputs/labels (to_categorical()); assign each column in your input array, X, to an input of your neural network; define a hidden layer with, say, three times as many nodes as you have input nodes; use an optional hidden layer(s) if you want; define one output node for each category you wish to detect; e.g., yes vs. no will have two output nodes; iris-setosa vs. iris-virginica vs. iris-versicolour will have three output nodes. Use a ReLU activation function on your hidden layers, and a softmax on your outputs. Tweak as desired or necessary.


After building and exporting our machine learning model, we build a Python Flask app to produce an HTML page embedded with JavaScript. The HTML page offers a form for users to enter their own information into, while the JavaScript reads the results from Flask and writes the results to the page accordingly.

### Project Website
Heroku App location: https://
