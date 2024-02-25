"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

# with open("/tmp/drivers.csv", "r") as file:
#     drivers = file.readlines()

# drivers = [row.replace("\n", "") for row in drivers]
# drivers = [row.split(",") for row in drivers]
# drivers = [row[:2] for row in drivers]
# pprint(drivers[0:10])

with open("data.csv","r") as file:
    data=file.readlines()

data=[row.replace("\n"," ")for row in data]
data=[row.replace("\t",";") for row in data]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return sum([int(cadena[2]) for cadena in data])
#clprint(pregunta_01())

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
letras = [palabra[0] for palabra in data]
    letra = sorted(list(set(letras)))
    return [(vocal,letras.count(vocal)) for vocal in letra]
    """
    letters=[word[0] for word in data]
    letter=list(set(letters))
    values=[]
    for i in letter:
        count=letters.count(i)
        values.append(count)
    order=list(zip(letter,values))
    #return sorted(order,key=lambda x: x[1])
    return sorted(order)

#print(pregunta_02())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    dictionary = {}
    tupla = [(cadena[0], int(cadena[2])) for cadena in data]

    for clave, valor in tupla:
        if clave not in dictionary.keys():
            dictionary[clave] = valor
        else:
            dictionary[clave] += valor
    
    return sorted([(key,value) for key, value in dictionary.items()])
#print(pregunta_03())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    meses = [palabra[9:11] for palabra in data]
    mes = sorted(list(set(meses)))
    return [(vocal,meses.count(vocal)) for vocal in mes]

# |


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dictionary = {}
    tupla = [(cadena[0], int(cadena[2])) for cadena in data]

    for clave, valor in tupla:
        if clave not in dictionary.keys():
            dictionary[clave] = [valor]
        else:
            dictionary[clave] += [valor]
    
    return sorted([(key,max(value),min(value)) for key, value in dictionary.items()])
#print(pregunta_05())  

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lista = [cadena.split(";") for cadena in data]
    lista = [cadena[4].split(",") for cadena in lista]
    dictionary = {}
    for l in lista:
        for valores in l:
            if valores[0:3] not in dictionary.keys():
                dictionary[valores[0:3]] = [int(valores[4:])]
            else:
                dictionary[valores[0:3]] += [int(valores[4:])]
    
    return sorted([(key,min(value),max(value)) for key, value in dictionary.items()])
print(pregunta_06())


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
"
    """
    dictionary = {}
    tupla = [(int(cadena[2]), cadena[0]) for cadena in data]

    for clave, valor in tupla:
        if clave not in dictionary.keys():
            dictionary[clave] = [valor]
        else:
            dictionary[clave] += [valor]
    
    return sorted([(key,value) for key, value in dictionary.items()])
#print(pregunta_07())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    dictionary = {}
    tupla = [(int(cadena[2]), cadena[0]) for cadena in data]

    for clave, valor in tupla:
        if clave not in dictionary.keys():
            dictionary[clave] = [valor]
        else:
            dictionary[clave] += [valor]
    
    return sorted([(key,sorted(list(set(value)))) for key, value in dictionary.items()]) 


#print(pregunta_08())


def pregunta_09():

    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista = [cadena.split(";") for cadena in data]
    lista = [cadena[4].split(",") for cadena in lista]
    dictionary = {}
    for l in lista:
        for valores in l:
            if valores[0:3] not in dictionary.keys():
                dictionary[valores[0:3]] = 1
            else:
                dictionary[valores[0:3]] += 1

    return dict(sorted([(key,value) for key, value in dictionary.items()]))
#print(pregunta_09())




def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista = [cadena.split(";") for cadena in data]
    tupla = []
    for sentence in lista:
        sentence.remove(sentence[1]) 
        sentence.remove(sentence[1])
        tupla.append((sentence[0],len((sentence[1]).split(",")),len((sentence[2]).split(",")),))
    return tupla
#print(pregunta_10())



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    lista = [cadena.split(";") for cadena in data]

    dictionary = {}
    for sentence in lista:
        sentence.remove(sentence[0]) 
        sentence.remove(sentence[1])
        sentence.remove(sentence[2])

    for numero in lista:
        numero[0] = int(numero[0])

    for sentence in lista:
        for letra in sentence[1].split(","):
            if letra not in dictionary.keys():
                dictionary[letra] = sentence[0]
            else:
                dictionary[letra] += sentence[0]

    return dict(sorted(dictionary.items()))
#print(pregunta_11())


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    lista = [cadena.split(";") for cadena in data]

    dictionary = {}
    for sentence in lista:
        sentence.remove(sentence[1])
        sentence.remove(sentence[1])  
        sentence.remove(sentence[1])


    lista = [[elemento[0],elemento[1].split(",")] for elemento in lista]
    #lista = [[elemento[0]] + elemento[1] for elemento in lista]
    
    #lista_sin_tres_letras = [[fila[0], [dato[4:] for dato in fila[1]]] for fila in lista]
    dictionary = {}
    for fila in lista:
        for dato in fila[1]:
            if fila[0] in dictionary.keys():
                dictionary[fila[0]] += int(dato[4:])
            else:
                dictionary[fila[0]] = int(dato[4:])

            #lista2.append([fila[0], dato[4:]])


    return dict(sorted(dictionary.items()))
    
 
#print(pregunta_12())