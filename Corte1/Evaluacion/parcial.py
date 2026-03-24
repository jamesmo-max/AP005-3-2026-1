
categorias = ("Alimentos", "Tecnologia", "Ropa")# tupla

productos = []

print("BIENVENIDO")

while True:
    print("\nMENU")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    
    if opcion == "1":
        codigo = input("Ingrese código: ")
        nombre = input("Ingrese nombre: ")

        precio = float(input("Ingrese precio: "))
        if precio < 0:
            print("Error: el precio no puede ser negativo")
            continue

        cantidad = int(input("Ingrese cantidad: "))
        categoria = input(f"Ingrese categoría {categorias}: ")

        producto = {"codigo": codigo, "nombre": nombre, "precio": precio, "cantidad": cantidad, "categoria": categoria}

        productos.append(producto)
        print("Producto agregado correctamente")

    
    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados")
        else:
            for p in productos:
                print(f"Código: {p['codigo']} | Nombre: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']} | Categoría: {p['categoria']}")

    
    elif opcion == "3":
        codigo_buscar = input("Ingrese el código a buscar: ")
        encontrado = False

        for p in productos:
            if p["codigo"] == codigo_buscar:
                print(f"Código: {p['codigo']} | Nombre: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']} | Categoría: {p['categoria']}")
                encontrado = True

        if not encontrado:
            print("Producto no encontrado")

    
    elif opcion == "4":
        codigo_eliminar = input("Ingrese el código a eliminar: ")

        for p in productos:
            if p["codigo"] == codigo_eliminar:
                productos.remove(p)
                print("Producto eliminado")
                break
        else:
            print("Producto no encontrado")

    
    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")