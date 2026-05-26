
import streamlit as st
import pandas as pd
import pickle
import logging

logging.basicConfig(level=logging.INFO)

try:
    model = pickle.load(open('RF_model_.pkl', 'rb'))

    st.title("Housing Price Prediction")

    Area = st.number_input('Area (sqft)', min_value=100)
    Bedrooms = st.number_input('Number of Bedrooms', min_value=1)
    Bathrooms = st.number_input('Number of Bathrooms', min_value=1)
    Schools = st.number_input('Number of Schools Nearby', min_value=0)

    if st.button('Predict Price'):

        input_data = pd.DataFrame(
            [[Area, Bedrooms, Bathrooms, Schools]],
            columns=[
                'Area',
                'Bedrooms',
                'Bathrooms',
                'Schools'
            ]
        )

        prediction = model.predict(input_data)

        st.success(f"Predicted Price: ${prediction[0]:,.2f}")

        logging.info("Prediction successful")

except Exception as e:
    st.error(f"Error: {e}")
    logging.error(f"Application error: {e}")
