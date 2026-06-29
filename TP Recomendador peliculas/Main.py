from colorama import *
from Input import *
from Calculos_generales import *
from Reglas import *
from Estadisticas import *
from Data_storage import *
import os



def main():
    # 1. Promedio general
    contador_general = 0 
    suma_edad = 0
    # 2. Promedio condicionado
    suma_estado_animo = 0
    contador_felices = 0
    # 3. Maximo general
    # 4. Maximo condicionado por varias variables
    contador_mayores_terror = 0
    maximo_mayores_edad = None
    # 5. Minimo (puede ser condicionado o no)
    contador_menores = 0
    # 6. Conteo de frecuencia de recomendaciones
    contador_series = 0
    contador_peliculas = 0
    # 7. Porcentajes (no condicionados y condicionados)
    contador_comedia = 0
    contador_accion = 0 
    contador_drama = 0
    contador_terror = 0
    
    while True:
        os.system("cls")
        opcion = int(input("1.Cargar usuario\n2.Realizar evaluación\n3.Mostrar recomendaciones\n4.Ver estadisticas generales\nElija una opcion: "))
        
        match opcion:
            case 1:
                os.system("cls")
                ingresar_datos(usuario, tipos_contenido, estados_espectador, momentos_dia, idiomas, generos)
                contador_general += 1
                suma_edad += usuario["edad"]
                if usuario["tipo_de_contenido"] == "serie":
                    contador_series += 1
                else:
                    contador_peliculas += 1
                tiempo_disponible_horas = calcular_horas(usuario["tiempo_disponible"])
                promedio_tiempo_pelicula = calcular_promedio_tiempo_pelicula(tiempo_disponible_horas, usuario["contenido_visto_x_semana"])
                indice_disponibilidad = calcular_indice_disponibilidad(tiempo_disponible_horas, usuario["estado_animo"], usuario["nivel_exigencia"])
            case 2:
                os.system("cls")
                catalogo_activo = definir_catalogo(usuario["tipo_de_contenido"], peliculas, series)
                regla_genero_momento_espectador(catalogo_activo, usuario["genero_preferido"], usuario["momento_del_dia"], usuario["estado_del_espectador"])
                regla_genero_tiempo_exigencia(catalogo_activo, usuario["genero_preferido"], usuario["tiempo_disponible"], usuario["nivel_exigencia"])
                regla_genero_idioma_habito(catalogo_activo, usuario["genero_preferido"], usuario["idioma"], usuario["contenido_visto_x_semana"])
                regla_genero_edad_animo(catalogo_activo, usuario["genero_preferido"], usuario["edad"], usuario["estado_animo"])
                regla_exigencia_habito_momento(catalogo_activo, usuario["nivel_exigencia"], usuario["contenido_visto_x_semana"], usuario["momento_del_dia"])
                regla_exigencia_edad_idioma(catalogo_activo, usuario["nivel_exigencia"], usuario["edad"], usuario["idioma"])
                regla_exigencia_espectador_animo(catalogo_activo, usuario["nivel_exigencia"], usuario["estado_del_espectador"], usuario["estado_animo"])
                regla_exigencia_habito_idioma(catalogo_activo, usuario["nivel_exigencia"], usuario["contenido_visto_x_semana"], usuario["idioma"])
                regla_año_edad_tiempo(catalogo_activo, usuario["edad"], usuario["tiempo_disponible"])
                regla_indice_habito_idioma(catalogo_activo, indice_disponibilidad, usuario["contenido_visto_x_semana"], usuario["idioma"])
                regla_perfil_exigencia_espectador(catalogo_activo, usuario["contenido_visto_x_semana"], usuario["nivel_exigencia"], usuario["estado_del_espectador"])
                regla_edad_momento_simple(catalogo_activo, usuario["edad"], usuario["momento_del_dia"])
            case 3:
                os.system("cls")
                mostrar_datos(catalogo_activo)
            
        os.system("pause")
        os.system("cls")

if __name__ == "__main__":
    main()
    
    
    # match genero_preferido:
    #     case "accion":
    #         contador_accion += 1
    #     case "drama":
    #         contador_drama += 1
    #     case "comedia":
    #         contador_comedia += 1
    #     case _:
    #         contador_terror += 1

    # #PROMEDIO GENERAL 
    # promedio_edad = calcular_promedios(suma_edad, contador_general)

    # #PROMEDIO CONDICIONADO  
    # if estado_animo >= 8:
    #     suma_estado_animo += estado_animo
    #     contador_felices += 1
    
    # if contador_felices > 0:
    #     promedio_estado_animo_felices = calcular_promedios(suma_estado_animo, contador_felices)
    # else:
    #     promedio_estado_animo_felices = 0

    # #MAXIMO GENERAL
    # maximo_edad = sacar_maximo(contador_general, edad)
    
    # #MAXIMO CONDICIONADO POR VARIAS VARIABLES       
    # if edad >= 18 and genero_preferido == "terror":
    #     contador_mayores_terror += 1
    #     if contador_mayores_terror == 1 or edad > maximo_mayores_edad:
    #         maximo_mayores_edad = sacar_maximo(contador_mayores_terror, edad)
    
    # #MINIMO
    # min_menores_edad = sacar_minimo(edad)
    
    # #PORCENTAJES   
    # porcentaje_accion = calcular_porcentajes(contador_accion, contador_general)
    # porcentaje_comedia = calcular_porcentajes(contador_comedia, contador_general)
    # porcentaje_drama = calcular_porcentajes(contador_drama, contador_general)
    # porcentaje_terror = calcular_porcentajes(contador_terror, contador_general)
    
    # print(Fore.CYAN + "\nRECOMENDACIÓN PERSONALIZADA")
    # print(Fore.CYAN + "====================================")

    # print(Fore.YELLOW + f"\nUsuario: {nombre}")
    # print(Fore.YELLOW + f"Edad: {edad}")
    # print(Fore.MAGENTA + f"Género preferido: {genero_preferido}")
    # print(Fore.GREEN + f"Estado de ánimo: {estado_animo}")
    # print(Fore.BLUE + f"Tiempo disponible: {tiempo_disponible_horas}\n"+ Style.RESET_ALL)
    
    # mensaje += f"Te recomendamos una {tipo_de_contenido} de {genero_preferido} "
    # mensaje += cadena_contexto
    # mensaje += f"- {cadena_complejidad_duracion}"
    # mensaje += f"- {cadena_calidad_intensidad}"
    # mensaje += f"{cadena_experiencia}\n"
    # mensaje += f"- {cadena_valoracion}"
    # mensaje += f"{cadena_disponibilidad}\n"
    # mensaje += f"\nTe recomendamos ver:\n{cadena_peliculas}\n"
    # mensaje += f"{cadena_apto}\n"
    # mensaje += cadena_compania
    
    # print(mensaje)
    
    # continuar = str(input("Desea continuar? si/no: "))

    # print("\n--- ESTADISTICAS ---")
    # print("Promedio edad:", promedio_edad)

    # if contador_felices > 0:
    #     print("Promedio estado de animo felices:", promedio_estado_animo_felices)

    # print("Maximo edad:", maximo_edad)

    # if contador_mayores_terror > 0:
    #     print("Maximo mayores que prefieren terror:", maximo_mayores_edad)
    # else:
    #     print("No hubo mayores que prefieren terror")

    # if contador_menores > 0:
    #     print("Minimo menores:", min_menores_edad)
    # else:
    #     print("No se ingresaron menores")
    # #CONTEO FRECUENCIA DE RECOMENDACIONES
    # print("Frecuencia series:", contador_series)
    # print("Frecuencia peliculas:", contador_peliculas,"\n")

    # #GRAFICOS
    # print(Fore.BLUE + "Accion: " + mostrar_barra(int(porcentaje_accion)) + f" ({porcentaje_accion}%)")
    # print(Fore.CYAN + "Comedia: " + mostrar_barra(int(porcentaje_comedia)) + f" ({porcentaje_comedia}%)")
    # print(Fore.GREEN + "Drama: " + mostrar_barra(int(porcentaje_drama)) + f" ({porcentaje_drama}%)")
    # print(Fore.YELLOW + "Terror: " + mostrar_barra(int(porcentaje_terror)) + f" ({porcentaje_terror}%)" + Style.RESET_ALL)
