import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load Model and Scaler
try:
    model = joblib.load('model.pkl')
    scaler = joblib.load('scaler.pkl')
    features = joblib.load('features.pkl')
except Exception as e:
    st.error(f"Error loading model files: {e}. Please run train_model.py first.")
    st.stop()

st.title("Mobile Price Prediction App")
st.image("mobile_banner.png", use_column_width=True)
st.markdown("""
This app predicts the price of a mobile phone based on its specifications. 
**Model trained on Cellphone.csv dataset.**
""")

st.sidebar.header("Input Features")

def user_input_features():
    data = {}
    for feature in features:
        # Determine descriptive label and ranges based on typical values
        # Default ranges are broad; in a real app, these would be fine-tuned or derived from data
        if feature == 'Sale':
             val = st.sidebar.slider(f"{feature}", 0, 1000, 10)
        elif feature == 'weight':
             val = st.sidebar.slider(f"{feature} (g)", 50, 500, 150)
        elif feature == 'resoloution':
             val = st.sidebar.slider(f"{feature} (inch)", 2.0, 10.0, 5.0)
        elif feature == 'ppi':
             val = st.sidebar.slider(f"{feature}", 50, 800, 300)
        elif feature == 'cpu core':
             val = st.sidebar.slider(f"{feature}", 1, 16, 4)
        elif feature == 'cpu freq':
             val = st.sidebar.slider(f"{feature} (GHz)", 0.5, 4.0, 1.5)
        elif feature == 'internal mem':
             val = st.sidebar.slider(f"{feature} (GB)", 2, 512, 16)
        elif feature == 'ram':
             val = st.sidebar.slider(f"{feature} (GB)", 1, 16, 4)
        elif feature == 'RearCam':
             val = st.sidebar.slider(f"{feature} (MP)", 0, 108, 13)
        elif feature == 'Front_Cam':
             val = st.sidebar.slider(f"{feature} (MP)", 0, 64, 5)
        elif feature == 'battery':
             val = st.sidebar.slider(f"{feature} (mAh)", 1000, 7000, 3000)
        elif feature == 'thickness':
             val = st.sidebar.slider(f"{feature} (mm)", 4.0, 20.0, 8.0)
        else:
             val = st.sidebar.number_input(f"{feature}", value=0.0)
        
        data[feature] = val
    
    return pd.DataFrame([data])

input_df = user_input_features()

st.subheader("User Input parameters")
st.write(input_df)

if st.button("Predict Price"):
    # Scale Input
    input_scaled = scaler.transform(input_df)
    
    # Predict
    prediction = model.predict(input_scaled)
    
    st.subheader("Predicted Price")
    st.success(f"${prediction[0]:.2f}")

st.markdown("---")
st.write("Based on 'Cellphone.csv' analysis.")
