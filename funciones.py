import json

#Funcion: Listar información: Listar los hoteles que tengan 4 estrellas (****)
def hoteles_cuatro_estrellas(datos):
    lista = []
    for dato in datos["resources"]:
        if dato["dc:title"][0:5] == "**** ":
            lista.append(dato["dc:title"])
    return lista


#Funcion: Contar información: Contar los hoteles que existen, ordenados por estrellas, es decir, mostrara el numero de hoteles que hay con 5 estrellas, con 4 estrellas, etc...
#def contar_hoteles(datos):
#    lista = []
#    una_estrella = 0 
#    dos_estrellas = 0
#    tres_estrellas = 0
#    cuatro_estrellas = 0
#    cinco_estrellas = 0
#    for dato in datos["resources"]:
#        if dato["dc:title"].count("*") == 5:
#            cinco_estrellas = cinco_estrellas + 1
#            lista.append(int((cinco_estrellas))
#        if dato["dc:title"].count("*") == 4:
#            cuatro_estrellas = cuatro_estrellas + 1
#            lista.append(int((cuatro_estrellas))
#        if dato["dc:title"].count("*") == 3:
#            tres_estrellas = tres_estrellas + 1
#            lista.append(int((tres_estrellas))
#        if dato["dc:title"].count("*") == 2:
#            dos_estrellas = dos_estrellas + 1
#            lista.append(int((dos_estrellas))
#        if dato["dc:title"].count("*") == 1:
#            una_estrella = una_estrella + 1
#            lista.append(int(una_estrella))
#    return lista 


#Funcion: Buscar o filtrar información: Pide por teclado una categoria de precio por teclado (Economico, Medio, Alto) y te muestra los hoteles que tienen esa categoria de precio.
#def categoria_por_precio(datos,categoria):
#    caros = []
#    normales = []
#    baratos = []
#    for dato in datos["resources"]:
#	    if dato["lpgc:precio"] == "alto":
#		    caros.append(dato["dc:title"])
#        if dato["lpgc:precio"] == "medio":
#		    normales.append(dato["dc:title"])
#        if dato["lpgc:precio"] == "Económico":
#		    baratos.append(dato["dc:title"])
#    lista = [caros,normales,baratos]
#    return lista


#Funcion: Buscar información relacionada: Pide por teclado los dos ultimos numeros del telefono y nos mostrara la lista de telefonos que coinciden junto con el nombre del hotel.
def buscar_informacion(datos,num):
    lista = []
    for dato in datos["resources"]:
	    if dato["lpgc:telefono"][-2:] == num:
		    lista.append("Nombre Hotel: " + dato["dc:title"] + " | Numero Telefono: " + dato["lpgc:telefono"]) 
    return lista 

#Funcion: Ejercicio libre: Pide por teclado el nombre de un hotel sin estrellas (ya que tenemos que tener en cuenta que los nombres de los hoteles de nuestro fichero empiezan con "*" que son las estrellas )y nos devuelve su pagina web.
def ejercicio_libre(datos):
    hoteles = {}
    for d in datos["resources"]:
	    if d["dc:title"].count("*") == 5:
		    d["dc:title"] = d["dc:title"].lstrip("***** ")
		    key = d["dc:title"] 
		    value = d["lpgc:web"]
		    hoteles[key] = value
	    elif d["dc:title"].count("*") == 4:
		    d["dc:title"] = d["dc:title"].lstrip("**** ")
		    key = d["dc:title"] 
		    value = d["lpgc:web"]
		    hoteles[key] = value
	    elif d["dc:title"].count("*") == 3:
		    d["dc:title"] = d["dc:title"].lstrip("*** ")
		    key = d["dc:title"] 
		    value = d["lpgc:web"]
		    hoteles[key] = value
	    elif d["dc:title"].count("*") == 2:
		    d["dc:title"] = d["dc:title"].lstrip("** ")
		    key = d["dc:title"] 
		    value = d["lpgc:web"]
		    hoteles[key] = value
	    elif d["dc:title"].count("*") == 1:
		    d["dc:title"] = d["dc:title"].lstrip("* ")
		    key = d["dc:title"] 
		    value = d["lpgc:web"]
		    hoteles[key] = value
	    else:
		    key = d["dc:title"] 
		    value = d["lpgc:web"]
		    hoteles[key] = value
    return 

