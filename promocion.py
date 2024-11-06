#crear un juego estilo preguntado

i = 0
res = 0
pregunta = str
respuesta = int
# opciones--------------------------------------------------------------------------------------------------------------------------


opcion = [""" 
            1 Es un bloque de pregunta
            2 Es un bloque de respuesta
            3 Es un loop
            4 Es un bloque de decision simple""",

"""
            1 repite el codigo un número definido de veces
            2 repite el codigo un número indefinido de veces
            3 guarda variables dentro de una lista
            4 para declarar variables""",

"""
            1 input/ouput
            2 int/float
            3 input/print
            4 prompt/document.write""",

"""
            1 / UNA
            2 / DOS
            3 / TRES
            4 / CUATRO""",

"""
            1 se agregan desde dentro del codigo
            2 se agregan desde la terminal
            3 son importados desde APIS
            4 1 y 2 son correctas""",

"""
            1 .upper()
            2 .lower()
            3 .capitalize()
            4 ninguna de las anteriores""",

"""
            1 Repite un bloque de código un número específico de veces 
            2 Repite un bloque de código mientras una condición sea verdadera 
            3 Repite un bloque de código sobre los elementos de una lista 
            4 Repite un bloque de código sobre los elementos de un diccionario""",

"""
            1 //
            2 # 
            3 !
            4 /*/""",

"""
            1 se utiliza para salir de un bucle
            2 se utiliza para comenzar un bucle
            3 sirve para cerrar el programa
            4 para abrir la terminal""",

"""
            1 Las listas pueden almacenar solo tipos de datos numéricos, mientras que las tuplas pueden almacenar cualquier tipo de datos
            2 las listas son inmodificables y las tuplas en cambio son modificables
            3 las listas son modificables y las tuplas son inmodificables
            4 Las listas se usan solo para datos ordenados, mientras que las tuplas se usan solo para datos no ordenados.""",
]
# preguntas ---------------------------------------------------------------------------------------------------------------------------

pregunta = ["""pregunta n°1
            ¿Qué es un condicional if en Python?""",
            """pregunta n°2
            ¿Qué hace un bucle while en Python?""",
            """pregunta n°3
            ¿Cómo se realizan operaciones de entrada salida en Python?""",
            """pregunta n°4
            ¿cuantos tipos de variables númericas tiene python?""",
            """pregunta n°5
            ¿Cómo se agregan elementos a una lista en Python?""",
            """pregunta n°6
            ¿que comando se utiliza para que todos los caracteres este en minuscula?""",
            """pregunta n°7
            ¿Qué es el bucle for en Python y qué función cumple?""",
            """pregunta n°8
            ¿con cual caracter se hacen comentarios en python?""",
            """pregunta n°9
            ¿para que sirve el comando break?""",
            """pregunta n°10
            ¿Cuál es la diferencia lista y una tupla?"""]
respuesta = [4,2,3,3,4,2,1,2,1,3]

#presentacion----------------------------------------------------------------------------------------------------------------------
print("""
                                       #########################
                                       #                       #
                                       #       BIENVENIDO      #
                                       #                       #
                                       #########################
                                """)
print("""las reglas del juego son sencillas, acertar una pregunta te da +1 punto y no acertar significa no sumar puntos,
      las preguntas son sobre el lenguaje de programacion python que es el que venimos viendo desde mitad de año.
                                              ¡suerte!""")


#for ------------------------------------------------------------------------------------------------------------------------------

for x in range (10):
    while res != 1 and res != 2 and res != 3 and res != 4:
        print(pregunta[x])
        print(opcion[x])
        res = int(input("ingrese un número del 1 al 4: "))
        if res == respuesta[x]:
            print("\033[32m¡respuesta correcta!\033[0m\n")
            i = i + 1
        elif res != respuesta[x] and res != 1 and res != 2 and res != 3 and res != 4:
            print("\033[33mIngrese solo valores de 1 al 4, intentelo de nuevo\033[0m\n")
        else:
            print("\033[31mrespuesta incorrecta\033[0m\n")
    res =0
if i >= 6:
    print("obtuviste",i,"respuestas correctas de 10")
    print("tu puntuacion fue de",i,"asi que estas aprobado")
else:
    print("obtuviste",i,"respuestas correctas de 10")
    print("tu puntuacion fue de",i,"asi que estas desaprobado")