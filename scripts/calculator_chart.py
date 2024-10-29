import os
from matplotlib import pyplot as plt
import pandas as pd

def generate_csv(data):
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


def calulator_chart(data):
    categorias = ['Carro', 'Transporte Público', 'Electricidad', 'Gas', 'Carne', 'Agua']
    porcentajes = [
        data['carEmissions'],
        data['publicTransportEmissions'],
        data['electricityEmissions'],
        data['gasEmissions'],
        data['meatEmissions'],
        data['waterEmissions']
    ]

    colores = ['#84a07c', '#a3d9a5', '#f0c987', '#c07f00', '#8c8c00', '#4c784e']

    
    plt.figure(figsize=(8, 6))  # Ajusta el tamaño según sea necesario

    # Crear el gráfico de pastel sin autopct y sin anotaciones
    wedges, _ = plt.pie(porcentajes, colors=colores,
                        startangle=140, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

    plt.axis('equal')  # Asegurarse de que el gráfico sea redondo

    # Combinar categoías y porcentajes para la leyenda
    legend_labels = [f'{categoria}: {porcentaje:.0f}Kg CO₂' for categoria, porcentaje in zip(categorias, porcentajes)]

    plt.legend(wedges, legend_labels, title="Categorias", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)
    
    plt.tight_layout()
    file_path = os.path.join('static', 'images', 'calculator_chart.png')
    plt.savefig(file_path, transparent=True)
    

    plt.close()
    # code to generate the chart
    
    return file_path