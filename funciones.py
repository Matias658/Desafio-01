import os
from data_stark import *
#*************************************************DESAFÍO 00***************************************************************************
def recorrer_lista(lista:list):
    for item in lista:
        print(item)
        print("-------------------------------------")
#--------------------------------------------------------------------------------------------------------------------------------------
#Recorrer nombres y alturas
def nombres_alturas_heroes(lista:list, key:str, key2:str = False)->list:
    lista_nombres_alturas = []
    for persona in lista:
        nombre = persona[key]
        if key2 == False:
            lista_nombres_alturas.append(nombre)
        else:
            altura = persona[key2]
            lista_nombres_alturas.append(nombre)
            lista_nombres_alturas.append(altura)

    return lista_nombres_alturas
#--------------------------------------------------------------------------------------------------------------------------------------
#Encontrar el valor maximo de lo que quieras.
def encontrar_max_min(lista:list, key:str, key2:str = False, maximo:bool = True, minimo:bool = False)->list:
    
    lista_maxima_minima = []
    if maximo:
        flag_valor_maxima = True
        valor_maxima = None
        for valor in lista:
            if flag_valor_maxima or float(valor[key]) > float(valor_maxima):
                valor_maxima = valor[key]
                nombre = valor[key2]
                flag_valor_maxima = False
        lista_maxima_minima.append(valor_maxima)
        lista_maxima_minima.append(nombre)
    if minimo:
        flag_valor_minima = True
        valor_minima = None
        
        for bajo in lista:
            if flag_valor_minima or float(valor_minima) > float(bajo[key]):
                valor_minima = bajo[key]
                nombre = bajo[key2]
                flag_valor_minima = False
        lista_maxima_minima.append(valor_minima)
        lista_maxima_minima.append(nombre)
    return lista_maxima_minima
#--------------------------------------------------------------------------------------------------------------------------------------
#Promedio
def sacar_promedio(lista:list, key:str)->float:
    altura_total = 0
    for item in lista:
        altura = float(item[key])
        altura_total += altura
        promedio = altura_total / len(lista)
    return promedio
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#*************************************************DESAFÍO 01***************************************************************************
#Filtrar lista
def filtrar_lista(lista:list, key:str, key2:str, key3:str, key4:str = False)->list:
    lista_filtrada = []
    
    for item in lista:
        if key3 in item[key2] and key4:
            lista_filtrada.append({key:item[key], key4:float(item[key4])})
        elif key3 in item[key2]:
            lista_filtrada.append(item[key])
    return lista_filtrada
#--------------------------------------------------------------------------------------------------------------------------------------
#Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def esta_en_lista(lista:list, item:str)->bool: 
    esta = False
    for elemento in lista:
        if elemento == item:
            esta = True
            break
    return esta

def contar_repetidos(lista:list, key:str, key2:str)->list:
    lista_sin_repetir = []
    color_ojos = []
    for item in lista:
        if not esta_en_lista(lista_sin_repetir, item[key]):
            lista_sin_repetir.append(item[key])

    for elemento in lista_sin_repetir:
        contador = 0
        for i in lista:
            if i[key] == elemento:
                contador += 1
        color_ojos.append({key:elemento, key2:contador})
        
    return color_ojos
#--------------------------------------------------------------------------------------------------------------------------------------
#Listar todos los superhéroes agrupados por color de ojos./pelo/inteligencia
def listar_por_tipo(lista:list, key:str, key2:str)->None:
    lista_heores = []
    for item in lista:
        if not esta_en_lista(lista_heores, item[key]) or item[key] == "":
            if item[key] == "":
                item[key] = "No tiene"
            lista_heores.append(item[key])
            

    for elemento in lista_heores:
        print(f"{elemento}\n")
        for i in lista:
            if i[key] == elemento:
                print(i[key2])
        print("-----------------------------------")
        
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#MENÚS :D
def menu():
    os.system("cls")
    print("""***Bienvenidos a las Industrias Stark***
************Menu de Opciones************
1-Nombre de cada SuperHeroe
2-Nombre y alturas de cada SuperHeroe
3-Altura del SuperHeroe más alto
4-Altura del SuperHeroe más bajo
5-Altura promedio
6-SuperHeroe más pesado
7-SuperHeroe menos pesado
8-Siguiente menú
9-Salir""")
    while True:
        try:
            x = int(input("Ingrese una opcion: "))
        except ValueError:
            print("ERROR. Eso no es un número")
        else:
            return x
#--------------------------------------------------------------------------------------------------------------------------------------
#Elegir opción 00
def elegir_opcion(x):
    match x:
        case 1:
            recorrer_lista(nombres_alturas_heroes(lista_personajes, "nombre", False))
        case 2:
            recorrer_lista(nombres_alturas_heroes(lista_personajes, "nombre", "altura"))
        case 3:
            max_min = encontrar_max_min(lista_personajes, 'altura', 'nombre', True)
            print(f"El heroe más alto es: {(max_min[1])}, Midiendo: {float(max_min[0])}")
        case 4:
            max_min = encontrar_max_min(lista_personajes, 'altura', 'nombre',False, True)
            print(f"El heroe más bajo es: {(max_min[1])}, Midiendo: {float(max_min[0])}")
        case 5:
            promedio = sacar_promedio(lista_personajes, "altura")
            print(round(promedio, 2))
        case 6:
            max_min = encontrar_max_min(lista_personajes, 'peso', 'nombre',True)
            print(f"El heroe más pesado es: {(max_min[1])}, Pesando: {float(max_min[0])}")
        case 7:
            max_min = encontrar_max_min(lista_personajes, 'peso', 'nombre',False, True)
            print(f"El heroe menos pesado es: {(max_min[1])}, Pesando: {float(max_min[0])}")
        case 8:
            return x
        case 9:
            y = input("Seguro que desea salir? s/n: ")
            return y
        case _:
            print("ERROR. Opción inválida")
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
def segundo_menu():
    os.system("cls")
    print("""***Bienvenidos a las Industrias Stark***
************Menu de Opciones 2**********
1-Nombre de cada SuperHeroe masculino
2-Nombre de cada SuperHero femenino
3-SuperHeroe más alto
4-SuperHeroína más alta
5-SuperHeroe más bajo
6-SuperHeroína más baja
7-Altura promedio de los Superheroes
8-Altura promedio de las SuperHeroínas
9-Color de ojos de todos los SuperHeroes
10-Color de pelo de todos los SuperHeroes
11-tipo de inteligencia de todos los SuperHeroes
12-Listar todos los superhéroes agrupados por color de ojos.
13-Listar todos los superhéroes agrupados por color de pelo.
14-Listar todos los superhéroes agrupados por tipo de inteligencia
15-Volver al menu anterior
16-Siguiente menú
17-Salir""")
    while True:
        try:
            x = int(input("Ingrese una opcion: "))
        except ValueError:
            print("ERROR. Eso no es un número")
        else:
            return x
#--------------------------------------------------------------------------------------------------------------------------------------
#Elegir opcion 01
def segundo_elegir_opcion(x):
    match x:
        case 1:
            hombres = filtrar_lista(lista_personajes, 'nombre', 'genero', 'M')
            recorrer_lista(hombres)
        case 2:
            mujeres = filtrar_lista(lista_personajes, 'nombre', 'genero', 'F')
            recorrer_lista(mujeres)
        case 3:
            hombres = filtrar_lista(lista_personajes, 'nombre', 'genero', 'M', 'altura')
            hombre_alto = encontrar_max_min(hombres, 'altura','nombre', True)
            print(f"El heroe masculino más alto es: {hombre_alto[1]} Midiendo: {float(hombre_alto[0])}")
        case 4:
            mujeres = filtrar_lista(lista_personajes, 'nombre', 'genero', 'F', 'altura')
            mujer_alta = encontrar_max_min(mujeres, 'altura','nombre', True)
            print(f"La heroína más alta es: {mujer_alta[1]} Midiendo: {float(mujer_alta[0])}") 
        case 5:
            hombres = filtrar_lista(lista_personajes, 'nombre', 'genero', 'M', 'altura')
            hombre_bajo = encontrar_max_min(hombres, 'altura','nombre', False, True)
            print(f"El heroe masculino más bajo es: {hombre_bajo[1]} Midiendo: {float(hombre_bajo[0])}")
        case 6:
            mujeres = filtrar_lista(lista_personajes, 'nombre', 'genero', 'F', 'altura')
            mujer_baja = encontrar_max_min(mujeres, 'altura','nombre', False, True)
            print(f"La heroína más baja es: {mujer_baja[1]} Midiendo: {float(mujer_baja[0])}")  
        case 7:
            hombres = filtrar_lista(lista_personajes, 'nombre', 'genero', 'M', 'altura')
            promedio = sacar_promedio(hombres, "altura")
            print(f"El promedio de los heroes masculinos es: {round(promedio, 2)}") 
        case 8:
            mujeres = filtrar_lista(lista_personajes, 'nombre', 'genero', 'F', 'altura')
            promedio = sacar_promedio(mujeres, "altura")
            print(f"El promedio de las heroínas es: {round(promedio, 2)}") 
        case 9:
            color_ojos = contar_repetidos(lista_personajes, "color_ojos", "cantidad") 
            for item in color_ojos:
                print(f"Color de ojos: {item['color_ojos']} Cantidad: {item['cantidad']}")
                print("-----------------------------------------------------")
        case 10: 
            color_pelo = contar_repetidos(lista_personajes, "color_pelo", "cantidad") 
            for item in color_pelo:
                if item['color_pelo'] == "":
                    item['color_pelo'] = "No tiene"
                print(f"Color de pelo: {item['color_pelo']} Cantidad: {item['cantidad']}")
                print("-----------------------------------------------------") 
        case 11:
            inteligencia = contar_repetidos(lista_personajes, "inteligencia", "cantidad") 
            for item in inteligencia:
                if item['inteligencia'] == "":
                    item['inteligencia'] = "No tiene"
                print(f"Tipo de inteligencia: {item['inteligencia']} Cantidad: {item['cantidad']}")
                print("-----------------------------------------------------")  
        case 12:
            listar_por_tipo(lista_personajes, "color_ojos", "nombre")
        case 13:
            listar_por_tipo(lista_personajes, "color_pelo", "nombre")
        case 14:
            listar_por_tipo(lista_personajes, "inteligencia", "nombre")
        case 15:
            return x    #Volver al menu anterior
        case 16:
            return x    #Menu siguiente
        case 17:
            y = input("Seguro que desea salir? s/n: ")
            return y
        case _:
            return print("ERROR. Opción inválida")
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
def tercer_menu():
    print("*******Trabajando*******")