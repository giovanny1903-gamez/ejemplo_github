# Hacer un juego que peda al usuario un número, e programa debe generar un número aleatorio y compararlo
# con el que el usuario ingreso, si son iguales debe salir un mensaje que diga GANO el juego de lo contrario
# darle una indicación si el número que digito el usuario le falta o le sobra para ser igual con el numero
# del sistema.
import random
import streamlit as st
st.title("JUEGO 👍")
rojo = "\033[31m"
reset = "\033[0m"
Titulo = f"{rojo}BIENVENIDO AL JUEGO DE ADIVINANZA{reset}"
print(Titulo.center(60,"="))
numero_sistema = random.randint(1, 100)
print("INTENTA DESCUBRIR EL NUMERO QUE ELEGI ENTRE 1 A 100")
numero_usuario = int(input("INGRESA UN NUMERO: "))
if numero_usuario == numero_sistema:
    print("GANO EL JUEGO")
elif numero_usuario < numero_sistema:
    print(f"LE FALTA. Ingresaste {numero_usuario} y el numero del sistema era {numero_sistema}.")
else:
    print(f"LE SOBRA. Ingresaste {numero_usuario} y el numero del sistema era {numero_sistema}.")
