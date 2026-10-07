
import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="CKD Check", layout="centered")
st.title("CKD Kidney Check")
st.write("Enter patient data for free checkup")

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("columns.pkl", "rb") as f:
        model_columns = pickle.load(f)
except:
    st.error("model.pkl not found")
    st.stop()

age = st.number_input("Age", 5, 90, 48)
bp = st.number_input("Blood Pressure", 50, 180, 80)
sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025])
al = st.selectbox("Albumin", [0,1,2,3,4,5])
su = st.selectbox("Sugar", [0,1,2,3,4,5])
hemo = st.number_input("Hemoglobin", 3.0, 18.0, 12.5)

if st.button("Check Result"):
    input_data = {'age': age, 'bp': bp, 'sg': sg, 'al': al, 'su': su, 'hemo': hemo}
    df = pd.DataFrame([input_data])
    df = df.reindex(columns=model_columns, fill_value=0)
    result = model.predict(df)[0]
    if str(result).lower() in ['ckd', '1']:
        st.error("Warning: CKD Risk - Visit Doctor")
    else:
        st.success("Normal - No CKD")
