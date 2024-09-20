# plasterplan/visualization.py
import matplotlib.pyplot as plt

def plot_quantities(wall_area, num_sheets, num_profiles):
    """
    Plota um gráfico de barras com os quantitativos de material.

    Args:
        wall_area (float): Área total da parede em metros quadrados.
        num_sheets (int): Número de chapas necessárias.
        num_profiles (int): Número de perfis necessários.
    """
    items = ['Wall Area (m²)', 'Sheets', 'Profiles']
    quantities = [wall_area, num_sheets, num_profiles]

    plt.bar(items, quantities)
    plt.title('Quantities of Drywall Materials')
    plt.ylabel('Amount')

    # Salvar o gráfico como um arquivo PNG
    plt.savefig('quantities.png')  # Salva o gráfico como quantities.png
    plt.close()  # Fecha a figura para liberar memória
