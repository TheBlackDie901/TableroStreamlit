# Tablero Interactivo con Streamlit para Ejercicios de Funciones en Python

Este proyecto es una aplicación web interactiva desarrollada con **Streamlit** que integra 10 ejercicios de funciones en Python. Los usuarios pueden ingresar datos a través de la interfaz gráfica, y la aplicación resuelve y muestra los resultados de cada ejercicio de forma dinámica.

## Estructura del Proyecto

### Funcionalidades

La aplicación permite seleccionar entre los siguientes ejercicios:

1. **Saludo simple**: Recibe un nombre y muestra un saludo personalizado.
2. **Suma de dos números**: Recibe dos números y devuelve su suma.
3. **Área de un triángulo**: Calcula el área de un triángulo dados la base y la altura.
4. **Calculadora de descuento**: Calcula el precio final de un producto aplicando descuento e impuestos.
5. **Suma de una lista de números**: Recibe una lista de números y devuelve su suma.
6. **Producto con valores predeterminados**: Calcula el total a pagar de un producto dado su nombre, cantidad, y precio por unidad (con valores predeterminados).
7. **Números pares e impares**: Separa una lista de números en pares e impares.
8. **Multiplicación con \*args**: Multiplica una cantidad arbitraria de números y devuelve el resultado.
9. **Información personal con \*\*kwargs**: Muestra información personal ingresada por el usuario.
10. **Calculadora flexible**: Realiza operaciones aritméticas (suma, resta, multiplicación, división) entre dos números.

### Uso del Código

El código está organizado de la siguiente manera:

- **streamlit.sidebar.selectbox()**: Utilizado para que el usuario seleccione el ejercicio que quiere realizar desde la barra lateral.
- **Widgets interactivos**: Se utilizan diferentes widgets de entrada para recibir los datos del usuario.
- **st.write()**: Utilizado para mostrar los resultados de los ejercicios en la interfaz.

### Estructura de Código

El proyecto está dividido en funciones, cada una corresponde con un ejercicio. Las funciones se almacenan en un diccionario (`opciones`), que actúa como un "switch" permitiendo seleccionar la función según la opción elegida por el usuario.


