# examples/main.py
from plasterplan.calculator import calculate_materials
from plasterplan.structure import calculate_profiles
from plasterplan.visualization import plot_quantities
from plasterplan.waste_calculator import calculate_waste
from plasterplan.report_generator import generate_report

def main():
    # Coletar entradas do usuário
    wall_area = float(input("Informe a área da parede em m²: "))
    wall_length = float(input("Informe o comprimento da parede em metros: "))
    sheet_area = float(input("Informe a área de uma chapa de drywall em m² (padrão: 3.0 m²): ") or 3.0)
    
    # Calcular a quantidade de chapas e perfis
    sheets_needed = calculate_materials(wall_area, sheet_area)
    profiles_needed = calculate_profiles(wall_length)

    # Exibir o resultado
    print(f"Chapas necessárias: {sheets_needed}")
    print(f"Perfis necessários: {profiles_needed}")

    # Calcular e exibir desperdício
    used_area = wall_area  # Supondo que toda a área é utilizada
    waste = calculate_waste(wall_area, used_area)
    print(f"Desperdício: {waste:.2f} m²")

    # Gerar e exibir relatório
    report = generate_report(wall_area, sheets_needed, profiles_needed)
    print(report)

    # Visualizar os dados
    plot_quantities(wall_area, sheets_needed, profiles_needed)

if __name__ == "__main__":
    main()
