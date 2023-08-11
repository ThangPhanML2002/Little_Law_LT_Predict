import pandas as pd
import numpy as np
from flask import Flask, request, render_template, jsonify
import joblib
from datetime import datetime

app = Flask(__name__)

df = pd.read_csv("Pos_Pakaging_Quan_Day1.csv")


def process(InvID):
    result = []
    data = df[df["InvID"] == InvID] 
    
    # Check if data for given InvID exists
    if not data.empty:
        result.append(data.iloc[0]["Quan_pag_max_day"])
        result.append(data.iloc[0]["Differ_mean"])     
        result.append(data.iloc[0]["Differ_median_day_pos_pag"])  
    else:
        # If data for the given InvID is not found, return None or an appropriate value.
        # You can modify this as per your requirement.
        result = None
    
    return result
model = joblib.load('model.pkl')
@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        InvID = str(request.form['InvID'])
        Quan_pos = float(request.form['Pos_quan'])
        month = float(request.form['month'])

        inp = process(InvID)
        if inp is not None:
            quan_pag_max_day, differ_mean, differ_median_day_pos_pag = inp
        else:
            quan_pag_max_day, differ_mean, differ_median_day_pos_pag = None, None, None
        input_data = pd.DataFrame({
            'Quan_pag_max_day': [quan_pag_max_day],
            'month' : [month],
            'Quan_pos' : [Quan_pos],
            'Differ_mean': [differ_mean],
            'Differ_median_day_pos_pag': [differ_median_day_pos_pag]
        })

        prediction = model.predict(input_data)
        output = "{:.0f}".format(float(prediction[0]))


        return render_template('index1.html', differ_mean=differ_mean, quan_pag_max_day=quan_pag_max_day,differ_median_day_pos_pag = differ_median_day_pos_pag,  month = month, prediction_text='Leadtime should be {} days'.format(output))
    except ValueError:
        return render_template('index1.html', differ_mean=None, quan_pag_max_day=None,differ_median_day_pos_pag = None,  month = None, prediction_text='Invalid Input! Please enter valid numeric values.')


if __name__ == "__main__":
    app.run(debug= True)