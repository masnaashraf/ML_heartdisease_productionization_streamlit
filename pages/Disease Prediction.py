import streamlit as st
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import os
import pickle

st.title(":red[Heart Disease Predictor]")

pipe=pickle.load(open('NB_model.pkl','rb'))



st.write(":blue[Provide values and predict your chance of heart disease]")

st.header("User input:")
cpl_val=0
sex_val=0
bs_val=3
ecg_val=3
angina_val=2
slope_val=5
t_val=1
def user_input():
    Age= st.number_input('Enter your Age',min_value=0)

    Sex = st.radio("Select your sex",('Male','Female'))
    global sex_val
    #1=Male , 0=Female
    if Sex == "Male":
        sex_val=1
        
    elif Sex == "Female":
        sex_val=0
    
    Chest_Pain_Level=st.radio("Select  Chest Pain Level ",('Stable Value','Unstable Value' ,'Microvascular Value','Variant'))
    #1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic
    global cpl_val
    if Chest_Pain_Level=="Stable Value":
        cpl_val=1
    elif Sex=="Unstable Value":
        cpl_val=2
    elif Sex=="Microvascular Value":
        cpl_val=3
    elif Sex=="Variant":
        cpl_val=4

    Resting_Blood_Pressure= st.number_input('Enter Resting Blood Pressure value',min_value=0)

    Cholestrol=st.number_input('Enter Cholestrol Level',min_value=0)

    
    Fasting_Blood_Sugar = st.radio("select person's fasting blood sugar ",('Greater than 120 mg/dl', ' Less than 120 mg/dl'))
    # 1 = true; 0 = false
    global bs_val
    if Fasting_Blood_Sugar=="Greater than 120 mg/dl":
        bs_val=1
    elif Fasting_Blood_Sugar=="Less than 120 mg/dl":
        bs_val=0

    Resting_ECG=st.radio("Select Resting electrocardiographic measurement", ('Normal', 'Having ST-T wave abnormality','Showing probable or definite left ventricular hypertrophy by Estes\' criteria'))
    #0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria
    global ecg_val
    if Resting_ECG=="Normal":
        ecg_val=0
    elif Resting_ECG=="Having ST-T wave abnormality":
        ecg_val=1
    elif Resting_ECG=="Showing probable or definite left ventricular hypertrophy by Estes\' criteria":
        ecg_val=2
    

    Max_Heart_Rate=Cholestrol=st.number_input('Enter ax_Heart_Rate value',min_value=0)

    Excercise_Induced_Angina= st.radio('Exercise induced angina',('Yes','No'))
    #Exercise induced angina (1 = yes; 0 = no)
    global angina_val
    if Excercise_Induced_Angina=="Yes":
        angina_val=1
    elif Excercise_Induced_Angina=="No":
        angina_val=0

    Depression=st.number_input('Enter drepression value in range(\o.o to 10.0\)',min_value=0.0,max_value=10.0)

    SlopeC= st.radio('Select the slope of the peak exercise ST segment',('Upsloping','Flat','Downsloping'))
    #Value 1: upsloping, Value 2: flat, Value 3: downsloping
    global slope_val
    if SlopeC=="Upsloping":
        slope_val=1
    elif SlopeC=="Flat":
        slope_val=2
    elif SlopeC=="Downsloping":
        slope_val=3

   
    Major_Vessels=st.radio("Select the number of major vessels \(0-3\)",('0','1','2','3'))
    vessel_val=int( Major_Vessels)
    
    global t_val
    Thalassemia_Level=st.radio("Select the level of thalassemia disoder",('Normal','Fixed defect','Reversable defect'))
    # (3 = normal; 6 = fixed defect; 7 = reversable defect)
    if Thalassemia_Level=="Normal":
        t_val=3
    elif Thalassemia_Level=="Reversable defect":
        t_val=7
    elif Thalassemia_Level=="Fixed defect":
        t_val=6
    



    data={"Age": Age,
          "Sex":sex_val,
          "Chest_Pain_Level":cpl_val,
          "Resting_Blood_Pressure":Resting_Blood_Pressure,
          "Cholestrol":Cholestrol,
          "Fasting_Blood_Sugar":bs_val,
          "Resting_ECG":ecg_val,
          "Max_Heart_Rate":Max_Heart_Rate,
          "Excercise_Induced_Angina":angina_val,
          "Depression":Depression,
          "SlopeC":slope_val,
          "Major_Vessels":vessel_val,
          "Thalassemia_Level":t_val
          }
    features=pd.DataFrame(data,index=[0])
    return features
df_userinput=user_input()



if st.button('Predict'):
    prediction=pipe.predict(df_userinput)[0]
    st.header(prediction)
    st.write("of disease is detected")