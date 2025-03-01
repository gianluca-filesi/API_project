import streamlit as st
import requests

# Streamlit App Title
st.title("🚗 Car Price Prediction App")

st.write("Enter car details below to predict the price:")

# Manufacturer selection
manufacturers = ["HYUNDAI", "TOYOTA", "MERCEDES-BENZ", "FORD", "CHEVROLET", 
                 "BMW", "LEXUS", "HONDA", "NISSAN", "VOLKSWAGEN", "Other", "KIA", "OPEL", "SSANGYONG"]
manufacturers.sort()

manufacturer = st.selectbox("Select Manufacturer", manufacturers)
wheel = st.selectbox("Wheel Right-hand drive", ["Yes", "No"])
leather = st.selectbox("Leather interior", ["Yes", "No"])
doors = st.selectbox("Select Number of Doors", ["2/3", "4/5", "More than 5"])
drive = st.selectbox("Select Drive", ["4x4", "Front", "Rear"])
gear = st.selectbox("Select Gear Type", ['Automatic', 'Manual', 'Tiptronic', 'Variator'])
fuels = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']
fuels.sort()

fuel = st.selectbox("Select Fuel Type", fuels)
turbo = st.selectbox("Select Turbo", ["Yes", "No"])

colors = ["Beige", "Black","Brown","White", 
        "Silver", "Grey", "Blue", "Red", "Green", "Golden",
        "Orange", "Pink", "Purple", "Sky blue", "Yellow", "Carnelian red"]
colors.sort()

color = st.selectbox("Select Color", colors)

categories =  ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon', 'Universal', 'Coupe',
                'Minivan', 'Cabriolet', 'Limousine', 'Pickup']
categories.sort()
category = st.selectbox("Select Category", categories)

# Year and Mileage Input
levy = st.number_input("Enter Levy", min_value=0, value=0)
year = st.number_input("Enter Car Year", min_value=1930, max_value=2025, value=2018)
engine = st.number_input("Enter Engine Volume", min_value=1, max_value=10, value=5)
mileage = st.number_input("Enter Car Mileage", min_value=0, value=50000)
airbags = st.number_input("Enter Number of Airbags", min_value=0, value=10)
cylinders = st.number_input("Enter Number of Cylinders", min_value=1, value=10)

doors_mapping = {
    "2/3": "02-Mar",
    "4/5": "04-May",
    "More than 5": ">5"
}

# Button to predict price
if st.button("Predict Price"):
    # Prepare data for FastAPI request
    input_data = {
        "levy": levy, # Yes
        "year": year, # No
        "engine": engine, # No
        "cylinders": cylinders, # No
        "mileage": mileage, # No
        "airbags": airbags, # No
        "turbo": int(turbo == "Yes"), # No
        **{f"category_{c}": int(c == category) for c in categories}, # No
        **{f"fuel_{f}": int(f == fuel) for f in fuels}, # No
        **{f"gear_{g}": int(g == gear) for g in ['Automatic', 'Manual', 'Tiptronic', 'Variator']}, # No
        **{f"drive_{d}": int(d == drive) for d in ["4x4", "Front", "Rear"]}, # Yes
        **{f"doors_{doors_mapping[d]}": int(d == doors) for d in doors_mapping}, # No
        **{f"color_{c}": int(c == color) for c in colors}, # No
        "leather": int(leather == "Yes"), # No
        "wheel": int(wheel == "Yes"), # No
        **{f"manufacturer_{m}": int(m == manufacturer) for m in manufacturers}, # No
        }
    
    # Call FastAPI endpoint
    api_url = "http://127.0.0.1:8000/predict"  # Update this when deployed
    response = requests.post(api_url, json=input_data)
    
    if response.status_code == 200:
        predicted_price = response.json()["predicted_price"]
        st.success(f"💰 Estimated Car Price: **${predicted_price}**")
    else:
        st.error("Error: Could not get prediction. Make sure API is running.")
