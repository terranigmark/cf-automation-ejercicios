# test_password_validator.py

import pytest
from programas.validador_contrasenas import is_strong_password

# 1) Casos básicos parametrizados con valores por defecto
@pytest.mark.parametrize("password, expected", [
    ("Abcdef1!",  True),   # cumple todo
    ("Abc1!xyz",  True),
    ("abcdef1!", False),   # falta mayúscula
    ("ABCDEF1!", False),   # falta minúscula
    ("Abcdefgh!", False),  # falta dígito
    ("Abcdef12", False),   # falta especial
    ("Ab1!",     False),   # demasiado corta
])
def test_strength_default(password, expected):
    assert is_strong_password(password) == expected

# 2) Prueba del parámetro require_special=False
def test_allow_no_special_char():
    # sin exigir carácter especial, esta pasa
    assert is_strong_password("Abcdef12", require_special=False) is True

# 3) Prueba de override de min_length
def test_override_min_length():
    # con min_length=4, "Ab1!" tiene 4 chars y cumple
    assert is_strong_password("Ab1!", min_length=4) is True

# 4) Entradas inválidas que deben lanzar TypeError o ValueError
@pytest.mark.exceptions
@pytest.mark.parametrize("bad_pwd", [12345, None, 5.6])
def test_non_string_password_raises(bad_pwd):
    with pytest.raises(TypeError):
        is_strong_password(bad_pwd)

@pytest.mark.exceptions
def test_invalid_min_length_raises():
    with pytest.raises(ValueError):
        is_strong_password("Abcdef1!", min_length=0)
