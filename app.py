# Model clustering
import pickle
import numpy as np
k_means = pickle.load(open("./static/models/final_model.pickle","rb"))
pca = pickle.load(open("./static/models/pca.pickle","rb"))
normalization = pickle.load(open("./static/models/standard_scaler.pickle","rb"))

def customerClustering(data):
    # convert data to 2D array
    data = np.array(data).reshape(1,-1)
    # normalize the data
    normalize_data = normalization.transform(data)
    # reduce the dimensionality of the data
    reduce_feature = pca.transform(normalize_data)
    # Get the prediction
    result = k_means.predict(reduce_feature)
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
        education = 'High School' if user_input[3] == 0 else 'University' if user_input[3] == 1 else 'Graduate School'
        income = user_input[4]
        occupation = 'Unemployed' if user_input[5] == 0 else 'Skilled Employee' if user_input[5] == 1 else 'Manager'
        settlement_size = 'Small City' if user_input[6] == 0 else 'Mid City' if user_input[6] == 1 else 'Big City'

        # Get the prediction from the model
        result = customerClustering(user_input)
        if(result == 0):
            result = 'Low-Average'
        elif(result == 1):
            result = 'Lowest'
        elif(result == 2):
            result = 'High-Average'
        elif(result == 3):
            result = 'Highest'
        else:
            result = 'Unknown'
        return render_template('output.html',name=name, gender=gender, marital_status=marital_status, age=age, education=education, income=income, occupation=occupation, settlement_size=settlement_size, result=result)
    except Exception as e:
        return 'Error Occured : ' + str(e)

# Run the Flask server
if(__name__=='__main__'):
    app.run()