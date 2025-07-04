import pytest
from programas.tiempo_lectura import calculate_days_to_read

# Casos sencillos parametrizados: (total_pages, pages_per_day, rate, expected_days)
@pytest.mark.parametrize("total_pages, pages_per_day, rate, expected", [
    (100, 10, 0.0, 10),     # sin mejora diaria
    (100, 10, 0.1, 8),      # mejora del 10% cada día
    (50,  5,  0.2, 6),      # mejora del 20% diario
    (30, 30, 0.5, 1),       # un día basta si pages_per_day >= total_pages
])
def test_calculate_days_parametrizado(total_pages, pages_per_day, rate, expected):
    assert calculate_days_to_read(total_pages, pages_per_day, rate) == expected

def test_default_rate_is_used():
    # Cuando no pasamos rate, debe usar el valor por defecto 0.1
    days_default = calculate_days_to_read(100, 10)
    days_explicit = calculate_days_to_read(100, 10, 0.1)
    assert days_default == days_explicit

def test_invalid_inputs_raise_value_error():
    # total_pages inválido
    with pytest.raises(ValueError):
        calculate_days_to_read(0, 10, 0.1)
    # pages_per_day inválido
    with pytest.raises(ValueError):
        calculate_days_to_read(100, 0, 0.1)
    # rate negativo
    with pytest.raises(ValueError):
        calculate_days_to_read(100, 10, -0.05)
