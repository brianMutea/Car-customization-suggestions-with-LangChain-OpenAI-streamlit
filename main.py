import langchain_helper as lch
import streamlit as st

st.title("Car Customization Suggestions")

car_model = st.sidebar.text_input(
    "What is your car model?", placeholder="Tesla Model S")

use_case = st.sidebar.text_input(
    "Customizing for?(press Enter to respond)", placeholder="off-roading", max_chars=15)

if use_case:
    st.header(
        f"Suggested {use_case} customizations for your {car_model} include:")
    response = lch.generate_suggestions(car_model, use_case)
    st.text(response['customizations'])
