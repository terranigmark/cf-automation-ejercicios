# Validación de contraseñas fuertes

Queremos comprobar si una contraseña cumple con los criterios mínimos de seguridad para considerarse “fuerte”.

Tu objetivo es determinar si una contraseña ingresada por el usuario satisface todas las reglas definidas.

## Entradas del usuario

Pide al usuario que ingrese la contraseña y conviértela a `str`. Debe inicializarse al inicio de tu programa, **antes** de declarar otras variables:

1. **Contraseña** (`password`)

## Desarrollo del programa

Para validar la contraseña, sigue estos pasos:

1. Define los parámetros internos:
   - `min_length = 8`  
   - `require_special = True`  
   - `special_chars = "!@#$%^&*()-_+="`  

2. Verifica que `password` sea una cadena de texto. Si no lo es, lanza un `TypeError`.

3. Verifica que `min_length` sea mayor que cero. Si no, lanza un `ValueError`.

4. Comprueba que la longitud de `password` sea al menos `min_length`.

5. Comprueba que `password` contenga al menos:
   - Una letra **minúscula**  
   - Una letra **mayúscula**  
   - Un **dígito**  
   - Si `require_special` es `True`, al menos un carácter de `special_chars`

6. Implementa la función:
   ```python
   def is_strong_password(password: str, min_length: int = 8, require_special: bool = True) -> bool:
       # lógica de validación…
   ```
   Debe retornar `True` si todos los criterios se cumplen, o `False` en caso contrario.

7. En el bloque `main()`, pide la contraseña al usuario, llama a `is_strong_password` y muestra un mensaje apropiado.

## Salida

- Almacena el resultado de la validación en una variable `is_strong` y luego imprime:
  - **"¡Contraseña fuerte!"** si `is_strong` es `True`.  
  - **"Contraseña débil. Asegúrate de cumplir los requisitos."** si `is_strong` es `False`.  

## Notas

- Usa `TypeError` y `ValueError` para manejar entradas inválidas.  
- Separa la lógica de validación de la interacción con el usuario.  
- Asume que `input()` siempre devuelve un valor que puede tratarse como `str`.  
- No añadas lógica de lectura/escritura de archivos ni otras dependencias externas.  
