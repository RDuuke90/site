
from matplotlib import pyplot as plt


def generate_bar_line_chart():
    # Datos del gráfico
    años = [2021, 2025, 2026, 2028, 2030]
    capacidad = [17.8, 19.8, 20.3, 20.5, 50]  # Capacidad en GW
    etiquetas = [
        "Capacidad actual (2021)", 
        "Proyecto 1: La Guajira (2025)", 
        "Proyecto 2: Caribe Norte (2026)", 
        "Proyecto 3: Nuevas Iniciativas (2028)", 
        "Proyección Región Caribe (2030)"
    ]

    # Crear el gráfico de barras
    fig, ax = plt.subplots(figsize=(14, 6))
    barras = ax.bar(años, capacidad, color=['#74c476', '#31a354', '#006d2c', '#238b45', '#00441b'])
    
    # Añadir la línea de tendencia (crecimiento proyectado)
    ax.plot(años, capacidad, color='yellow', marker='o', label='Crecimiento acumulado', linestyle='-', linewidth=2, markerfacecolor='orange')

    # Agregar títulos y etiquetas
    ax.set_title('Crecimiento Proyectado del Potencial Eólico en Colombia (2021-2030)', fontsize=14, fontweight='bold', color='white')
    
    ax.set_xlabel('Año', fontsize=12, color='white')
    ax.set_ylabel('Capacidad Eólica (GW)', fontsize=12, color='white')

    # Añadir leyenda con etiquetas correspondientes a cada barra
    ax.legend(barras, etiquetas, title="Proyectos y Proyecciones", loc="upper left", bbox_to_anchor=(1, 1), fontsize=10)

    # Mostrar el valor de cada punto en la línea
    for i, txt in enumerate(capacidad):
        ax.annotate(f'{txt}GW', (años[i], capacidad[i]), textcoords="offset points", xytext=(0,10), ha='center', color='orange')

    # Aumentar el margen superior para dar más espacio a la leyenda
    plt.subplots_adjust(right=0.75)

    # Añadir grid para mejorar la visibilidad
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Mostrar el gráfico en pantalla
    plt.savefig('static/images/line_bar_chart.png', transparent=True)
    plt.close()
