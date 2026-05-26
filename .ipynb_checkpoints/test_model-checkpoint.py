import pickle
import pandas as pd

model = pickle.load(open('RF_model_.pkl', 'rb'))

def test_prediction():

    input_data = pd.DataFrame(
        [[1200, 3, 2, 4]],
        columns=[
            'Area',
            'Bedrooms',
            'Bathrooms',
            'Schools'
        ]
    )

    prediction = model.predict(input_data)

    assert prediction[0] > 0