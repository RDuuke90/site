from matplotlib import pyplot as plt

def generate_pie_chart():
    # Datos para el gráfico de torta
    labels = ['Energía Hidroeléctrica', 'Otras Energías Renovables (Eólica, Solar, etc.)']
    sizes = [81, 19]  # Porcentajes
    colors = ['#4CAF50', '#FFEB3B']  # Verde para hidroeléctrica, amarillo para otras renovables
    explode = (0.05, 0)  # Separar ligeramente la sección de hidroeléctrica

    # Crear gráfico de torta
    plt.figure(figsize=(10, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)

    # Asegurarse de que el gráfico sea un círculo
    plt.axis('equal')

    # Título
    plt.title('Distribución de Energía Renovable en Colombia (2021)', fontsize=14, color='white')

    plt.savefig('static/images/pie_chart.png', transparent=True)
    plt.close()
