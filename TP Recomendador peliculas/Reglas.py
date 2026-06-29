from Calculos_generales import *

def definir_catalogo(tipo_de_contenido, peliculas, series):  #esta funcion retorna el catalogo_activo

    if tipo_de_contenido == "pelicula":
        catalogo_activo = peliculas
    elif tipo_de_contenido == "serie":
        catalogo_activo = series

    return catalogo_activo

def sumar_puntos_genero(catalogo_activo, genero, puntos):
    for contenido in catalogo_activo:
        if contenido["genero"] == genero:
            contenido["puntos"] += puntos

def sumar_puntos_valoracion(catalogo_activo, nivel_exigencia, puntos):
    for contenido in catalogo_activo:
        if contenido["valoracion"] >= nivel_exigencia:
            contenido["puntos"] += puntos

def sumar_puntos_año(catalogo_activo, año_minimo, puntos):
    for contenido in catalogo_activo:
        if contenido["año"] >= año_minimo:
            contenido["puntos"] += puntos


# R-Género 1: genero_preferido + momento_del_dia + estado_del_espectador
def regla_genero_momento_espectador(catalogo_activo, genero_preferido, momento_del_dia, estado_del_espectador):

    if genero_preferido == "terror" or genero_preferido == "thriller":
        if momento_del_dia == "noche":
            if estado_del_espectador == "solo":
                sumar_puntos_genero(catalogo_activo, genero_preferido, 4.0)
        elif momento_del_dia == "mañana":
            if estado_del_espectador == "familia":
                sumar_puntos_genero(catalogo_activo, "animacion", 3.5)
                sumar_puntos_genero(catalogo_activo, "comedia", 2.0)

    elif genero_preferido == "romance":
        if estado_del_espectador == "pareja":
            if momento_del_dia == "noche" or momento_del_dia == "tarde":
                sumar_puntos_genero(catalogo_activo, "romance", 4.0)

    elif genero_preferido == "animacion" or genero_preferido == "comedia":
        if estado_del_espectador == "familia":
            sumar_puntos_genero(catalogo_activo, genero_preferido, 3.5)

# R-Género 2: genero_preferido + tiempo_disponible + nivel_exigencia
def regla_genero_tiempo_exigencia(catalogo_activo, genero_preferido, tiempo_disponible, nivel_exigencia):

    if tiempo_disponible <= 60:
        if nivel_exigencia >= 7:
            sumar_puntos_valoracion(catalogo_activo, 8.0, 3.5)
        elif nivel_exigencia <= 3:
            sumar_puntos_genero(catalogo_activo, genero_preferido, 2.5)

    elif tiempo_disponible >= 120:
        if nivel_exigencia <= 3:
            sumar_puntos_genero(catalogo_activo, genero_preferido, 3.0)
        elif nivel_exigencia >= 7:
            sumar_puntos_valoracion(catalogo_activo, 8.5, 4.0)

# R-Género 3: genero_preferido + idioma + contenido_visto_x_semana
def regla_genero_idioma_habito(catalogo_activo, genero_preferido, idioma, contenido_visto_x_semana):

    if contenido_visto_x_semana >= 5:
        if idioma == "ingles" or idioma == "cualquiera":
            sumar_puntos_valoracion(catalogo_activo, 7.5, 3.5)
        elif idioma == "español":
            sumar_puntos_genero(catalogo_activo, genero_preferido, 3.0)

    elif contenido_visto_x_semana <= 2:
        if idioma == "español":
            sumar_puntos_genero(catalogo_activo, genero_preferido, 3.5)
        elif idioma == "ingles" or idioma == "cualquiera":
            sumar_puntos_valoracion(catalogo_activo, 8.0, 3.0)

# R-Género 4: genero_preferido + edad + estado_animo
def regla_genero_edad_animo(catalogo_activo, genero_preferido, edad, estado_animo):

    generos_pesados = ["terror", "drama", "thriller"]

    if edad <= 17:
        if not (genero_preferido in generos_pesados):
            sumar_puntos_genero(catalogo_activo, genero_preferido, 3.5)
        else:
            sumar_puntos_genero(catalogo_activo, "animacion", 4.0)

    elif edad >= 18:
        if 1 <= estado_animo <= 3:
            if not (genero_preferido in generos_pesados):
                sumar_puntos_genero(catalogo_activo, genero_preferido, 3.5)
        elif 8 <= estado_animo <= 10:
            sumar_puntos_genero(catalogo_activo, genero_preferido, 4.0)

#R-Exigencia 1 — nivel_exigencia + contenido_visto_x_semana + momento_del_dia
def regla_exigencia_habito_momento(catalogo_activo, nivel_exigencia, contenido_visto_x_semana, momento_del_dia):

    if nivel_exigencia >= 6:
        if contenido_visto_x_semana >= 4:
            if momento_del_dia == "noche":
                sumar_puntos_valoracion(catalogo_activo, 8.5, 4.0)
            elif momento_del_dia == "tarde":
                sumar_puntos_valoracion(catalogo_activo, 8.0, 3.5)
            elif momento_del_dia == "mañana":
                sumar_puntos_valoracion(catalogo_activo, 7.5, 3.0)
        else:
            if momento_del_dia == "noche":
                sumar_puntos_valoracion(catalogo_activo, 7.5, 3.5)
            elif momento_del_dia == "tarde":
                sumar_puntos_valoracion(catalogo_activo, 7.0, 3.0)
            elif momento_del_dia == "mañana":
                sumar_puntos_valoracion(catalogo_activo, 6.5, 2.5)

    else:
        if contenido_visto_x_semana >= 4:
            if momento_del_dia == "noche":
                sumar_puntos_valoracion(catalogo_activo, 6.0, 3.0)
            elif momento_del_dia == "tarde":
                sumar_puntos_valoracion(catalogo_activo, 5.5, 2.5)
            elif momento_del_dia == "mañana":
                sumar_puntos_valoracion(catalogo_activo, 5.0, 2.5)
        else:
            if momento_del_dia == "noche":
                sumar_puntos_valoracion(catalogo_activo, 4.5, 3.0)
            elif momento_del_dia == "tarde":
                sumar_puntos_valoracion(catalogo_activo, 4.0, 2.5)
            elif momento_del_dia == "mañana":
                sumar_puntos_valoracion(catalogo_activo, 3.5, 2.0)

#R-Exigencia 2 — nivel_exigencia + edad + idioma
def regla_exigencia_edad_idioma(catalogo_activo, nivel_exigencia, edad, idioma):

    if nivel_exigencia >= 6:
        if edad >= 18:
            if idioma == "ingles" or idioma == "cualquiera":
                sumar_puntos_valoracion(catalogo_activo, 8.5, 4.0)
            elif idioma == "español":
                sumar_puntos_valoracion(catalogo_activo, 8.0, 3.5)
        else:
            if idioma == "ingles" or idioma == "cualquiera":
                sumar_puntos_valoracion(catalogo_activo, 7.5, 3.5)
            elif idioma == "español":
                sumar_puntos_valoracion(catalogo_activo, 7.0, 3.0)

    else:
        if edad >= 18:
            if idioma == "ingles" or idioma == "cualquiera":
                sumar_puntos_valoracion(catalogo_activo, 6.0, 3.0)
            elif idioma == "español":
                sumar_puntos_valoracion(catalogo_activo, 5.5, 2.5)
        else:
            if idioma == "ingles" or idioma == "cualquiera":
                sumar_puntos_valoracion(catalogo_activo, 4.5, 2.5)
            elif idioma == "español":
                sumar_puntos_valoracion(catalogo_activo, 4.0, 2.0)

#R-Exigencia 3 — nivel_exigencia + estado_del_espectador + estado_animo
def regla_exigencia_espectador_animo(catalogo_activo, nivel_exigencia, estado_del_espectador, estado_animo):

    if nivel_exigencia >= 6:
        if estado_del_espectador == "solo":
            if estado_animo >= 6:
                sumar_puntos_valoracion(catalogo_activo, 8.5, 4.0)
            else:
                sumar_puntos_valoracion(catalogo_activo, 7.5, 3.5)
        elif estado_del_espectador == "pareja":
            if estado_animo >= 6:
                sumar_puntos_valoracion(catalogo_activo, 8.0, 3.5)
            else:
                sumar_puntos_valoracion(catalogo_activo, 7.0, 3.0)
        elif estado_del_espectador == "familia":
            if estado_animo >= 6:
                sumar_puntos_valoracion(catalogo_activo, 7.5, 3.5)
            else:
                sumar_puntos_valoracion(catalogo_activo, 6.5, 3.0)

    else:
        if estado_del_espectador == "solo":
            if estado_animo >= 6:
                sumar_puntos_valoracion(catalogo_activo, 6.0, 3.0)
            else:
                sumar_puntos_valoracion(catalogo_activo, 5.0, 2.5)
        elif estado_del_espectador == "pareja":
            if estado_animo >= 6:
                sumar_puntos_valoracion(catalogo_activo, 5.5, 2.5)
            else:
                sumar_puntos_valoracion(catalogo_activo, 4.5, 2.0)
        elif estado_del_espectador == "familia":
            if estado_animo >= 6:
                sumar_puntos_valoracion(catalogo_activo, 5.0, 2.5)
            else:
                sumar_puntos_valoracion(catalogo_activo, 4.0, 2.0)

#R-Exigencia 4 — nivel_exigencia + contenido_visto_x_semana + idioma
def regla_exigencia_habito_idioma(catalogo_activo, nivel_exigencia, contenido_visto_x_semana, idioma):

    if nivel_exigencia >= 6:
        if contenido_visto_x_semana >= 4:
            if idioma == "ingles" or idioma == "cualquiera":
                sumar_puntos_valoracion(catalogo_activo, 8.5, 4.0)
            elif idioma == "español":
                sumar_puntos_valoracion(catalogo_activo, 8.0, 3.5)
        else:
            if idioma == "ingles" or idioma == "cualquiera":
                sumar_puntos_valoracion(catalogo_activo, 7.5, 3.5)
            elif idioma == "español":
                sumar_puntos_valoracion(catalogo_activo, 7.0, 3.0)

    else:
        if contenido_visto_x_semana >= 4:
            if idioma == "ingles" or idioma == "cualquiera":
                sumar_puntos_valoracion(catalogo_activo, 6.0, 3.0)
            elif idioma == "español":
                sumar_puntos_valoracion(catalogo_activo, 5.5, 2.5)
        else:
            if idioma == "ingles" or idioma == "cualquiera":
                sumar_puntos_valoracion(catalogo_activo, 4.5, 2.5)
            elif idioma == "español":
                sumar_puntos_valoracion(catalogo_activo, 4.0, 2.0)

#R-Eje 1 — Año + edad + tiempo_disponible
def regla_año_edad_tiempo(catalogo_activo, edad, tiempo_disponible):

    if edad <= 30:
        if tiempo_disponible >= 90:
            sumar_puntos_año(catalogo_activo, 2015, 3.5)
        else:
            sumar_puntos_año(catalogo_activo, 2018, 3.0)
    else:
        if tiempo_disponible >= 90:
            sumar_puntos_año(catalogo_activo, 2000, 3.0)
        else:
            sumar_puntos_año(catalogo_activo, 2010, 2.5)

#R-Eje 2 — Índice de disponibilidad + contenido_visto_x_semana + idioma
def regla_indice_habito_idioma(catalogo_activo, indice_disponibilidad, contenido_visto_x_semana, idioma):

    disponibilidad = definir_indice_disponibilidad(indice_disponibilidad)

    if disponibilidad in ["alta", "muy_alta"]:
        if contenido_visto_x_semana >= 4:
            if idioma == "ingles" or idioma == "cualquiera":
                sumar_puntos_valoracion(catalogo_activo, 8.0, 4.0)
            else:
                sumar_puntos_valoracion(catalogo_activo, 7.5, 3.5)
        else:
            sumar_puntos_valoracion(catalogo_activo, 7.0, 3.0)
    else:
        if contenido_visto_x_semana >= 4:
            sumar_puntos_valoracion(catalogo_activo, 5.5, 2.5)
        else:
            sumar_puntos_valoracion(catalogo_activo, 4.5, 2.0)

#R-Eje 3 — Perfil del consumidor + nivel_exigencia + estado_del_espectador
def regla_perfil_exigencia_espectador(catalogo_activo, contenido_visto_x_semana, nivel_exigencia, estado_del_espectador):

    perfil = definir_perfil_consumidor(contenido_visto_x_semana)

    if perfil == "cinefilo":
        if nivel_exigencia >= 6:
            sumar_puntos_valoracion(catalogo_activo, 8.5, 4.0)
        else:
            sumar_puntos_valoracion(catalogo_activo, 7.0, 3.0)
    elif perfil == "habitual":
        if estado_del_espectador == "solo":
            sumar_puntos_valoracion(catalogo_activo, 7.0, 3.0)
        else:
            sumar_puntos_valoracion(catalogo_activo, 6.0, 2.5)
    else:  # casual
        sumar_puntos_valoracion(catalogo_activo, 5.0, 2.5)

def regla_edad_momento_simple(catalogo_activo, edad, momento_del_dia): 

    if edad <= 17:
        if momento_del_dia == "noche":
            sumar_puntos_genero(catalogo_activo, "comedia", 3.0)
        else:
            sumar_puntos_genero(catalogo_activo, "animacion", 3.5)
    else:
        if momento_del_dia == "noche":
            sumar_puntos_genero(catalogo_activo, "thriller", 3.0)
        else:
            sumar_puntos_genero(catalogo_activo, "drama", 2.5)