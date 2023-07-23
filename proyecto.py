def mostrar_menu_inicial():
    print("------ Menú Inicial ------")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")

def mostrar_menu_secundario():
    print("------ Menú Secundario ------")
    print("1. Listado de usuarios (ascendente)")
    print("2. Listado de usuarios (descendente)")
    print("3. Cerrar sesión")
    print("4. Salir")

def iniciar_sesion(usuarios):
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
        return True, usuario
    else:
        print("Usuario o contraseña incorrectos.")
        return False, None

def registrar_usuario(usuarios):
    usuario = input("Ingrese un nombre de usuario: ")
    while usuario in usuarios:
        print("El usuario ya existe, por favor, elija otro.")
        usuario = input("Ingrese un nombre de usuario: ")

    contraseña = input("Ingrese una contraseña: ")
    usuarios[usuario] = contraseña
    print("Usuario registrado exitosamente.")

def listar_usuarios(usuarios, orden):
    print("------ Listado de usuarios ------")
    for usuario in sorted(usuarios.keys(), reverse=orden):
        print(f"Usuario: {usuario}, Contraseña: {usuarios[usuario]}")
    print("---------------------")

def main():
    usuarios = {
        "Sergio": "9",
        "Pilar": "8",
        "Angel": "7",
        "Jason": "6"
    }

    usuario_actual = None

    while True:
        if usuario_actual is None:
            mostrar_menu_inicial()
            opcion = input("Ingrese la opción deseada: ")

            if opcion == "1":
                if usuario_actual is None:
                    inicio_sesion, usuario_actual = iniciar_sesion(usuarios)
                else:
                    print("Ya ha iniciado sesión.")
            elif opcion == "2":
                registrar_usuario(usuarios)
            elif opcion == "3":
                print("Gracias por usar nuestra aplicación. ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")
        else:
            mostrar_menu_secundario()
            opcion = input("Ingrese la opción deseada: ")

            if opcion == "1":
                listar_usuarios(usuarios, False)  # Orden ascendente
            elif opcion == "2":
                listar_usuarios(usuarios, True)   # Orden descendente
            elif opcion == "3":
                usuario_actual = None
                print("Sesión cerrada.")
            elif opcion == "4":
                print("Gracias por usar nuestra aplicación. ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
