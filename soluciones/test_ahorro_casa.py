import pytest
from programas.ahorro_casa import calculate_months

# Fixture de parámetros por defecto (tasa r y porcentaje de pago inicial)
@pytest.fixture
def defaults():
    return {"r": 0.05, "portion_down_payment": 0.25}

# Casos básicos parametrizados:
# (yearly_salary, portion_saved, cost_of_dream_home, expected_months)
@pytest.mark.parametrize(
    "yearly_salary, portion_saved, cost_of_dream_home, expected_months",
    [
        (120,    1.0,   100,    3),    # Ahorro total cada mes, casa muy barata
        (120,    0.5,   120,    6),    # Ahorro 50%, coste moderado
        (1000,   0.25,  100,    1),    # Ahorro rápido al bajo coste
        (120000, 0.10,  250000, 183),  # Ejemplo realista (~15 años)
    ]
)
def test_calculate_months_parametrizado(
    yearly_salary, portion_saved, cost_of_dream_home, expected_months
):
    months = calculate_months(yearly_salary, portion_saved, cost_of_dream_home)
    assert months == expected_months

# Caso borde: coste de la casa = 0 → 0 meses
def test_coste_casa_cero_devuelve_cero():
    assert calculate_months(50_000, 0.1, 0) == 0

# Agrupamos con un marker los tests de excepciones
@pytest.mark.exceptions
@pytest.mark.parametrize(
    "yearly_salary, portion_saved, cost_of_dream_home",
    [
        (-10_000, 0.1,    100_000),  # salario negativo
        (50_000,  -0.2,   200_000),  # fracción negativa
        (50_000,   1.5,   200_000),  # fracción > 1
        (50_000,   0.1,  -100_000),  # coste negativo
    ]
)
def test_entradas_invalidas_raise_value_error(
    yearly_salary, portion_saved, cost_of_dream_home
):
    with pytest.raises(ValueError):
        calculate_months(yearly_salary, portion_saved, cost_of_dream_home)
