import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Farm Cost Tracking System", layout="wide")

st.title("🌾 Farm Cost Tracking & Profit Prediction System")

DATA_FILE = "farm_data.csv"

if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=[
        "crop_name", "land_area_acres", "seed_cost", "fertilizer_cost",
        "chemical_cost", "labor_cost", "machine_cost", "water_cost",
        "transport_cost", "other_cost", "expected_yield_kg",
        "actual_yield_kg", "selling_price_per_kg", "budget_cost"
    ])
    df.to_csv(DATA_FILE, index=False)

menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Add Farm Data", "View Data"]
)

if menu == "Home":
    st.header("Project Introduction")
    st.write("This system helps farmers track expenses and calculate farm profit.")

elif menu == "Add Farm Data":
    st.header("Add Farm Data")

    crop_name = st.text_input("Crop Name")
    land_area_acres = st.number_input("Land Area Acres", min_value=0.1)

    seed_cost = st.number_input("Seed Cost", min_value=0.0)
    fertilizer_cost = st.number_input("Fertilizer Cost", min_value=0.0)
    chemical_cost = st.number_input("Chemical Cost", min_value=0.0)
    labor_cost = st.number_input("Labor Cost", min_value=0.0)
    machine_cost = st.number_input("Machine Cost", min_value=0.0)
    water_cost = st.number_input("Water Cost", min_value=0.0)
    transport_cost = st.number_input("Transport Cost", min_value=0.0)
    other_cost = st.number_input("Other Cost", min_value=0.0)

    expected_yield_kg = st.number_input("Expected Yield Kg", min_value=0.0)
    actual_yield_kg = st.number_input("Actual Yield Kg", min_value=0.1)
    selling_price_per_kg = st.number_input("Selling Price Per Kg", min_value=0.0)
    budget_cost = st.number_input("Budget Cost", min_value=0.0)

    if st.button("Save Data"):
        new_data = pd.DataFrame([{
            "crop_name": crop_name,
            "land_area_acres": land_area_acres,
            "seed_cost": seed_cost,
            "fertilizer_cost": fertilizer_cost,
            "chemical_cost": chemical_cost,
            "labor_cost": labor_cost,
            "machine_cost": machine_cost,
            "water_cost": water_cost,
            "transport_cost": transport_cost,
            "other_cost": other_cost,
            "expected_yield_kg": expected_yield_kg,
            "actual_yield_kg": actual_yield_kg,
            "selling_price_per_kg": selling_price_per_kg,
            "budget_cost": budget_cost
        }])

        old_data = pd.read_csv(DATA_FILE)
        updated_data = pd.concat([old_data, new_data], ignore_index=True)
        updated_data.to_csv(DATA_FILE, index=False)

        st.success("Farm data saved successfully!")

elif menu == "View Data":
    st.header("Farm Data")
    df = pd.read_csv(DATA_FILE)

    if len(df) == 0:
        st.warning("No data available yet.")
    else:
        st.dataframe(df)