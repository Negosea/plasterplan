# plasterplan/utils.py
def validate_positive_number(value):
    """
    Valida se um número é positivo.

    Args:
        value (float): O valor a ser validado.

    Raises:
        ValueError: Se o valor não for positivo.
    """
    if value <= 0:
        raise ValueError("O valor deve ser positivo.")
