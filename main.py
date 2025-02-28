import streamlit as st
import requests

# Streamlit App Title
st.title("🚗 Car Price Prediction App")

st.write("Enter car details below to predict the price:")

# Manufacturer selection
manufacturers = ["HYUNDAI", "TOYOTA", "MERCEDES-BENZ", "FORD", "CHEVROLET", 
                 "BMW", "LEXUS", "HONDA", "NISSAN", "VOLKSWAGEN", "OTHER"]

manufacturer = st.selectbox("Select Manufacturer", manufacturers)

# Year and Mileage Input
year = st.number_input("Enter Car Year", min_value=2000, max_value=2025, value=2018)
mileage = st.number_input("Enter Car Mileage", min_value=0, value=50000)

# Button to predict price
if st.button("Predict Price"):
    # Prepare data for FastAPI request
    input_data = {
        "year": year,
        "mileage": mileage,
        **{f"manufacturer_{m}": int(m == manufacturer) for m in manufacturers}  # One-hot encoding
    }

    # Call FastAPI endpoint
    api_url = "http://127.0.0.1:8000/predict"  # Update this when deployed
    response = requests.post(api_url, json=input_data)
    
    if response.status_code == 200:
        predicted_price = response.json()["predicted_price"]
        st.success(f"💰 Estimated Car Price: **${predicted_price}**")
    else:
        st.error("Error: Could not get prediction. Make sure API is running.")
