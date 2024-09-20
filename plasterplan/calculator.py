# plasterplan/calculator.py

def calculate_materials(wall_area, sheet_area=2.16):
    """
    Calcula a quantidade de chapas de drywall necessárias.

    Args:
        wall_area (float): Área total da parede em metros quadrados.
        sheet_area (float): Área de uma chapa de drywall em metros quadrados (padrão: 2.216 m²).

    Returns:
        int: Número de chapas necessárias.

    Raises:
        ValueError: Se a área da parede ou a área da chapa forem negativas ou zero.
    """
    if wall_area <= 0:
        raise ValueError("A área da parede deve ser positiva.")
    if sheet_area <= 0:
        raise ValueError("A área da chapa deve ser positiva.")

    # Cálculo do número de chapas
    num_sheets = wall_area / sheet_area
    return int(num_sheets) + (1 if num_sheets % 1 > 0 else 0)
