# PlasterPlan
Uso
Aqui está um exemplo de como usar o PlasterPlan:
## Descrição

from plasterplan import calculate_materials, calculate_profiles

# Exemplo de uso
wall_area = 30.0  # Área da parede em m²
wall_length = 10.0  # Comprimento da parede em metros

sheets_needed = calculate_materials(wall_area)
profiles_needed = calculate_profiles(wall_length)

print(f"Chapas necessárias: {sheets_needed}")
print(f"Perfis necessários: {profiles_needed}")



--------------------------------------------------------------
Interface Gráfica
Você também pode usar a interface gráfica:

python user_interface.py



O PlasterPlan é um pacote Python projetado para ajudar no cálculo de quantitativos de materiais usados em drywall. Ele calcula a quantidade de chapas de drywall necessárias, a quantidade de perfis, e oferece uma visualização dos resultados com gráficos.

## Instalação
```bash
pip install .
# plasterplan


##Uso
Aqui está um exemplo de como usar o PlasterPlan:
