import json

import pandas as pd
from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def home():
    with open('information/energias.json', 'r') as file:
        energias = json.load(file)
        file.close()

    with open('information/alternativas.json', 'r') as file:
        alternativas = json.load(file)
        file.close()

    return render_template('index.html',
                           energias=energias['energias'],
                           alternativas=alternativas['alternativas']
                           )


@app.route('/save_carbon_footprint', methods=['POST'])
def save_carbon_footprint():
    data = request.get_json()
    # Process the data as needed, e.g., save to a database or file
    df = pd.DataFrame({
        "Item": ["Car", "Public Transport", "Electricity", "Gas", "Meat", "Water", "Total"],
        "Emissions (kg CO2/year)": [
            data['carEmissions'],
            data['publicTransportEmissions'],
            data['electricityEmissions'],
            data['gasEmissions'],
            data['meatEmissions'],
            data['waterEmissions'],
            data['totalEmissions']
        ]
    })

    df.to_csv('files/carbon_footprint.csv', index=False)

    # Generate and save pie chart image
    labels = ['Car', 'Public Transport', 'Electricity', 'Gas', 'Meat', 'Water']
    sizes = [
        data['carEmissions'],
        data['publicTransportEmissions'],
        data['electricityEmissions'],
        data['gasEmissions'],
        data['meatEmissions'],
        data['waterEmissions']
    ]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Current Carbon Footprint Distribution')
    plt.gcf().set_facecolor('#f0f0f0')  # Set the background color
    plt.savefig('static/pie_chart.png')
    plt.close()

    return jsonify({'message': 'Data received successfully'}), 200


if __name__ == '__main__':
    app.run()
