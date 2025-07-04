def calculate_months(
    yearly_salary: float,
    portion_saved: float,
    cost_of_dream_home: float,
    r: float = 0.05,
    portion_down_payment: float = 0.25
) -> int:
    """
    Calcula el número de meses necesarios para ahorrar el pago inicial.

    Raises:
        ValueError: si yearly_salary < 0, portion_saved no está en [0,1] o cost_of_dream_home < 0.
    """
    # Validación de entradas
    if yearly_salary < 0:
        raise ValueError("El salario anual no puede ser negativo.")
    if not (0 <= portion_saved <= 1):
        raise ValueError("La fracción a ahorrar debe estar entre 0 y 1.")
    if cost_of_dream_home < 0:
        raise ValueError("El costo de la casa no puede ser negativo.")

    amount_saved = 0.0
    monthly_salary = yearly_salary / 12
    down_payment = cost_of_dream_home * portion_down_payment
    months = 0

    while amount_saved < down_payment:
        # retorno de la inversión
        amount_saved += amount_saved * (r / 12)
        # aporte de ahorro mensual
        amount_saved += monthly_salary * portion_saved
        months += 1

    return months


def main():
    # Entradas del usuario
    yearly_salary = float(input("Ingresa tu salario anual inicial: "))
    portion_saved = float(input(
        "Ingresa la fracción del salario a ahorrar (p.ej. 0.1 para 10%): "
    ))
    cost_of_dream_home = float(input("Ingresa el costo de la casa de tus sueños: "))

    # Cálculo y salida
    months = calculate_months(yearly_salary, portion_saved, cost_of_dream_home)
    down_payment = cost_of_dream_home * 0.25
    print(f"\nSe necesitan {months} meses para ahorrar el pago inicial de ${down_payment:,.2f}.")


if __name__ == "__main__":
    main()
