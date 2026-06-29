def calcular_horas(tiempo_disponible: int) -> float:

    '''Esta funcion pasa el tiempo en minutos a horas y lo retorna.'''

    tiempo_disponible_horas = tiempo_disponible / 60
    return tiempo_disponible_horas

def calcular_promedio_tiempo_pelicula(tiempo_disponible_horas: float, contenido_visto_x_semana: int) -> float:

    '''Esta funcion retorna el tiempo de pelicula para recomendar según el tiempo disponible en horas 
    y la cantidad de contenido visto por semana.'''

    promedio_tiempo_pelicula = tiempo_disponible_horas / contenido_visto_x_semana
    return promedio_tiempo_pelicula

def calcular_indice_disponibilidad(tiempo_disponible_horas: float, estado_animo: int, nivel_exigencia: int) -> float:

    '''Esta funcion retorna el indicie de disponibilidad segun el tiempo en horas, el estado de animo y la exigencia.'''

    indice_disponibilidad = (tiempo_disponible_horas * estado_animo) / nivel_exigencia
    return indice_disponibilidad

def definir_indice_disponibilidad(indice_disponibilidad):

    '''Esta funcion retorna la disponibilidad según el indice de disponibilidad'''

    if indice_disponibilidad <= 1:
        disponibilidad = "muy_baja"
    elif indice_disponibilidad <= 3:
        disponibilidad = "baja"
    elif indice_disponibilidad <= 6:
        disponibilidad = "media"
    elif indice_disponibilidad <= 10:
        disponibilidad = "alta"
    else:
        disponibilidad = "muy_alta"
    return disponibilidad

def definir_perfil_consumidor(contenido_visto_x_semana):

    '''Esta funcion, según la cantidad de contenido visto por semana,
    define el perfil y lo retorna.'''
    
    if contenido_visto_x_semana <= 2:
        perfil = "casual"
    elif contenido_visto_x_semana <= 6:
        perfil = "habitual"
    else:
        perfil = "cinefilo"
    return perfil
