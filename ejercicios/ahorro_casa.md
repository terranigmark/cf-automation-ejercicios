# Ahorro para el pago inicial de tu casa de ensueño

¡Acabas de graduarte de CF y tienes un trabajo! Te mudas a otra ciudad y decides que quieres empezar a ahorrar para comprar una casa. Las casas son bastante caras, así que empiezas a ahorrar para el pago inicial de la casa de tus sueños.

Tu objetivo es averiguar cuántos meses toma ahorrar lo suficiente para el pago inicial. El costo de tu pago inicial se calcula multiplicando el costo total de tu casa de ensueño por el porcentaje del pago inicial.

## Entradas del usuario

Pide al usuario que ingrese las siguientes variables y las convierta a `float`. Deben inicializarse en el siguiente orden al inicio de tu programa, **antes** de declarar otras variables:

1. **Salario anual inicial** (`yearly_salary`)  
2. **Fracción del salario a ahorrar** (`portion_saved`). Esta variable debe estar en forma decimal (por ejemplo, `0.1` para el 10%).  
3. **Costo de la casa de tus sueños** (`cost_of_dream_home`)  

## Desarrollo del programa

Necesitarás determinar cuántos meses tomará ahorrar suficiente dinero, usando la siguiente información:

1. `yearly_salary`, como se describió arriba.  
2. `portion_saved`, como se describió arriba.  
3. `cost_of_dream_home`, como se describió arriba.  
4. `portion_down_payment`, el porcentaje del costo total necesario para el pago inicial. Asume `portion_down_payment = 0.25` (25%).  
5. La cantidad que has ahorrado hasta ahora es `amount_saved`, que inicia en `$0`.  
6. Obtienes una tasa de retorno anual `r`. Al final de cada mes recibes fondos adicionales `amount_saved * (r/12)` para tus ahorros (el 12 es porque `r` es una tasa anual). Asume `r = 0.05` (5%).  
7. Al final de cada mes, tus ahorros aumentan en:  
   1. Una fracción de tu salario mensual (`monthly_salary * portion_saved`).  
   2. El retorno mensual de tu inversión (`amount_saved * (r/12)`).  
   > **Nota:** La inversión usada para calcular el retorno mensual es la cantidad que tenías ahorrada al inicio de cada mes.

## Salida

- Tu programa debe almacenar el número de meses requeridos para ahorrar el pago inicial usando una variable llamada `months` y luego imprimirlo.

## Notas

- Ten cuidado con los valores que representan montos anuales versus montos mensuales.  
- Si el número de meses que devuelve tu programa está desfasado por uno, vuelve a leer el texto destacado arriba.  
- Asume que los usuarios ingresan entradas válidas (por ejemplo, no cadenas de texto cuando se espera un `float`).
