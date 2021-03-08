from funciones import *

import json

with open ('info-hoteles.json','r') as fichero:
    datos = json.load(fichero)

print("--------")
print("- MENU -")
print("--------")
menu = '''1. Listar información
2. Contar información
3. Buscar o filtrar información
4. Buscar información relacionada
5. Ejercicio libre
6. Salir'''

print(menu)

opcion = int(input("Opción: "))
while opcion <1 or opcion >6:
    print("Opcion Incorrecta")
    opcion = int(input("Opción: "))

while opcion !=6:
    #Listar información: Listar los hoteles que tengan 4 estrellas (****)
    if opcion == 1:
        print("HOTELES 4 ESTRELLAS: ")
        print("---------------------")
        for elem in hoteles_cuatro_estrellas(datos):
            print(elem)
    #Contar información: Contar los hoteles que existen, ordenados por estrellas, es decir, mostrara el numero de hoteles que hay con 5 estrellas, con 4 estrellas, etc...
    elif opcion == 2:
        for i in contar_hoteles(datos):
            print("Hoteles de 5 estrellas: " + int(i)[0])
            print("Hoteles de 4 estrellas: " + int(i)[1])
            print("Hoteles de 3 estrellas: " + int(i)[2])
            print("Hoteles de 2 estrellas: " + int(i)[3])
            print("Hoteles de 1 estrella: " + int(i)[4])
    ##Buscar o filtrar información: Pide por teclado una categoria de precio por teclado (Economico, Medio, Alto) y te muestra los hoteles que tienen esa categoria de precio.
    #elif opcion == 3:
    #    print("HOTELES POR CATEGORIAS: ")
    #    print("------------------------")
    #    lista = ['caro','normal','barato']
    #    print("Categorias: ")
    #    for i in lista:
    #        print(i)
    #    categoria = input("Introduce la categoria: ")
    #    for elem in categoria_por_precio(datos,categoria):
    #        if categoria == "caro":
    #            for c in elem[0]:
    #                print(c)
    #        if categoria == "normal":
    #            for n in elem[1]:
    #                print(n)
    #        if categoria == "barato":
    #            for b in elem[2]:
    #                print(b)
    #Buscar información relacionada: Pide por teclado los dos ultimos numeros del telefono y nos mostrara la lista de telefonos que coinciden junto con el nombre del hotel.
    elif opcion == 4:
        print("NUMEROS DE TELEFONO: ")
        #for dato in datos["resources"]:
        #    for elem in dato:
        #Mostrar telefonos
        num = input("Ultimos dos digitos de numero de telefono:" )
        print("-------------------------------------------------")
        for i in buscar_informacion(datos,num):
            print(i)
    #Ejercicio libre: Pide por teclado el nombre de un hotel sin estrellas (ya que tenemos que tener en cuenta que los nombres de los hoteles de nuestro fichero empiezan con "*" que son las estrellas )y nos devuelve su pagina web.
    elif opcion == 5:
        nombre_web = input("Nombre Web: ")
        for i in ejercicio_libre(datos,nombre_web):
            print("Descripcion", i["dc:description"],"\t Direccion: ", i["lpgc:direccion"])
    print("--------")
    print("- MENU -")
    print("--------")
    print(menu)
    opcion = int(input("Opción: "))
    while opcion <1 or opcion >6:
        print("Opcion Incorrecta")
        opcion = int(input("Opción: "))
        

