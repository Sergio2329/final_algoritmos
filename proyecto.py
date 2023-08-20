def mostrar_menu_principal():
    print("------ AULAGEST ------")
    print("1. Secretario")
    print("2. Docente")
    print("3. Alumno")
    print("4. Salir")

def mostrar_menu_secundario(menu):
    print(f"------ {menu} ------")
    if menu == "Menú_Secretario":
        print("1. Crear usuarios para docentes")
        print("2. Crear usuarios para alumnos")
        print("3. Lista de usuarios")
        print("4. Cerrar Sesión")
    elif menu == "Menú_Docente":
        print("1. Ingresar notas")
        print("2. Mostrar lista de alumnos matriculados")
        print("3. Promedio de notas")
        print("4. Cerrar Sesión")
    elif menu == "Menú_Alumno":
        print("1. Reporte de Notas")
        print("2. Cuadro de Mérito")
        print("3. Cerrar Sesión")
    elif menu == "Menú_Intento":
        print("1. Intentar nuevamente")
        print("2. Volver al menú principal")

def mostrar_menu_lista_usuarios():
    print("------ Menú lista de usuarios ------")
    print("1. Lista de docentes")
    print("2. Lista de alumnos")
    print("3. Volver al menú anterior")

def mostrar_menu_orden():
    print("------ Orden de la lista ------")
    print("1. Orden ascendente")
    print("2. Orden descendente")
    print("3. Volver al menú anterior")

def inicio_sesion_secretario(dic_secretarios):
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    if usuario in dic_secretarios and dic_secretarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
        return usuario
    else:
        print("Usuario o contraseña incorrectos.")
        return None

def inicio_sesion_docente(dic_docentes):
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    if usuario in dic_docentes and dic_docentes[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
        return usuario
    else:
        print("Usuario o contraseña incorrectos.")
        return None

def inicio_sesion_alumno(dic_alumnos):
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    if usuario in dic_alumnos and dic_alumnos[usuario]["contraseña"] == contraseña:
        print("Inicio de sesión exitoso.")
        return usuario
    else:
        print("Usuario o contraseña incorrectos.")
        return None

def registrar_usuario(tipo_usuario, usuarios):
    usuario = input("Ingrese un nombre de usuario: ")
    while usuario in usuarios:
        print("El usuario ya existe, por favor, elija otro.")
        usuario = input("Ingrese un nombre de usuario: ")

    contraseña = input("Ingrese una contraseña: ")
    usuarios[usuario] = {"contraseña": contraseña, "notas": []}
    print(f"Usuario {tipo_usuario} registrado exitosamente.")

def menu_secretario(dic_secretarios, dic_docentes, dic_alumnos):
    while True:
        mostrar_menu_secundario("Menú_Secretario")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            registrar_usuario("docente", dic_docentes)
        elif opcion == "2":
            registrar_usuario("alumno", dic_alumnos)
        elif opcion == "3":
            while True:
                mostrar_menu_lista_usuarios()
                opcion_lista = input("Ingrese la opción deseada: ")

                if opcion_lista == "1":
                    while True:
                        mostrar_menu_orden()
                        opcion_orden = input("Ingrese la opción deseada: ")
                        if opcion_orden == "1":
                            print("Lista de usuarios docentes en orden ascendente:")
                            for usuario in sorted(dic_docentes.keys()):
                                print(usuario)
                        elif opcion_orden == "2":
                            print("Lista de usuarios docentes en orden descendente:")
                            for usuario in sorted(dic_docentes.keys(), reverse=True):
                                print(usuario)
                        elif opcion_orden == "3":
                            break
                        else:
                            print("Opción inválida. Por favor, ingrese una opción válida.")
                elif opcion_lista == "2":
                    while True:
                        mostrar_menu_orden()
                        opcion_orden = input("Ingrese la opción deseada: ")
                        if opcion_orden == "1":
                            print("Lista de usuarios alumnos en orden ascendente:")
                            for usuario in sorted(dic_alumnos.keys()):
                                print(usuario)
                        elif opcion_orden == "2":
                            print("Lista de usuarios alumnos en orden descendente:")
                            for usuario in sorted(dic_alumnos.keys(), reverse=True):
                                print(usuario)
                        elif opcion_orden == "3":
                            break
                        else:
                            print("Opción inválida. Por favor, ingrese una opción válida.")
                elif opcion_lista == "3":
                    break
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")
        elif opcion == "4":
            print("Volviendo al menú principal.")
            return
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            
def registrar_alumno(dic_alumnos):
    alumno_nombre = input("Ingrese el nombre del alumno: ").strip()
    if alumno_nombre in dic_alumnos:
        print("El alumno ya existe.")
    else:
        contraseña = input("Ingrese una contraseña para el alumno: ")
        dic_alumnos[alumno_nombre] = {"contraseña": contraseña, "notas": []}
        print("Alumno registrado exitosamente.")
            
def mostrar_alumnos(dic_alumnos):
    print("Alumnos matriculados:")
    for alumno in dic_alumnos:
        print(alumno)

def calcular_promedio_y_aprobacion(dic_alumnos):
    alumno = input("Ingrese el nombre de usuario del alumno: ").strip()

    if alumno in dic_alumnos:
        notas = dic_alumnos[alumno]["notas"]
        if notas:
            promedio = sum(notas) / len(notas)
            print(f"Promedio de notas para {alumno}: {promedio:.2f}")
            
            if promedio >= 10:
                print("Aprobó el curso.")
            else:
                print("Desaprobó el curso.")
        else:
            print("El alumno no tiene notas ingresadas.")
    else:
        print("El alumno no existe.")
        
def mostrar_alumnos_y_promedios(dic_alumnos):
    print("Alumno       |    Promedio")
    print("-" * 30)
    for alumno, datos in dic_alumnos.items():
        notas = datos["notas"]
        if len(notas) > 0:
            promedio = sum(notas) / len(notas)
        else:
            promedio = 0
        print(f"{alumno:<12} |    {promedio:.2f}")

def menu_docente(dic_docentes, dic_alumnos):
    while True:
        mostrar_menu_secundario("Menú_Docente")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            ingresar_notas(dic_alumnos)
        elif opcion == "2":
            mostrar_alumnos(dic_alumnos)
        elif opcion == "3":
            mostrar_alumnos_y_promedios(dic_alumnos)
        elif opcion == "4":
            print("Volviendo al menú principal.")
            return
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def ingresar_notas(dic_alumnos):
    alumno = input("Ingrese el nombre de usuario del alumno: ").strip()
    alumno_encontrado = None

    for alumno_registrado in dic_alumnos:
        if alumno_registrado.lower() == alumno.lower():
            alumno_encontrado = alumno_registrado
            break

    if alumno_encontrado is not None:
        notas = []
        for i in range(3):
            nota = float(input(f"Ingrese la nota {i + 1} para {alumno_encontrado}: "))
            notas.append(nota)
        dic_alumnos[alumno_encontrado]["notas"] = notas
        print(f"Notas ingresadas exitosamente para {alumno_encontrado}.")
    else:
        print("El alumno no existe.")

def mostrar_reporte_notas_y_promedio(alumno):
    print("Reporte de Notas:")
    notas = alumno["notas"]
    print(f"Práctica 1: {notas[0]}")
    print(f"Práctica 2: {notas[1]}")
    print(f"Examen Final: {notas[2]}")
    promedio = sum(notas) / len(notas)
    print(f"Promedio del Curso: {promedio:.2f}")
    if promedio >= 13:
        print("Curso Aprobado.")
    else:
        print("Curso Desaprobado.")

def mostrar_cuadro_merito(dic_alumnos):
    ordenados_por_promedio = sorted(dic_alumnos.items(), key=lambda x: calcular_promedio(x[1]["notas"]), reverse=True)
    
    print("Cuadro de Mérito:")
    print("Posición |   Alumno    |    Promedio")
    print("-" * 40)
    for posicion, (alumno, datos) in enumerate(ordenados_por_promedio, start=1):
        promedio = calcular_promedio(datos["notas"])
        print(f"{posicion:<9} | {alumno:<12} |    {promedio:.2f}")

    alumno_actual = obtener_usuario_actual(dic_alumnos)
    if alumno_actual:
        posicion_alumno = obtener_posicion_alumno(ordenados_por_promedio, alumno_actual)
        print(f"\nPosición de {alumno_actual} en el cuadro de mérito: {posicion_alumno}")
        tercio_superior = len(ordenados_por_promedio) // 3
        if posicion_alumno <= tercio_superior:
            print("El alumno se encuentra en el tercio superior del cuadro de mérito.")
            
def mostrar_cuadro_merito(dic_alumnos, alumno_actual):
    print("Cuadro de Mérito:")
    print("Alumno     |    Promedio")
    
    alumnos_ordenados = sorted(dic_alumnos.items(), key=lambda x: calcular_promedio(x[1]["notas"]), reverse=True)
    tercio_superior = len(alumnos_ordenados) // 3

    for i, (alumno, datos) in enumerate(alumnos_ordenados, start=1):
        promedio = calcular_promedio(datos["notas"])
        print(f"{alumno:<12} |    {promedio:.2f}")
        if i <= tercio_superior and alumno == alumno_actual:
            print("¡Este alumno está en el tercio superior!")

def calcular_promedio(notas):
    return sum(notas) / len(notas) if notas else 0

def menu_alumno(usuario_actual, dic_alumnos):
    alumno = dic_alumnos[usuario_actual]
    while True:
        mostrar_menu_secundario("Menú_Alumno")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            mostrar_reporte_notas_y_promedio(alumno)
        elif opcion == "2":
            mostrar_cuadro_merito(dic_alumnos, usuario_actual)
        elif opcion == "3":
            print("Cerrar sesión")
            return
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def menu_intentos(usuarios):
    intentos = 3
    while intentos > 0:
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")

        if usuario in usuarios and contraseña == usuarios[usuario]:
            print("Inicio de sesión exitoso.")
            return usuario
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Le quedan {intentos} intentos.")
                mostrar_menu_secundario("Menú_Intento")
                opcion_intento = input("Ingrese la opción deseada: ")
                if opcion_intento != "1":
                    break
            else:
                print("Ha excedido el número de intentos.")
                return None

dic_secretarios = {
    "Secretario1": "666",
    "Secretario2": "777",
    "Secretario3": "888"
}
dic_docentes = {
    "Docente1": "666",
    "Docente2": "777",
    "Docente3": "888"
}
dic_alumnos = {
    "Sergio": {"contraseña": "666", "notas": []},
    "Maggie": {"contraseña": "777", "notas": []},
    "Lidia": {"contraseña": "888", "notas": []}
}

# Bucle principal
while True:
    mostrar_menu_principal()
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        usuario_actual = inicio_sesion_secretario(dic_secretarios)
        if usuario_actual is not None:
            menu_secretario(dic_secretarios, dic_docentes, dic_alumnos)

    elif opcion == "2":
        usuario_actual = inicio_sesion_docente(dic_docentes)
        if usuario_actual is not None:
            menu_docente(dic_docentes, dic_alumnos)

    elif opcion == "3":
        usuario_actual = inicio_sesion_alumno(dic_alumnos)
        if usuario_actual is not None:
            menu_alumno(usuario_actual, dic_alumnos)

    elif opcion == "4":
        print("Gracias por usar nuestra aplicación. ¡Hasta pronto!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

