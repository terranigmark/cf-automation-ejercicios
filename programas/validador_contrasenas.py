# password_validator.py


def is_strong_password(
        password: str,
        min_length: int = 8,
        require_special: bool = True
) -> bool:
    """
    Verifica si `password` cumple con los criterios de contraseña fuerte:
      - Es cadena de texto.
      - Tiene al menos `min_length` caracteres.
      - Contiene al menos una minúscula, una mayúscula y un dígito.
      - Si require_special=True, al menos un carácter de !@#$%^&*()-_+=.

    Parámetros:
        password (str): La contraseña a validar.
        min_length (int): Longitud mínima requerida (>0).
        require_special (bool): Si exige un carácter especial.

    Retorna:
        bool: True si es “fuerte”, False en caso contrario.

    Lanza:
        TypeError: si password no es str.
        ValueError: si min_length ≤ 0.
    """
    if not isinstance(password, str):
        raise TypeError("El password debe ser una cadena de texto.")
    if min_length <= 0:
        raise ValueError("La longitud mínima debe ser mayor que cero.")

    if len(password) < min_length:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False

    special_chars = set("!@#$%^&*()-_+=")
    if require_special and not any(c in special_chars for c in password):
        return False

    return True


def main():
    pwd = input("Ingresa tu contraseña: ")
    if is_strong_password(pwd):
        print("¡Contraseña fuerte!")
    else:
        print("Contraseña débil. Asegúrate de cumplir los requisitos.")


if __name__ == "__main__":
    main()
