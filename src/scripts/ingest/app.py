import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

model = pickle.load(open('outputs/models/model.pkl', 'rb'))
app = Flask(__name__, template_folder='template') #Initialize the flask App

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    result = model.predict(final_features)
    
    if int(result)== 1:
        prediction ='Patient died during the follow up period'
    else: 
        prediction ='Patient did not die during the follow up period.'

    return render_template('index.html', prediction_text=prediction)

if __name__ == '__main__':
    app.run(debug=True)