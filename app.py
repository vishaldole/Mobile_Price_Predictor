import pandas as pd
import numpy as np
import streamlit as st
import pickle

df = pickle.load(open('df_mobile1.pkl','rb'))
pipe = pickle.load(open('pipe_moble1.pkl','rb'))                             

st.title('Well come to Mobile Price Predictor')

brand_name = st.selectbox('Mobile Brand Name',df['brand_name'].unique())

has_5g = st.selectbox('Has 5 G',['Yes','No'])

has_nfc = st.selectbox('Has NFC',['Yes','No'])

has_ir_blaster = st.selectbox('Has IR Blaster',['Yes','No'])

processor_brand	= st.selectbox('Processor Brand',df['processor_brand'].unique())

num_cores = st.selectbox('No of Cores',[8,6,4])

processor_speed = st.number_input('Processsor Speed (In  GHz)')

battery_capacity = st.number_input('Batter Capacity')

fast_charging_available = st.selectbox('Fast Charging Available',['Yes','No'])

ram_capacity = st.selectbox('Ram Capacity',[12,  6,  4,  8,  3, 16,  2, 18,  1])


internal_memory = st.selectbox('Internal Memory',[ 256,  128,   64,   32,  512, 1024,   16,    8])

refresh_rate = st.selectbox('Refresh Rate',[120,  90,  60, 144, 165, 240])

os = st.selectbox('OS',df['os'].unique())

primary_camera_rear = st.number_input('Primary Rear Camera (In MP)')

primary_camera_front = st.number_input('Primary Front Camera (In MP)')

extended_memory_available = st.selectbox('Extended Memory Available',['Yes','No'])

if st.button("Prediction"):
       
       if fast_charging_available == 'Yes':
            fast_charging_available = 1
       else:
            fast_charging_available = 0   

       if  extended_memory_available == 'Yes':
            extended_memory_available = 1
       else:
            
            extended_memory_available = 0 

       if has_5g == 'yes':
            has_5g = 1
       else:
            has_5g = 0  

       if has_nfc == 'yes':
            has_nfc = 1
       else:
            has_nfc = 0   

       if has_ir_blaster == 'yes':
            has_ir_blaster = 1
       else:
            has_ir_blaster = 0                      
        

       quary = np.array([brand_name, has_5g, has_nfc, has_ir_blaster, processor_brand,num_cores, processor_speed, battery_capacity,fast_charging_available, ram_capacity, internal_memory,refresh_rate, os, primary_camera_rear, primary_camera_front,extended_memory_available])
       quary = quary.reshape(1,16)
       st.markdown("<h2 style='color: red;'>The predicted price of this configuration is</h2>", unsafe_allow_html=True)
       st.title(str(int(round(np.exp(pipe.predict(quary)[0])))))