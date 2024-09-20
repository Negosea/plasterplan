# tests/test_visualization.py
# Testes para visualizações geralmente requerem frameworks diferentes, como image diffing.
# Neste caso, mantemos simples.
import unittest
from plasterplan.visualization import plot_quantities

class TestVisualization(unittest.TestCase):
    def test_plot_quantities(self):
        # Não há verificação simples de asserts para gráficos, mas podemos testar se roda sem erro.
        plot_quantities(10, 3, 5)

if __name__ == '__main__':
    unittest.main()
