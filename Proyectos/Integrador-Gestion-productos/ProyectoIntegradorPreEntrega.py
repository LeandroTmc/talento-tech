import re


productos = []
patron_correo = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$' # Por si lo usás más adelante


while True:
    print("\n" + "="*30)
    print("   SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("="*30)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por nombre")
    print("4. Eliminar producto por número")
    print("5. Salir")
    print("="*30)
    
    opcion = input("Seleccione una opción (1-5): ").strip()
    

    if opcion == "1":
        print("\n--- Agregar Producto ---")
        

        while True:
            nombre = input("Nombre del producto: ").strip().title()
            if nombre: break
            print("El nombre no puede estar vacío.")
            

        while True:
            categoria = input("Categoría: ").strip().title()
            if categoria: break
            print("La categoría no puede estar vacía.")
            

        while True:
            try:
                precio = float(input("Precio: $"))
                if precio >= 0: break
                print("El precio no puede ser negativo.")
            except ValueError:
                print("Error: Ingrese un número válido para el precio.")
        

        nuevo_producto = [nombre, categoria, precio]
        productos.append(nuevo_producto)
        print(f"¡{nombre} agregado con éxito!")
        

    elif opcion == "2":
        print("\n--- Lista de Productos ---")
        if not productos:
            print("No hay productos registrados en el sistema.")
        else:
            for i, p in enumerate(productos, start=1):
                print(f"{i}. Nombre: {p[0]} | Categoría: {p[1]} | Precio: ${p[2]:.2f}")
                

    elif opcion == "3":
        print("\n--- Buscar Producto ---")
        if not productos:
            print("La base de datos está vacía.")
        else:
            busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()
            encontrado = False
            
            for p in productos:
                if busqueda in p[0].lower():
                    print(f"-> Encontrado: {p[0]} (Categoría: {p[1]}) - ${p[2]:.2f}")
                    encontrado = True
            
            if not encontrado:
                print(f"No se encontraron productos que coincidan con '{busqueda}'.")
                

    elif opcion == "4":
        print("\n--- Eliminar Producto ---")
        if not productos:
            print("No hay productos para eliminar.")
        else:

            for i, p in enumerate(productos, start=1):
                print(f"{i}. {p[0]}")
            
            try:
                numero = int(input("\nIngrese el número del producto a eliminar: "))
                
                if 1 <= numero <= len(productos):
                    indice_a_borrar = numero - 1
                    producto_eliminado = productos.pop(indice_a_borrar)
                    print(f"¡Se eliminó '{producto_eliminado[0]}' correctamente!")
                else:
                    print("Número fuera de rango. Operación cancelada.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
                

    elif opcion == "5":
        print("\n¡Gracias por usar el sistema! Saliendo...")
        break
        
    else:
        print("Opción inválida. Por favor, elija un número del 1 al 5.")