matriz_clientes = []
while True:
    nombres = input("Ingresa tus nombres")
    nombres = nombres.upper()
    apellidos = input("Ingresa tus apellidos")
    apellidos = apellidos.upper()
    rut = input("Ingresa tú rut sin puntos ni guión")
    rut = rut[:-1] + "-" + rut[-1]
    lista_clientes = [nombres, apellidos, rut]
    matriz_clientes.append(lista_clientes)

    option = input("¿Quieres agregar otro cliente? (y/n): ")
    option = option.upper()
    if option == "Y":
        continue
    elif option == "N":
        break
    else:
        print("No es una opción valida")
for cliente in matriz_clientes:
    print(f"Nombres cliente:{cliente[0]}")
    print(f"Apellidos cliente:{cliente[1]}")
    print(f"Rut cliente:{cliente[2]}")
    print("------------------------------------")