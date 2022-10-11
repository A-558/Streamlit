# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:32:53 2022

@author: AKammari
"""

import numpy as np
#from flask import Flask, request,render_template
import pickle
import streamlit as st 


#app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#@app.route('/', methods = ['POST','GET'])
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=['POST'])
def predict_note_authentication(TV,Radio,NewsPaper):
    '''
    For rendering results on HTML GUI
    '''
   # int_features = [float(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)

    #output = prediction[0]
 
    
    prediction=model.predict([[TV,Radio,NewsPaper]])
    print(prediction)
    return prediction



def main():
    st.title("Sales Prediction by Ads ")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Sales Preduction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    TV = st.text_input("TV","")
    Radio = st.text_input("Radio","")
    NewsPaper = st.text_input("NewsPaper","")
   
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(TV,Radio,NewsPaper)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()