import joblib
import numpy as np
import streamlit as st

# Load the pre-trained model
model = joblib.load("rf_model.pkl")

# Set up the Streamlit app with a title and instructions
st.title("🏠 California House Price Predictor")
st.markdown("Enter the housing details below to predict the house price.")

# Create input fields for the user to enter housing details
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.slider("Housing Median Age", 1, 100, 41)
total_rooms = st.number_input("Total Rooms", value=1000.0)
total_bedrooms = st.number_input("Total Bedrooms", value=400.0)
population = st.number_input("Population", value=500.0)
households = st.number_input("Households", value=500.0)
median_income = st.number_input("Median Income", value=3.2)

# Create radio buttons for location category
st.markdown("### Location Category")
location = st.radio(
    "Proximity to Ocean", ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
)

# Map location categories to numerical features
# Each category corresponds to a one-hot encoded vector.
location_dict = {
    "<1H OCEAN": [1, 0, 0, 0, 0],
    "INLAND": [0, 1, 0, 0, 0],
    "ISLAND": [0, 0, 1, 0, 0],
    "NEAR BAY": [0, 0, 0, 1, 0],
    "NEAR OCEAN": [0, 0, 0, 0, 1],
}

# Get the location features based on user input
location_features = location_dict[location]

# If the user clicks the predict button, process the input and make a prediction
if st.button("Predict House Price"):
    log_total_rooms = np.log(total_rooms + 1)
    log_total_bedrooms = np.log(total_bedrooms + 1)
    log_population = np.log(population + 1)
    log_households = np.log(households + 1)

    bedroom_ratio = log_total_bedrooms / log_total_rooms
    rooms_per_household = log_total_rooms / log_households

    input_data = np.array(
        [
            longitude,
            latitude,
            housing_median_age,
            log_total_rooms,
            log_total_bedrooms,
            log_population,
            log_households,
            median_income,
            *location_features,
            bedroom_ratio,
            rooms_per_household,
        ]
    ).reshape(1, -1)

    prediction = model.predict(input_data)[0]
    st.success(f"🏡 Estimated House Price: **${prediction:,.2f}**")
