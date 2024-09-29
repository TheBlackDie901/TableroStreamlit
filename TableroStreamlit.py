import streamlit as st

st.title('Ejercicios de Funciones en Python')

def saludar():
    nombre = st.text_input("Ingresa tu nombre")
    if nombre:
        st.write(f"Hola, {nombre}!")

def sumar():
    a = st.number_input("Ingresa el primer número", value=0)
    b = st.number_input("Ingresa el segundo número", value=0)
    st.write(f"Resultado: {a + b}")

def calcular_area_triangulo():
    base = st.number_input("Ingresa la base del triángulo", value=0.0)
    altura = st.number_input("Ingresa la altura del triángulo", value=0.0)
    st.write(f"Área: {(base * altura) / 2}")

def calcular_precio_final():
    precio = st.number_input("Precio original", value=0.0)
    descuento = st.number_input("Porcentaje de descuento", value=10.0)
    impuesto = st.number_input("Impuesto (%)", value=16.0)
    precio_descuento = precio - (precio * descuento / 100)
    precio_final = precio_descuento + (precio_descuento * impuesto / 100)
    st.write(f"Precio final: {precio_final}")

def sumar_lista():
    lista = st.text_input("Ingresa los números separados por comas")
    if lista:
        lista_numeros = [int(x) for x in lista.split(',')]
        st.write(f"Suma: {sum(lista_numeros)}")

def producto():
    nombre = st.text_input("Nombre del producto", value="Producto")
    cantidad = st.number_input("Cantidad", value=1)
    precio = st.number_input("Precio por unidad", value=10.0)
    st.write(f"Total a pagar: {cantidad * precio}")

def numeros_pares_e_impares():
    lista = st.text_input("Ingresa los números separados por comas")
    if lista:
        lista_numeros = [int(x) for x in lista.split(',')]
        pares = [num for num in lista_numeros if num % 2 == 0]
        impares = [num for num in lista_numeros if num % 2 != 0]
        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")

def multiplicar_todos():
    lista = st.text_input("Ingresa los números a multiplicar separados por comas")
    if lista:
        numeros = [int(x) for x in lista.split(',')]
        resultado = 1
        for num in numeros:
            resultado *= num
        st.write(f"Resultado: {resultado}")

def informacion_personal():
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", value=0)
    direccion = st.text_input("Dirección")
    if nombre and edad and direccion:
        st.write({"nombre": nombre, "edad": edad, "dirección": direccion})

def calculadora_flexible():
    a = st.number_input("Ingresa el primer número", value=0)
    b = st.number_input("Ingresa el segundo número", value=0)
    operacion = st.selectbox("Operación", ["suma", "resta", "multiplicación", "división"])
    if operacion == "suma":
        st.write(f"Resultado: {a + b}")
    elif operacion == "resta":
        st.write(f"Resultado: {a - b}")
    elif operacion == "multiplicación":
        st.write(f"Resultado: {a * b}")
    elif operacion == "división":
        if b != 0:
            st.write(f"Resultado: {a / b}")
        else:
            st.write("Error: División por cero")


opciones = {
    "1. Saludo simple": saludar,
    "2. Suma de dos números": sumar,
    "3. Área de un triángulo": calcular_area_triangulo,
    "4. Calculadora de descuento": calcular_precio_final,
    "5. Suma de una lista de números": sumar_lista,
    "6. Funciones con valores predeterminados": producto,
    "7. Números pares e impares": numeros_pares_e_impares,
    "8. Multiplicación con *args": multiplicar_todos,
    "9. Información personal con **kwargs": informacion_personal,
    "10. Calculadora flexible": calculadora_flexible
}

opcion = st.sidebar.selectbox(
    "Selecciona el ejercicio",
    list(opciones.keys())
)

opciones[opcion]()
