#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
        
    '''
    numero_1 = int(input("Ingrese el primer numero"))
    numero_2 = int(input("Infrese el segundo numero"))

    resta = numero_1 - numero_2
    if resta > 0:
      print("El resultado de restar el segundo numero al primero es positivo")
    elif resta < 0:
      print("El resultado de restar el segundo numero al primero es negativo")
    else:
      print("El resultado de restar el segundo numero al primero es cero")



def ej2():
# Ejercicios de práctica con números

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    
    '''

    numero_1 = int(input("Ingrese el primer numero: "))
    numero_2 = int(input("Ingrese el segundo numero: "))
    numero_3 = int(input("Ingrese el tercer numero: "))

    paridad_numero_1 = numero_1 % 2
    paridad_numero_2 = numero_2 % 2
    paridad_numero_3 = numero_3 % 2

    if paridad_numero_1 == 0:
        print("numero_1 es par")
    else:
        print("numero_1 es impar")
    if paridad_numero_2 == 0:
        print("numero_2 es par")
    else:
        print("numero_2 es impar")
    if paridad_numero_3 == 0:
        print("numero_3 es par")
    else:
        print("numero_3 es impar")


def ej3():
    # Ejercicios de práctica con números

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    

    '''

    numero_1 = int(input("Ingrese el primer numero: "))
    numero_2 = int(input("Ingrese el segundo numero: "))
    print("Ingrese que operacion desea realizar: ")
    print("Ingrese '1' para suma, '2' para resta, '3' para multiplicacion")
    print("'4' para division, '5' para potencia")

    operacion = int(input())

    if operacion == 1:
        suma = numero_1 + numero_2
        print("La suma es: ", suma)
    elif operacion == 2:
        resta = numero_1 - numero_2
        print("La resta es: ", resta)
    elif operacion == 3:
        multiplicacion = numero_1 * numero_2
        print("La multiplicacion es:", multiplicacion)
    elif operacion == 4:
        division = numero_1 / numero_2
        print("La division es:", division)
    elif operacion == 5:
        potencia = numero_1 ** numero_2
        print("La potencia es:", potencia)

    # Otra opcion ingresando letras y no numeros para las opciones

    numero_1 = int(input("Ingrese el primer numero: "))
    numero_2 = int(input("Ingrese el segundo numero: "))
    print("Ingrese que operacion desea realizar: ")
    print("Ingrese 's' para suma, 'r' para resta, 'm' para multiplicacion")
    print("'d' para division, 'p' para potencia")

    operacion = str(input())

    if operacion == 's':
        suma = numero_1 + numero_2
        print("La suma es: ", suma)
    elif operacion == 'r':
        resta = numero_1 - numero_2
        print("La resta es: ", resta)
    elif operacion == 'm':
        multiplicacion = numero_1 * numero_2
        print("La multiplicacion es:", multiplicacion)
    elif operacion == 'd':
        division = numero_1 / numero_2
        print("La division es:", division)
    elif operacion == 'p':
        potencia = numero_1 ** numero_2
        print("La potencia es:", potencia)


def ej4():
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor

    '''
    texto_1 = str(input("Ingrese la primera palabra\n"))
    texto_2 = str(input("Ingrese la segunda palabra\n"))
    texto_3 = str(input("Ingrese la tercer y ultima palabra\n"))
    print("Como quiere ordenar las palabras?")
    print("Ingrese '1' para ordenarlas alfabeticamente, si no,")
    print("ingrese '2' para ordenarlas por canttidad de letras")

    elegir = int(input())
        # Aqui se calcula la palabra mas corta y su valor determina el bucle
    long_texto_1 = len(texto_1)
    long_texto_2 = len(texto_2)
    long_texto_3 = len(texto_3)
    '''
    
    if (long_texto_1 > long_texto_2):
            longitud = long_texto_2
    else:
        longitud = long_texto_1
        if (longitud > long_texto_3):
            longitud = long_texto_3
        else:
            longitud = longitud
            print("")

    '''

    if elegir == 1:
        contador_1 = 0
        texto_alto = ""
        texto_medio = ""
        texto_bajo = ""
        letra_texto_1 = texto_1[0]
        letra_texto_2 = texto_2[0]
        letra_texto_3 = texto_3[0]

        if letra_texto_1 == letra_texto_2 and letra_texto_1 != letra_texto_3: 
            if long_texto_1 >= long_texto_2:
                longitud = long_texto_2
            else:
                longitud = long_texto_1
            if letra_texto_1 > letra_texto_3:
                texto_bajo = texto_3
            else:
                texto_alto = texto_3
        while contador_1 < longitud:
            contador_1 = 1
            letra_texto_1 = texto_1[contador_1]
            letra_texto_2 = texto_2[contador_1]
            contador_1 += 1
            if letra_texto_1 == letra_texto_2:
                return
            elif letra_texto_1 > letra_texto_2:
                if texto_bajo == "":
                    texto_medio = texto_1
                    texto_bajo = texto_2
                else:
                    texto_alto = texto_1
                    texto_medio = texto_2
            elif letra_texto_1 < letra_texto_2:
                if texto_bajo == "":
                    texto_medio = texto_2
                    texto_bajo = texto_1
                else:
                    texto_alto = texto_2
                    texto_medio = texto_1
            print(texto_alto, texto_medio, texto_bajo)
            # break

        else:

            if letra_texto_1 == letra_texto_3 and letra_texto_1 != letra_texto_2:
                if long_texto_1 >= long_texto_3:
                    longitud = long_texto_3
                else:
                    longitud = long_texto_1
                if letra_texto_1 > letra_texto_2:
                    texto_bajo = texto_2
                else:
                        texto_alto = texto_2
                contador_2 = 1
            while contador_2 < longitud:
                letra_texto_1 = texto_1[contador_2]
                letra_texto_3 = texto_3[contador_2]
                contador_2 += 1
                if letra_texto_1 == letra_texto_3:
                    return
                elif letra_texto_1 > letra_texto_3:
                    if texto_alto == "":
                        texto_alto = texto_1
                        texto_medio = texto_3
                    else:
                        texto_medio = texto_1
                        texto_bajo = texto_3
                elif letra_texto_1 < letra_texto_3:
                    if texto_alto == "":
                        texto_alto = texto_3
                        texto_medio = texto_1
                    else:
                        texto_medio = texto_3
                        texto_bajo = texto_1
                print(texto_alto, texto_medio, texto_bajo)
                break
            else:    

                if letra_texto_2 == letra_texto_3 and letra_texto_2 != letra_texto_1:
                    if long_texto_2 >= long_texto_3:
                        longitud = long_texto_3
                    else:
                        longitud = long_texto_2
                    if letra_texto_2 > letra_texto_1:
                        texto_bajo = texto_1
                    else:
                        texto_alto = texto_1
                    contador_3 = 1
                while contador_3 < longitud:
                    letra_texto_2 = texto_2[contador_3]
                    letra_texto_3 = texto_3[contador_3]
                    contador_3 += 1
                    if letra_texto_2 == letra_texto_3:
                        return
                    elif letra_texto_2 > letra_texto_3:
                        if texto_alto == "":
                            texto_alto = texto_2
                            texto_medio = texto_3
                        else:
                            texto_medio = texto_2
                            texto_bajo = texto_3
                    elif letra_texto_2 < letra_texto_3:
                        if texto_alto == "":
                            texto_alto = texto_3
                            texto_medio = texto_2
                        else:
                            texto_medio = texto_3
                            texto_bajo = texto_2 
                    print(texto_alto, texto_medio, texto_bajo)
                    break
                else:

                    if letra_texto_1 != letra_texto_2 != letra_texto_3:


                        if (letra_texto_1 > letra_texto_2 and letra_texto_1 > letra_texto_3
                            and letra_texto_2 > letra_texto_3):
                            texto_alto = texto_1
                            texto_medio = texto_2
                            texto_bajo = texto_3
                        elif (letra_texto_1 > letra_texto_2 and letra_texto_1 > letra_texto_3
                            and letra_texto_2 < letra_texto_3):
                            texto_alto = texto_1
                            texto_medio = texto_3
                            texto_bajo = texto_2
                        elif (letra_texto_1 < letra_texto_2 and letra_texto_1 > letra_texto_3
                            and letra_texto_2 > letra_texto_3):
                            texto_alto = texto_2
                            texto_medio = texto_1
                            texto_bajo = texto_3
                        elif (letra_texto_1 < letra_texto_2 and letra_texto_1 < letra_texto_3
                            and letra_texto_2 > letra_texto_3):
                            texto_alto = texto_2
                            texto_medio = texto_3
                            texto_bajo = texto_1
                        elif (letra_texto_1 > letra_texto_2 and letra_texto_1 < letra_texto_3
                            and letra_texto_2 < letra_texto_3):
                            texto_alto = texto_3
                            texto_medio = texto_1
                            texto_bajo = texto_2
                        elif (letra_texto_1 < letra_texto_2 and letra_texto_1 < letra_texto_3
                            and letra_texto_2 < letra_texto_3):
                            texto_alto = texto_3
                            texto_medio = texto_2
                            texto_bajo = texto_1
                    print(texto_alto, texto_medio, texto_bajo)
                    print("")
                    
    '''
    if elegir == 2:
        if (long_texto_1 > long_texto_2):
            longitud_2 = long_texto_2

        else:
            longitud_1 = long_texto_1
            if (longitud > long_texto_3):
                longitud = long_texto_3
            else:
                longitud = longitud
                print("")
    '''




def ej5():
    # Ejercicios de práctica con números
       
    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado  

    '''

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    #ej5()
