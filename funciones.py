import json

with open ('info-hoteles.json','r') as fichero:
    datos = json.load(fichero)

#Funcion: Listar información: Listar los hoteles que tengan 4 estrellas (****)
def hoteles_cuatro_estrellas(datos):
    lista = []
    for dato in datos["resources"]:
        if dato["dc:title"][0:5] == "**** ":
            lista.append(dato["dc:title"])
    return lista


#Funcion: Contar información: Contar los hoteles que existen, ordenados por estrellas, es decir, mostrara el numero de hoteles que hay con 5 estrellas, con 4 estrellas, etc...
#def contar_hoteles(datos):   
#	lista = []
#	fivestarts = 0
#	fourstarts = 0 
#	threestarts = 0
#	twostarts = 0
#	onestart = 0
#	for d in datos["resources"]:
#		if d["dc:title"].count("*") == 5:
#			fivestarts += 1
#			lista.append(fivestarts)
#		if d["dc:title"].count("*") == 4:
#			fourstarts += 1
#			lista.append(fourstarts)
#		if d["dc:title"].count("*") == 3:
#			threestarts += 1
#			lista.append(threestarts)
#		if d["dc:title"].count("*") == 2:
#			twostarts += 1
#			lista.append(twostarts)
#		if d["dc:title"].count("*") == 1:
#			onestart += 1
#			lista.append(onestart)
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

##Funcion: Ejercicio libre: Pide por teclado el nombre de un hotel sin estrellas (ya que tenemos que tener en cuenta que los nombres de los hoteles de nuestro fichero empiezan con "*" que son las estrellas )y nos devuelve su pagina web.
def ejercicio_libre(datos,nombre_web):
    lista = []
    for dato in datos["resources"]:
        if dato["lpgc:web"] == nombre_web:
            dict = {}
            dict["Descripcion"] = dato["dc:description"]
            dict["Direccion-Hotel"] = dato["lpgc:direccion"]
            lista.append(dict)
    return lista 

