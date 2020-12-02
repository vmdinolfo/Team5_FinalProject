# Team5_FinalProject

# Do you know your stroke risk?

Source of the data: https://www.sciencedirect.com/science/article/pii/S0933365719302295?via%3Dihub
Liu, Tianyu; Fan, Wenhui; Wu, Cheng (2019), “Data for: A hybrid machine learning approach to cerebral stroke prediction based on imbalanced medical-datasets”, Mendeley Data, V1, doi: 10.17632/x8ygrw87jw.1

The medical dataset contains 43,400 records of potential patients which includes 783 occurrences of stroke. 

Cerebral stroke has become a significant global public health issue. The ideal solution to this concern is to prevent in advance by controlling related metabolic factors. However, it is difficult for medical staff to decide whether special precautions are needed for a potential patient only based on the monitoring of physiological indicators unless they are obviously abnormal. This project builds a machine learning model to predict whether someone is at risk of having a stroke.

In this project we examine 43,400 rows of data pertaining to individuals, in order to build a machine learning model to predict whether someone is at risk of having a stroke. The data in each row includes numerical factors, such as age, average glucose levels and BMI (body mass index), and categorical factors, such as "has hypertension" (yes or no), "has heart disease" (yes or no), ever married, work type, and smoking status. We use this data to determine which factors contribute to having a stroke, and among those which hold the most weight.

#### Data Dictionary
![](/static/images/data_dictionary.png)


After building and exporting our machine learning model, we build a Python Flask app to produce an HTML page embedded with JavaScript. The HTML page offers a form for users to enter their own information into, while the JavaScript reads the results from Flask and writes the results to the page accordingly.

