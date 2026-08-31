import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------
# Load trained model and scaler
# ---------------------------------------------------

model = joblib.load("final_model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------------------------------------------
# Page configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Water Leakage Detection",
    page_icon="💧",
    layout="centered"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("💧 Water Leakage Detection System")

st.write(
    "Enter the pipe sensor information below to predict "
    "whether a water leakage is likely to occur."
)

# ---------------------------------------------------
# Input fields
# ---------------------------------------------------

pressure = st.number_input(
    "Pressure",
    min_value=0.0,
    value=60.0
)

flow_rate = st.number_input(
    "Flow Rate",
    min_value=0.0,
    value=80.0
)

temperature = st.number_input(
    "Temperature",
    min_value=0.0,
    value=100.0
)

vibration = st.number_input(
    "Vibration",
    min_value=0.0,
    value=3.0
)

rpm = st.number_input(
    "RPM",
    min_value=0.0,
    value=2000.0
)

operational_hours = st.number_input(
    "Operational Hours",
    min_value=0.0,
    value=5000.0
)

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

if st.button("Predict Leakage"):

    if flow_rate == 0:
        st.error("Flow Rate cannot be zero.")

    else:

        # Feature engineering
        pressure_flow_ratio = pressure / flow_rate

        # Mean vibration from the training dataset
        vibration_mean = 3.009713010891649

        vibration_deviation = abs(
            vibration - vibration_mean
        )

        # ---------------------------------------------------
        # Create all features expected by the scaler
        # ---------------------------------------------------

        input_data = pd.DataFrame({
            "Pressure": [pressure],
            "Flow_Rate": [flow_rate],
            "Temperature": [temperature],
            "Vibration": [vibration],
            "RPM": [rpm],
            "Operational_Hours": [operational_hours],
            "Pressure_Flow_Ratio": [pressure_flow_ratio],
            "Vibration_Deviation": [vibration_deviation]
        })

        # Scale using the saved scaler
        scaled_data = scaler.transform(input_data)

        scaled_data = pd.DataFrame(
            scaled_data,
            columns=input_data.columns
        )

        # Select the three features used by final_model
        model_input = scaled_data[
            [
                "Pressure_Flow_Ratio",
                "Flow_Rate",
                "Pressure"
            ]
        ]

        # Make prediction
        prediction = model.predict(model_input)[0]

        # Probability of leakage
        probability = model.predict_proba(model_input)[0][1]

        # ---------------------------------------------------
                # Display result

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error("🚨 Water Leakage Detected!")
        else:
            st.success("✅ No Water Leakage Detected.")

        st.write(
            f"Leakage Probability: {probability:.2%}"
        )

        st.write(
            f"No Leakage Probability: {(1 - probability):.2%}"
        )