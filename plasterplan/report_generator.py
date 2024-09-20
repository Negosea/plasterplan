# plasterplan/report_generator.py
def generate_report(wall_area, sheets_needed, profiles_needed):
    """
    Gera um relatório simples sobre o uso de materiais.

    Args:
        wall_area (float): Área total da parede em metros quadrados.
        sheets_needed (int): Número de chapas necessárias.
        profiles_needed (int): Número de perfis necessários.

    Returns:
        str: Relatório formatado.
    """
    report = (
        f"Relatório de Uso de Materiais\n"
        f"Área da parede: {wall_area} m²\n"
        f"Chapas necessárias: {sheets_needed}\n"
        f"Perfis necessários: {profiles_needed}\n"
    )
    return report
