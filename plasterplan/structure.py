# plasterplan/structure.py
def calculate_profiles(wall_length, profile_spacing=0.6):
    """
    Calcula o número de perfis necessários para a estrutura.

    Args:
        wall_length (float): Comprimento total da parede em metros.
        profile_spacing (float): Distância entre os perfis em metros (padrão: 0.6 m).

    Returns:
        int: Número de perfis necessários.
    """
    num_profiles = wall_length / profile_spacing
    return int(num_profiles) + (1 if num_profiles % 1 > 0 else 0)
