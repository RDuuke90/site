from matplotlib import pyplot as plt

def generate_area_chart():
    años = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]  # Años de muestra
    hidroelectrica = [85, 84, 83, 82, 82, 81, 81, 81]  # Decreciente
    solar_eolica = [0, 1, 3, 5, 10, 14, 17, 19]  # Creciente

    # Crear la gráfica de área
    plt.figure(figsize=(10, 6))

    # Colores asociados a energías renovables
    plt.fill_between(años, hidroelectrica, label='Hidroeléctrica', color='#4CAF50', alpha=0.7)
    plt.fill_between(años, solar_eolica, label='Solar y Eólica', color='#FFEB3B', alpha=0.7)

    # Títulos y etiquetas
    plt.title('Participación de Energías Renovables en la Matriz Energética (2010-2024)', fontsize=14, fontweight='bold', color='white')
    plt.xlabel('Año', fontsize=12, color='white')
    plt.ylabel('Porcentaje de Participación', fontsize=12, color='white')
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')
    plt.legend(loc='upper right')

    # Añadir cuadrícula para mejor visualización
    plt.grid(True, linestyle='--', alpha=0.5)

    # Guardar el gráfico como imagen
    plt.savefig('static/images/area_chart.png', transparent=True)

    plt.close()   
