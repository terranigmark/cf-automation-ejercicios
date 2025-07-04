def calculate_days_to_read(
    total_pages: int,
    pages_per_day: int,
    daily_increase_rate: float = 0.1
) -> int:
    """
    Calcula cuántos días se necesitan para leer un libro de `total_pages` páginas,
    comenzando con `pages_per_day` páginas el primer día y mejorando la velocidad
    un `daily_increase_rate` (en decimal) cada día.

    Parámetros:
        total_pages (int): Número total de páginas del libro (>0).
        pages_per_day (int): Páginas que lees el primer día (>0).
        daily_increase_rate (float): Tasa de mejora diaria (>=0).

    Retorna:
        int: Días necesarios para terminar el libro.

    Lanza:
        ValueError: si alguno de los parámetros no cumple sus restricciones.
    """
    # Validación de entradas
    if total_pages <= 0:
        raise ValueError("El total de páginas debe ser mayor que cero.")
    if pages_per_day <= 0:
        raise ValueError("Las páginas por día deben ser mayor que cero.")
    if daily_increase_rate < 0:
        raise ValueError("La tasa de mejora diaria no puede ser negativa.")

    days = 0
    pages_read = 0
    current_speed = pages_per_day

    while pages_read < total_pages:
        pages_read += current_speed
        current_speed += current_speed * daily_increase_rate
        days += 1

    return days


def main():
    total_pages = int(input("Número total de páginas del libro: "))
    pages_per_day = int(input("Páginas que lees el primer día: "))
    daily_increase_rate = float(input(
        "Tasa de mejora diaria (en decimal, p.ej. 0.1 para 10%): "
    ))

    days = calculate_days_to_read(total_pages, pages_per_day, daily_increase_rate)
    print(f"\nNecesitarás {days} días para leer el libro completo.")


if __name__ == "__main__":
    main()
