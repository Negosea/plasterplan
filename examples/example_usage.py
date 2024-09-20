# examples/example_usage.py
from plasterplan.calculator import calculate_materials
from plasterplan.structure import calculate_profiles
from plasterplan.visualization import plot_quantities

def main():
    wall_area = 30.0  # Área da parede em m²
    wall_length = 10.0  # Comprimento da parede em metros

    # Calcular a quantidade de chapas e perfis
    sheets_needed = calculate_materials(wall_area)
    profiles_needed = calculate_profiles(wall_length)

    # Exibir o resultado
    print(f"Chapas necessárias: {sheets_needed}")
    print(f"Perfis necessários: {profiles_needed}")

    # Visualizar os dados
    plot_quantities(wall_area, sheets_needed, profiles_needed)

if __name__ == "__main__":
    main()
