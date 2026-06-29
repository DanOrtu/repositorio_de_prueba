def pedir_cadena(mensaje: str, minimo: int, mensaje_error: str, opciones = None) -> str:
    cadena = input(mensaje)
    while len(cadena) < minimo or (opciones != None and cadena not in opciones):
        cadena = input(mensaje_error)
    return cadena

def pedir_entero(mensaje: str, minimo: int, maximo: int, mensaje_error: str) -> int:
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
            numero = int(input(mensaje_error))
    return numero

def ingresar_datos(usuario: dict, tipos_contenido: list, estados_espectador: list, momentos_dia: list, idiomas: list, generos: list):
    '''La funcion ingresa los datos del usuario para que se desarrolle el programa.''' #en base a esta funcion el programa funciona. Es el case 1 
    print("\tRECOMENDADOR DE PELÍCULAS Y SERIES\n")
    print("Para conocerte mejor y conocer tus gustos, te vamos a hacer algunas preguntas.\n")
    print ("PERFIL DEL ESPECTADOR..............................\n")
    usuario["nombre"] = pedir_cadena("Ingrese nombre: ", 2, "Error... Reingrese su nombre: ")
    
    print("\nDatos númericos")
    usuario["edad"] = pedir_entero(" -> Tu edad: ", 0, 100, "X Ingresá entre 0 y 100.\n -> Reingrese su edad: ")
    usuario["tiempo_disponible"] = pedir_entero(" -> Tiempo disponible hoy (en minutos): ", 1, 1440, "X Ingresá entre 0 y 1440.\n -> Reingrese tiempo disponible (en minutos): ")
    usuario["nivel_exigencia"] = pedir_entero(" -> Nivel de exigencia al ver película/serie (1-10): ", 1, 10, "X Ingresá entre 1 y 10.\n -> Reingrese nivel de exigencia al ver pelicula/serie (1-10): ")
    usuario["estado_animo"] = pedir_entero(" -> Estado de ánimo actual (1-10): ", 1, 10, "X Ingresa entre 1 y 10.\n -> Reingrese estado de ánimo actual(1-10): ")
    usuario["contenido_visto_x_semana"] = pedir_entero(" -> Películas o capítulos que ves por semana (aprox.): ", 1, 50, "X Ingresá entre 1 y 50.\n -> Reingrese películas o capítulos que ve por semana: ")
    
    print("\nDatos categóricos")
    usuario["tipo_de_contenido"] = pedir_cadena(" -> ¿Película o serie?: ", 2, "X Ingresá película o serie\n -> Reingrese película o serie: ", tipos_contenido)
    usuario["momento_del_dia"] = pedir_cadena(" -> ¿En qué momento del día? (mañana/tarde/noche): ", 2, "X Ingresá mañana, tarde o noche\n -> Reingrese en qué momento del dia: ", momentos_dia)
    usuario["estado_del_espectador"] = pedir_cadena(" -> ¿Con quién vas a ver? (solo, familia, pareja): ", 2, "X Ingresá solo, familia o pareja\n -> Reingrese con quien va a ver: ", estados_espectador)
    usuario["genero_preferido"] = pedir_cadena(" -> ¿Qué genéro que desea ver? (accion/comedia/drama/terror/romance/thriller/ciencia_ficcion/animacion/documental): ", 2, "X Ingresá accion, comedia, drama, terror, romance, thriller, ciencia ficcion, animacion o documental\n -> Reingrese género qué desea ver: ", generos)
    usuario["idioma"] = pedir_cadena(" -> ¿Qué idioma preferís? (español/ingles/cualquiera): ", 2, "X Ingresá español, ingles, cualquiera\n -> Reingrese idioma: ", idiomas)


def definir_recomendacion(catalogo_activo):
    '''Esta funcion según el catálogo activo y la cantidad de puntos de la lista de contenido,
    suma el nombre del contenido y retorna la lista de recomendacion.'''  #esta funcion devuelve la lista recomendacion
    recomendacion = []
    for contenido in catalogo_activo:
        if contenido["puntos"] > 6:
            recomendacion.append(contenido["nombre"])
    return recomendacion

def mostrar_datos(catalogo_activo):
    '''Muestra la recomendacion.'''
    recomendacion = definir_recomendacion(catalogo_activo)
    for nombre in recomendacion:
        print(nombre)

#RECURSIVIDAD
def mostrar_barra(cantidad: int) -> str: 
    if cantidad <= 0:
        barra = ""
    elif cantidad == 1:
        barra = "*"
    else:
        barra = "*" + mostrar_barra(cantidad - 1)
    
    return barra