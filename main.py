import json

from scripts.area_chart import generate_area_chart
from scripts.bar_line_chart import generate_bar_line_chart
from scripts.calculator_chart import calulator_chart, generate_csv
from flask import Flask, render_template, request, send_file

from scripts.pie_chart import generate_pie_chart

app = Flask(__name__)

generate_pie_chart()
generate_bar_line_chart()
generate_area_chart()

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
    
    generate_csv(data)

    file_path = calulator_chart(data)

    return send_file(file_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
