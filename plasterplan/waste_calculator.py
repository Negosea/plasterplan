# plasterplan/waste_calculator.py
def calculate_waste(total_area, used_area):
    """
    Calcula o desperdício de material.

    Args:
        total_area (float): Área total em metros quadrados.
        used_area (float): Área utilizada em metros quadrados.

    Returns:
        float: Área desperdiçada em metros quadrados.
    """
    if used_area > total_area:
        raise ValueError("A área utilizada não pode ser maior que a área total.")
    
    return total_area - used_area
