import pickle
from flask import Flask,render_template,request
import pandas as pd

app=Flask( __name__)
regressor=pickle.load(open('regressor.pkl','rb'))


@app.route( '/')
def index():
    return  render_template('index.html')


@app.route('/predict',methods = ['GET', 'POST'])
def predict():
    prediction=regressor.predict([[pd.to_numeric(request.form.get('temperature'))]])
    output=round(prediction[0],2)
    return  render_template('index.html',prediction_text=f'Toatl revenue generated is Rs. {output}/-')

if __name__=='__main__':
    app.run(debug=True)
    