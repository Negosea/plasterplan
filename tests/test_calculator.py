# tests/test_calculator.py
import unittest
from plasterplan.calculator import calculate_materials

class TestCalculator(unittest.TestCase):
    
    def test_calculate_materials_standard(self):
        # Teste padrão: Área da parede é 10 m², uma chapa tem 3 m²
        self.assertEqual(calculate_materials(10, 3.0), 4)

    def test_calculate_materials_no_remainder(self):
        # Teste sem sobras: Área exata dividida pela chapa
        self.assertEqual(calculate_materials(9, 3.0), 3)

    def test_calculate_materials_with_remainder(self):
        # Teste com sobras: Área da parede não é múltiplo da chapa
        self.assertEqual(calculate_materials(10.5, 3.0), 4)
    
   # plasterplan/calculator.py

def calculate_materials(wall_area, sheet_area=3.0):
    """
    Calcula a quantidade de chapas de drywall necessárias.

    Args:
        wall_area (float): Área total da parede em metros quadrados.
        sheet_area (float): Área de uma chapa de drywall em metros quadrados (padrão: 3.0 m²).

    Returns:
        int: Número de chapas necessárias.

    Raises:
        ValueError: Se sheet_area for menor ou igual a 0.
    """
    if sheet_area <= 0:
        raise ValueError("O tamanho da chapa deve ser maior que zero.")
    
    num_sheets = wall_area / sheet_area
    return int(num_sheets) + (1 if num_sheets % 1 > 0 else 0)

if __name__ == '__main__':
    unittest.main()
