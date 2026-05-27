"""House price prediction Streamlit application."""

import logging
import pickle

import pandas as pd
import streamlit as st

logging.basicConfig(level=logging.INFO)

try:
    with open('RF_model_.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    st.title("Housing Price Prediction")

    Area = st.number_input('Area (sqft)', min_value=100)
    Bedrooms = st.number_input('Number of Bedrooms', min_value=1)
    Bathrooms = st.number_input('Number of Bathrooms', min_value=1)
    Schools = st.number_input('Number of Schools Nearby', min_value=0)

    if st.button('Predict Price'):

        input_data = pd.DataFrame(
            [[Area, Bedrooms, Bathrooms, Schools]],
            columns=['Area', 'Bedrooms', 'Bathrooms', 'Schools']
        )

        prediction = model.predict(input_data)

        st.success(f"Predicted Price: ${prediction[0]:,.2f}")

        logging.info("Prediction successful")

except (OSError, ValueError, AttributeError) as e:
    st.error(f"Error: {e}")
    logging.error("Application error: %s", e)