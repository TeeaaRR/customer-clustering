# Model clustering
import pickle
import numpy as np
import pandas as pd
k_means = pickle.load(open("./static/models/final_model.pickle","rb"))
famd = pickle.load(open("./static/models/famd.pickle","rb"))
normalization = pickle.load(open("./static/models/standard_scaler.pickle","rb"))

def customerClustering(education, income, occupation, settlement):
    # convert data to dataframe
    data = pd.DataFrame(data=[[education, income, occupation, settlement]], 
                        columns=["Education", "Income", "Occupation", "Settlement size"])

    # create dummy data to help FAMD reduction (bug in famd.transform)
    dummy = pd.DataFrame(data=[ ["Unknown / other", 140000, "Unemployed / unskilled", "Small city"],
                                ["Highschool", 140000, "Skilled / official", "Mid-sized city"], 
                                ["University", 140000, "Management / self-employed", "Big city"], 
                                ["Graduate school", 140000, "Skilled / official", "Big city"]], 
                                columns=["Education", "Income", "Occupation", "Settlement size"])
    
    data = pd.concat([data, dummy], ignore_index=True)

    # normalize the income
    data[["Income"]] = normalization.transform(data[["Income"]])
    
    # reduce the dimensionality of the data
    reduce_feature = famd.transform(data)

    # Get the prediction
    result = k_means.predict(reduce_feature)[0]
    
    print(result)
    return result


############################################################################

# app.py
from flask import Flask, request, render_template # Import flask libraries

# Initialize the flask class and specify the templates directory
app = Flask(__name__)

# Default route set as 'index'
@app.route('/')
def index():
    return render_template('index.html')

# route 'form' set as 'form.html'
@app.route('/form')
def form():
    return render_template('form.html')

# Route 'result' accepts POST request
@app.route('/result',methods=['POST'])
def clustering():
    try:
        # Get the input from the form
        user_input = request.form.to_dict()

        # Convert the input to a list
        user_input = list(user_input.values())

        # remove attribute name if any from the list
        name = ''
        if request.form['name'] in user_input:
            name = user_input[0]
            user_input = user_input[1:]

        # Convert the list to a list of integers
        user_input = list(map(int, user_input))

        # destructure the list
        gender = 'Male' if user_input[0] == 0 else 'Female'
        marital_status = 'Single' if user_input[1] == 0 else 'Non-Single'
        age = user_input[2]
        education = 'Unknown / other' if user_input[3] == 1 else 'Highschool' if user_input[3] == 1 else 'University' if user_input[3] == 2 else 'Graduate school'
        income = user_input[4]
        occupation = 'Unemployed / unskilled' if user_input[5] == 0 else 'Skilled / official' if user_input[5] == 1 else 'Management / self-employed'
        settlement_size = 'Small city' if user_input[6] == 0 else 'Mid-sized city' if user_input[6] == 1 else 'Big city'

        # Get the prediction from the model
        result = customerClustering(education, income, occupation, settlement_size)
        if(result == 0):
            result = 'Medium'
        elif(result == 1):
            result = 'Low'
        elif(result == 2):
            result = 'High'
        else:
            result = 'Unknown'
        return render_template('output.html',name=name, gender=gender, marital_status=marital_status, age=age, education=education, income=income, occupation=occupation, settlement_size=settlement_size, result=result)
    except Exception as e:
        return 'Error Occured : ' + str(e)

# Run the Flask server
if(__name__=='__main__'):
    app.run()