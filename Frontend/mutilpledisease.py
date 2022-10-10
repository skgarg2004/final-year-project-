import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
import pickle


# loading the models
# diabetes_model =pickle.load(open("#","rb"))
# heart_model =pickle.load(open("#","rb"))
# parkinson_model =pickle.load(open("#","rb"))

# sidebar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction', [
    'diabetes prediction',
    'heart disease prediction',
    'parkison prediction'
    ],
    icons=['activity', 'heart', 'person'],
    default_index=0)

# Diabetes prediction page
if selected == 'diabetes prediction':  # pagetitle
    st.title("Diabetes disease prediction")

    # columns
    # no inputs from the user

    col1, col2, col3 = st.columns(3)

    with col1:
     Pregnancies = st.text_input("Number of Pregnencies")
    with col2:
     Glucose = st.text_input("Glucose level")
    with col3:
     BloodPressure = st.text_input("Blood pressure  value")
    with col1:

     SkinThickness = st.text_input("Sckinthickness value")

    with col2:

     Insulin = st.text_input("Insulin value ")
    with col3:
     BMI = st.text_input("BMI value")
    with col1:
     DiabetesPedigreefunction = st.text_input("Diabetespedigreefunction value")
    with col2:

     Age = st.text_input("AGE")

    # code for prediction
    diabetes_dig = ''

    # button
    if st.button("Diabetes test result"):
      #  diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressur,SkinThickness,Insulin,BMI, DiabetesPedigreefunction,Age]])

        # after the prediction is done if the value in the list at index is 0 is 1 then the person is diabetic
        if diabetes_prediction[0] == 1:
              diabetes_dig = 'The person is Diabetic'
        else:
               diabetes_dig = 'THe person is not Diabetic'
    st.success(diabetes_dig)

if selected == 'heart disease prediction':
    st.title("Heart disease prediction")

    # age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	target
    # columns
    # no inputs from the user

    col1, col2, col3 = st.columns(3)

    with col1:
     age = st.text_input("AGE")
    with col2:
     sex = st.text_input("sex")
    with col3:
     cp = st.text_input("cp value")
    with col1:
     trestbps = st.text_input("trestbps value")

    with col2:

     chol = st.text_input("chol value ")
    with col3:
     fbs = st.text_input("fbs value")
    with col1:
     restecg = st.text_input("restecg value")
    with col2:
     thalach = st.text_input("thalach value")
    with col3:
     exang = st.text_input("exang value")
    with col1:
        oldpeak = st.text_input("oldpeak value")
    with col2:
        slope = st.text_input("slope value")
    with col3:
        ca = st.text_input("ca value")
    with col1:
        thal = st.text_input("Thal value")
    with col2:
        traget = st.text_input("Target value")

    # code for prediction
    heart_dig = ''

    # button
    if st.button("Heart test result"):
        # change the parameters according to the model
      #  heart_prediction = heart_model.predict([[Pregnancies,Glucose,BloodPressur,SkinThickness,Insulin,BMI, DiabetesPedigreefunction,Age]])

        if heart_prediction[0] == 1:
               heart_dig = 'The person have heart disease'
        else:
                heart_dig = 'THe person does not have heart disease'
    st.success(heart_dig)


if selected == 'parkison prediction':
    st.title("Parkison prediction")
  # parameters
#    name	MDVP:Fo(Hz)	MDVP:Fhi(Hz)	MDVP:Flo(Hz)	MDVP:Jitter(%)	MDVP:Jitter(Abs)	MDVP:RAP	MDVP:PPQ	Jitter:DDP	MDVP:Shimmer	MDVP:Shimmer(dB)	Shimmer:APQ3	Shimmer:APQ5	MDVP:APQ	Shimmer:DDA	NHR	HNR	status	RPDE	DFA	spread1	spread2	D2	PPE
   #change the variables according to the dataset used in the model
   
    col1, col2, col3 = st.columns(3)
    with col1:
     age = st.text_input("AGE")
    with col2 :
     sex =st.text_input("sex")
    with col3:
     cp=st.text_input("cp value")
    with col1:
     trestbps = st.text_input("trestbps value")

    with col2 :

     chol= st.text_input("chol value ")
    with col3:
     fbs = st.text_input("fbs value")
    with col1 :
     restecg = st.text_input("restecg value")
    with col2 :
     thalach = st.text_input("thalach value")
    with col3:
     exang=st.text_input("exang value")
    with col1 :
        oldpeak=st.text_input("oldpeak value")
    with col2 :
        slope=st.text_input("slope value")
    with col3:
        ca=st.text_input("ca value")
    with col1 : 
        thal = st.text_input("Thal value")
    with col2 :
        traget = st.text_input("Target value")
    


    # code for prediction 
    parkinson_dig =''

    # button 
    if st.button("Parkinson test result"):
     # change the parameters according to the model
      #  parkinson_prediction = parkinson_model.predict([[Pregnancies,Glucose,BloodPressur,SkinThickness,Insulin,BMI, DiabetesPedigreefunction,Age]])
        
        if parkinson_prediction[0]==1 :  
              parkinson_dig ='The person have Parkinson disease'
        else :
                parkinson_dig ='THe person does not have Parkinson disease'
    st.success( parkinson_dig)
