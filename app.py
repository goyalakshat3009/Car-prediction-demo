from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

companies = [
"Maruti 🚗",
"Hyundai 🚙",
"Honda 🚘",
"Toyota 🚗",
"Tata 🚙",
"Mahindra 🚜",
"Ford 🚗",
"Chevrolet 🚘",
"Audi 🏎️",
"BMW 🏁"
]

car_models = [
    "Maruti Suzuki Swift",
    "Hyundai i20",
    "Honda City",
    "Toyota Innova",
    "Tata Nexon",
    "Mahindra Scorpio"
]

fuel_types = ["Petrol","Diesel","CNG","LPG"]

@app.route('/')
def home():
    return render_template(
        'index.html',
        companies=companies,
        car_models=car_models,
        fuel_types=fuel_types
    )

@app.route('/predict', methods=['POST'])
def predict():

    data = pd.DataFrame({
        'name':[request.form['name']],
        'company':[request.form['company']],
        'year':[int(request.form['year'])],
        'kms_driven':[int(request.form['kms_driven'])],
        'fuel_type':[request.form['fuel_type']]
    })

    prediction = model.predict(data)[0]

    return render_template(
        'index.html',
        companies=companies,
        car_models=car_models,
        fuel_types=fuel_types,
        prediction_text=f"₹ {int(prediction):,}"
    )

if __name__ == "__main__":
    app.run(debug=True)