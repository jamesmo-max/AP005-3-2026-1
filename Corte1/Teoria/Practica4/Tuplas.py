# ---------------- LISTAS ----------------

colores = ["Rojo", "Azul", "Amarillo", "Naranja", "Violeta", "Verde"]

print("Lista original:", colores)
print("Tamaño:", len(colores))
print("Tercer elemento:", colores[2])

colores.append("Blanco")
colores.insert(3, "Negro")
colores += ["Marron", "Gris"]

print("\nLista actualizada:", colores)

colores.remove("Marron")

colores.sort()
print("Lista ordenada:", colores)


# ---------------- NUMEROS ----------------

numeros = [10,9,8,7,6,5,4,3,2,1]

numeros.sort()
print("\nNumeros de menor a mayor:", numeros)

numeros.sort(reverse=True)
print("Numeros de mayor a menor:", numeros)


# ---------------- TUPLAS ----------------

tupla_colores = tuple(colores)
print("\nTupla:", tupla_colores)

print("¿Está 'Rojo' en la tupla?", "Rojo" in tupla_colores)

tupla_unica = ("Blanco",)
print("Tupla con un elemento:", tupla_unica)

datos = ("Gaspar", 5, 8, 1999)
nombre, dia, mes, año = datos

print("\nNombre:", nombre)
print("Fecha:", dia, "/", mes, "/", año)

lista_datos = list(datos)
print("Tupla convertida en lista:", lista_datos)