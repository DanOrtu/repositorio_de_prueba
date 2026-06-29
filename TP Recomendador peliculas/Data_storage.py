#diccionario del usuario
usuario = {          
    "nombre": None,
    "edad": None,
    "estado_animo": None,
    "contenido_visto_x_semana": None,
    "nivel_exigencia": None,
    "tiempo_disponible": None,
    "tipo_de_contenido": None,
    "estado_del_espectador": None,
    "momento_del_dia": None,
    "genero_preferido": None,
    "idioma": None
}

tipos_contenido = ["serie", "pelicula"]

momentos_dia = ["mañana", "tarde", "noche"]

estados_espectador = ["solo", "pareja", "familia"]

generos = [
    "accion",
    "comedia",
    "drama",
    "terror",
    "romance",
    "thriller",
    "ciencia_ficcion",
    "animacion",
    "documental"
]

idiomas = ["español", "ingles", "cualquiera"]

#lista de diccionarios de películas
peliculas = [
    # ACCION
    {"nombre": "Mad Max: Fury Road", "genero": "accion", "año": 2015, "valoracion": 8.1, "puntos": 0},
    {"nombre": "The Expendables", "genero": "accion", "año": 2010, "valoracion": 6.4, "puntos": 0},
    {"nombre": "xXx: State of the Union", "genero": "accion", "año": 2005, "valoracion": 4.5, "puntos": 0},

    # COMEDIA
    {"nombre": "The Grand Budapest Hotel", "genero": "comedia", "año": 2014, "valoracion": 8.1, "puntos": 0},
    {"nombre": "We're the Millers", "genero": "comedia", "año": 2013, "valoracion": 7.0, "puntos": 0},
    {"nombre": "Jack and Jill", "genero": "comedia", "año": 2011, "valoracion": 3.3, "puntos": 0},

    # DRAMA
    {"nombre": "The Shawshank Redemption", "genero": "drama", "año": 1994, "valoracion": 9.3, "puntos": 0},
    {"nombre": "The Pursuit of Happyness", "genero": "drama", "año": 2006, "valoracion": 8.0, "puntos": 0},
    {"nombre": "After Earth", "genero": "drama", "año": 2013, "valoracion": 4.8, "puntos": 0},

    # TERROR
    {"nombre": "The Shining", "genero": "terror", "año": 1980, "valoracion": 8.4, "puntos": 0},
    {"nombre": "Insidious", "genero": "terror", "año": 2010, "valoracion": 6.8, "puntos": 0},
    {"nombre": "Slender Man", "genero": "terror", "año": 2018, "valoracion": 3.2, "puntos": 0},

    # ROMANCE
    {"nombre": "The Notebook", "genero": "romance", "año": 2004, "valoracion": 7.8, "puntos": 0},
    {"nombre": "Dear John", "genero": "romance", "año": 2010, "valoracion": 6.3, "puntos": 0},
    {"nombre": "Endless Love", "genero": "romance", "año": 2014, "valoracion": 4.1, "puntos": 0},

    # THRILLER
    {"nombre": "Se7en", "genero": "thriller", "año": 1995, "valoracion": 8.6, "puntos": 0},
    {"nombre": "The Call", "genero": "thriller", "año": 2013, "valoracion": 6.7, "puntos": 0},
    {"nombre": "The Snowman", "genero": "thriller", "año": 2017, "valoracion": 5.1, "puntos": 0},

    # CIENCIA FICCION
    {"nombre": "Interstellar", "genero": "ciencia_ficcion", "año": 2014, "valoracion": 8.7, "puntos": 0},
    {"nombre": "Oblivion", "genero": "ciencia_ficcion", "año": 2013, "valoracion": 7.0, "puntos": 0},
    {"nombre": "Battlefield Earth", "genero": "ciencia_ficcion", "año": 2000, "valoracion": 2.5, "puntos": 0},

    # ANIMACION
    {"nombre": "Spider-Man: Into the Spider-Verse", "genero": "animacion", "año": 2018, "valoracion": 8.4, "puntos": 0},
    {"nombre": "The Croods", "genero": "animacion", "año": 2013, "valoracion": 7.2, "puntos": 0},
    {"nombre": "Norm of the North", "genero": "animacion", "año": 2016, "valoracion": 3.4, "puntos": 0},

    # DOCUMENTAL
    {"nombre": "Planet Earth", "genero": "documental", "año": 2006, "valoracion": 9.4, "puntos": 0},
    {"nombre": "Minimalism", "genero": "documental", "año": 2016, "valoracion": 6.7, "puntos": 0},
    {"nombre": "The Secret", "genero": "documental", "año": 2006, "valoracion": 5.5, "puntos": 0}
]

#lista de diccionario de series
series = [
    # ACCION
    {"nombre": "Breaking Bad", "genero": "accion", "año": 2008, "valoracion": 9.5, "puntos": 0},
    {"nombre": "Reacher", "genero": "accion", "año": 2022, "valoracion": 8.0, "puntos": 0},
    {"nombre": "Inhumans", "genero": "accion", "año": 2017, "valoracion": 4.9, "puntos": 0},

    # COMEDIA
    {"nombre": "The Office", "genero": "comedia", "año": 2005, "valoracion": 9.0, "puntos": 0},
    {"nombre": "Brooklyn Nine-Nine", "genero": "comedia", "año": 2013, "valoracion": 8.4, "puntos": 0},
    {"nombre": "Blockbuster", "genero": "comedia", "año": 2022, "valoracion": 5.1, "puntos": 0},

    # DRAMA
    {"nombre": "Chernobyl", "genero": "drama", "año": 2019, "valoracion": 9.3, "puntos": 0},
    {"nombre": "The Crown", "genero": "drama", "año": 2016, "valoracion": 8.6, "puntos": 0},
    {"nombre": "Another Life", "genero": "drama", "año": 2019, "valoracion": 5.3, "puntos": 0},

    # TERROR
    {"nombre": "The Haunting of Hill House", "genero": "terror", "año": 2018, "valoracion": 8.6, "puntos": 0},
    {"nombre": "Marianne", "genero": "terror", "año": 2019, "valoracion": 7.4, "puntos": 0},
    {"nombre": "Resident Evil", "genero": "terror", "año": 2022, "valoracion": 4.2, "puntos": 0},

    # ROMANCE
    {"nombre": "Bridgerton", "genero": "romance", "año": 2020, "valoracion": 7.4, "puntos": 0},
    {"nombre": "Virgin River", "genero": "romance", "año": 2019, "valoracion": 7.0, "puntos": 0},
    {"nombre": "Valeria", "genero": "romance", "año": 2020, "valoracion": 5.8, "puntos": 0},

    # THRILLER
    {"nombre": "Mindhunter", "genero": "thriller", "año": 2017, "valoracion": 8.6, "puntos": 0},
    {"nombre": "The Night Agent", "genero": "thriller", "año": 2023, "valoracion": 7.5, "puntos": 0},
    {"nombre": "Clickbait", "genero": "thriller", "año": 2021, "valoracion": 5.9, "puntos": 0},

    # CIENCIA FICCION
    {"nombre": "Dark", "genero": "ciencia_ficcion", "año": 2017, "valoracion": 8.7, "puntos": 0},
    {"nombre": "Lost in Space", "genero": "ciencia_ficcion", "año": 2018, "valoracion": 7.3, "puntos": 0},
    {"nombre": "Another Life", "genero": "ciencia_ficcion", "año": 2019, "valoracion": 5.3, "puntos": 0},

    # ANIMACION
    {"nombre": "Arcane", "genero": "animacion", "año": 2021, "valoracion": 9.0, "puntos": 0},
    {"nombre": "Avatar: The Last Airbender", "genero": "animacion", "año": 2005, "valoracion": 8.3, "puntos": 0},
    {"nombre": "Velma", "genero": "animacion", "año": 2023, "valoracion": 1.6, "puntos": 0},

    # DOCUMENTAL
    {"nombre": "Planet Earth II", "genero": "documental", "año": 2016, "valoracion": 9.5, "puntos": 0},
    {"nombre": "Our Planet", "genero": "documental", "año": 2019, "valoracion": 8.9, "puntos": 0},
    {"nombre": "Ancient Apocalypse", "genero": "documental", "año": 2022, "valoracion": 5.5, "puntos": 0}
]