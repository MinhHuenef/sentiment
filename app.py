from email import message
from tkinter import Button
import streamlit 
import pickle 

#Loading the tranied model
model = pickle.load(open('mh.pkl','rb'))

#Create title 
streamlit.title("Predicting if review is positive or negative")

message = streamlit.text_input("Enter a review")

submit = streamlit.button("Predict")

if submit:
    prediction = model.predict([message])

    #print(prediction)
    #streamlit.write(prediction)

    if prediction[0] == 'positive':
        streamlit.success('This review is good')
    else:
        streamlit.warning('This review is bad')



