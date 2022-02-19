clase = [] # lista que contendra los alumnos de la clase, representados en forma de diccionarios.


def mostrar_ayuda():
    # muestra la lista de comandos disponibles por pantalla.

    print(" [i] Comandos aceptados:")
    print("     help: muestra este mensaje de ayuda")
    print("     add: anade un nuevo alumno")
    print("     remove: elimina un alumno")
    print("     show_student: muestra informacion de un alumno")
    print("     show_class: muestra informacion de la clase")
    print("     mod: modifica los datos de un alumno")
    print("     avg: calcula la media de la clase y la muestra")
    print("     exit: sale del programa")


def add_alumno():
    # Anade un alumno a la lista "clase". Primero pide sus datos, luego crea el diccionario "nuevo_alumno", y por ultimo
    # pone ese diccionario recien creado en la lista.

    nombre_completo = input(" [i] Introduce el nombre completo: ")
    edad = int(input(" [i] Introduce la edad: ")) # convierto a int porque por defecto input guarda datos como strings
    media = int(input(" [i] Introduce la media: ")) # ^^^ aqui igual
    nuevo_alumno = {"nombre_completo": nombre_completo,
                    "edad": edad,
                    "media": media}
    try:
        clase.append(nuevo_alumno)
        print(" [i] ADD OK")
    except:
        print(" [!] ADD FAILED")


def eliminar_alumno(nombre_completo):
    # Elimina al alumno especificado de la lista "clase".

    alumno = buscar_alumno(nombre_completo)
    if alumno is not None:
        clase.remove(alumno)
        print(" [i] Alumno eliminado de la clase.")
    else:
        print(" [!] No se puede eliminar un alumno que no existe.")


def mostrar_info(nombre_completo):
    # Muestra la info del alumno especificado.

    alumno = buscar_alumno(nombre_completo)
    print(" [i] Mostrando info de: ", alumno["nombre_completo"])
    print("     > Nombre completo: ", alumno["nombre_completo"])
    print("     > Edad: ", alumno["edad"])
    print("     > Media: ", alumno["media"])


def buscar_alumno(nombre_a_buscar):
    # Accede a la lista "clase" y si encuentra al alumno especificado, lo retorna para su uso en otras funciones (por
    # ejemplo, la de mostrar_info para ver su info, eliminar_alumno para eliminarlo...

    for alumno in clase:
        if alumno["nombre_completo"] == nombre_a_buscar:
            return alumno

    print(" [!] Alumno no encontrado.")
    return None # OJO! si el alumno no se encuentra, retorna None (una especie de "null").


def calcular_media():
    # Calcula la media de la clase. Para ello, recorre la lista "clase", accediendo a las medias de cada alumno,
    # las suma y las divide por el numero total de alumnos (la longitud de la lista "clase").

    numerador = 0
    denominador = len(clase)
    for alumno in clase:
        numerador = numerador + alumno["media"]
        denominador = denominador + 1

    media = numerador / denominador
    return media


def mostrar_clase():
    # Recorre toda la lista "clase", mostrando los nombres de los alumnos que forman parte de la misma.

    print(" [i] Mostrando los alumnos de la clase...")
    for alumno in clase:
        print(" > ", alumno["nombre_completo"])


def modificar_alumno(nombre_a_modificar):
    # Busca un alumno en la clase y le da la opcion de modificar sus datos al usuario.
    # Cuando el alumno se encuentra, el usuario puede decidir que valores modificar.

    alumno = buscar_alumno(nombre_a_modificar)
    if alumno is not None:
        print(" [i] Sobreescribiendo datos de ", alumno["nombre_completo"])
        op = input("     Desea sobreescribir su nombre? (y/n): ")
        if op == "y":
            nombre = input("     Introduzca el nuevo nombre: ")
            alumno["nombre"] = nombre

        op = input("     Desea sobreescribir su edad? (y/n): ")
        if op == "y":
            edad = input("     Introduzca la nueva edad: ")
            alumno["edad"] = edad

        op = input("     Desea sobreescribir su media? (y/n): ")
        if op == "y":
            media = input("     Introduzca su nueva media: ")
            alumno["media"] = media

    else:
        print(" [!] No se puede eliminar un alumno que no existe.")


def programa():
    # Esta es la funcion principal del programa. Mediante un bucle infinito pediremos constantemente acciones a
    # realizar al usuario, hasta que el mismo ponga el comando "exit". El comando introducido por el usuario en cada
    # una de las iteraciones es guardado en la variable "op".

    print(" Simulador de clase en Python. Usa el comando help para ver las acciones disponibles.")

    # declaro la variable op y le doy un valor por defecto para usarla en el bucle
    # python es mierda y le tengo que dar un valor si o si al declararla, asi que ignora el "someshit"
    op = "someshit"

    while op != "exit":
        op = input(" >>> ")

        if op == "help":
            mostrar_ayuda()

        elif op == "add":
            add_alumno()

        elif op == "remove":
            nombre_completo = input(" [i] Introduzca el nombre completo del alumno: ")
            eliminar_alumno(nombre_completo)

        elif op == "show_student":
            nombre_completo = input(" [i] Introduzca el nombre completo del alumno: ")
            mostrar_info(nombre_completo)

        elif op == "show_class":
            mostrar_clase()

        elif op == "mod":
            nombre_completo = input(" [i] Introduzca el nombre completo del alumno: ")
            modificar_alumno(nombre_completo)

        elif op == "avg":
            media = calcular_media()
            print(" [i] La media de la clase es: ", media)

    print(" Bye!")


# desde aqui ejecutamos el programa, que esta en la funcion programa()
# desde la funcion programa, leemos lo que el usuario quiera hacer y llamamos al resto de funciones
programa()