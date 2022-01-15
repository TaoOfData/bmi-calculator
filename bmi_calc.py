import streamlit as st
import pandas as pd

st.title("Body Mass Index Calculator")
ht = st.number_input("Enter your height in centimeters:")
wt = st.number_input("Enter your weight in pounds:")

if ht > 0 and wt > 0:
    bmi = (wt / (ht/2.54)**2) * 703
    st.write(f"Your bmi is: {bmi:.1f}")

st.write("Below are the standard weight status categories.\nThese categories are the same for men and women of all "
         "body types and ages.")
weight_status = pd.DataFrame({
    'BMI': ["Below 18.5", "18.5 to 24.9", "25.0 to 29.9", "30.0 and Above"],
    'Weight Status': ["Underweight", "Health Weight", "Overweight", "Obesity"]
})
st.table(weight_status)