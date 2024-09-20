# plasterplan/custom_calculator.py
def calculate_custom_materials(wall_area, sheet_area=3.0, thickness=0.12):
    """
    Calcula a quantidade de chapas de drywall necessárias, considerando espessura.

    Args:
        wall_area (float): Área total da parede em metros quadrados.
        sheet_area (float): Área de uma chapa de drywall em metros quadrados (padrão: 3.0 m²).
        thickness (float): Espessura do drywall em metros (padrão: 0.12 m).

    Returns:
        int: Número de chapas necessárias.
    """
    adjusted_area = wall_area / thickness  # Ajusta a área com base na espessura
    num_sheets = adjusted_area / sheet_area
    return int(num_sheets) + (1 if num_sheets % 1 > 0 else 0)
