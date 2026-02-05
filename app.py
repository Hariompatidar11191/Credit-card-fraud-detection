import streamlit as st
import numpy as np
import joblib
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "fraud_model.pkl")
model = joblib.load(model_path)

st.set_page_config(page_title="Fraud Detection", layout="centered")

st.title("Credit Card Fraud Detection Dashboard")

st.write("Paste all 30 values at once separated by commas.")
st.write("Order: Time, V1–V28, Amount")

sample_normal = "10000,-1.359807,-0.072781,2.536347,1.378155,-0.338321,0.462388,0.239599,0.098698,0.363787,0.090794,-0.551600,-0.617801,-0.991390,-0.311169,1.468177,-0.470401,0.207971,0.025791,0.403993,0.251412,-0.018307,0.277838,-0.110474,0.066928,0.128539,-0.189115,0.133558,-0.021053,149.62"

sample_fraud = "406,-2.312227,1.951992,-1.609851,3.997906,-0.522188,-1.426545,-2.537387,1.391657,-2.770089,-2.772272,3.202033,-2.899907,-0.595222,-4.289254,0.389724,-1.140747,-2.830056,-0.016822,0.416956,0.126911,0.517232,-0.035049,-0.465211,0.320198,0.044519,0.177840,0.261145,-0.143276,0.00"

col1, col2 = st.columns(2)

with col1:
    if st.button("Use Sample Normal"):
        st.session_state["input"] = sample_normal

with col2:
    if st.button("Use Sample Fraud"):
        st.session_state["input"] = sample_fraud

default_text = st.session_state.get("input", "")

user_input = st.text_area(
    "Enter 30 values separated by commas:",
    value=default_text,
    height=100
)

if st.button("Predict"):
    try:
        values = [float(x.strip()) for x in user_input.split(",")]

        if len(values) != 30:
            st.error("You must enter exactly 30 values.")
        else:
            input_data = np.array(values).reshape(1, -1)
            prediction = model.predict(input_data)

            if prediction[0] == 1:
                st.error("Fraudulent Transaction Detected")
            else:
                st.success("Normal Transaction")

    except:
        st.error("Invalid input format.")
