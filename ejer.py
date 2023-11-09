"""
Paso 1: Primero, elige cuatro palabras que te gusten y busca sus significados en la página de la RAE (https://www.rae.es/), Crea un diccionario 
en Python donde cada palabra sea la llave y su respectiva definición sea su valor.
Paso 2: Crea un conjunto vacío
Paso 2: Lee por consola una palabra y guardarla en el conjunto 
Paso 3: Muestra la definición de la palabra introducida usando el diccionario
Paso 4: Imprime el conjunto.

"""

diccionario = {
    "perro": "El perro, llamado también perro doméstico o can, es un mamífero carnívoro de la familia de los cánidos.",
    "gato": "El gato doméstico, conocido comúnmente como gato, es un mamífero carnívoro de la familia Felidae.",
    "conejo": "El conejo común es un mamífero lagomorfo de la familia Leporidae.",
    "hamburguesa": "Una hamburguesa es un sándwich hecho a base de carne picada o de origen vegetal."
}

conjunto = set()

conjunto.add(input("Ingresar una palabra: "))

print("\nvalores del diccionatio: "+str(diccionario.values())+"\n")

print("Valores del conjunto "+str(conjunto))

