# Tiempo de lectura de un libro

Quieres saber **cuántos días** tardarás en leer un libro completo si comienzas leyendo un número fijo de páginas el primer día y mejoras tu ritmo cada día.

Tu objetivo es calcular el número mínimo de días necesarios para alcanzar o superar el total de páginas del libro.

## Entradas del usuario

Pide al usuario que ingrese las siguientes variables y las convierta a los tipos indicados. Deben inicializarse al inicio del programa, **antes** de declarar otras variables:

1. **Total de páginas del libro** (`total_pages`)  
   - Tipo: `int`  
   - Descripción: Número total de páginas que tiene el libro.  
2. **Páginas que lees el primer día** (`pages_per_day`)  
   - Tipo: `int`  
   - Descripción: Cantidad de páginas que puedes leer en el primer día.  
3. **Tasa de mejora diaria** (`daily_increase_rate`)  
   - Tipo: `float`  
   - Descripción: Fracción en decimal que indica cuánto mejora tu ritmo de lectura cada día (por ejemplo, `0.1` para 10%).  
   - Valor por defecto: `0.10` (10%)  

## Desarrollo del programa

Para calcular el número de días necesarios:

1. **Validar entradas**  
   - `total_pages` debe ser > 0.  
   - `pages_per_day` debe ser > 0.  
   - `daily_increase_rate` debe ser ≥ 0.  
   Si alguna validación falla, lanzar un `ValueError` con mensaje adecuado.

2. **Inicializar variables**  
   - `days = 0`  
   - `pages_read = 0`  
   - `current_speed = pages_per_day`  

3. **Bucle de lectura diaria**  
   Mientras `pages_read < total_pages`:
   1. Sumar al acumulado: `pages_read += current_speed`  
   2. Mejorar ritmo: `current_speed += current_speed * daily_increase_rate`  
   3. Incrementar contador de días: `days += 1`  

4. **Devolver resultado**  
   Al salir del bucle, `days` contiene el número de días necesarios.

## Salida

- El programa debe almacenar el resultado en una variable llamada `days` y luego imprimir un mensaje del tipo:
`Necesitarás X días para leer el libro completo.`


## Notas

- Ten en cuenta la diferencia entre los tipos de datos (`int` vs. `float`).  
- La mejora diaria se aplica sobre la velocidad del día **anterior**, no sobre la inicial constantemente.  
- Si al primer día ya cubres todas las páginas (`pages_per_day ≥ total_pages`), el resultado será `1`.  
- Asume que el usuario ingresa valores válidos (no se manejarán conversiones de string inválidas).  
