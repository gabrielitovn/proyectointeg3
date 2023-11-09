import os
from pynput import keyboard

""""
Proyecto integrador parte 3
Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:

Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e 
imprimir el nuevo número hasta el número 50.

La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.

Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se 
debe importar la librería os

"""

import os
from pynput import keyboard

# Contador global
contador = 0

def clear_and_print(number):
    # Borra la terminal antes de imprimir el nuevo número
    os.system('cls' if os.name == 'nt' else 'clear')
    print(number)

def on_key_release(key):
    global contador

    if contador < 50:
        if key.char == "n":
            contador += 1
            clear_and_print(contador)
        else:
            print("No es 'n'")

    if contador >= 50:
        listener.stop()

# Configurar el listener del teclado
listener = keyboard.Listener(on_release=on_key_release)
listener.start()

# Esperar hasta que el contador llegue a 50
while contador < 50:
    pass

