#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para poner a prueba los conocimientos adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica numérica
    
    # Comparadores
    # Ingrese dos números cualesquiera y realice las siguientes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))
    
    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda
    if numero_1 > numero_2:
        print("numero_1 es mayor que numero_2")
    else: 
        print("numero_1 es menor que numero_2")

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso
    if numero_1 > 0:
        print ("numro_1 es positivo")
    elif numero_1 < 0:
        print("numero_1 es negativo")
    else:
        print("numero_1 es '0'")


    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición
    if (numero_1 > 0 and numero_1 < 100):
        print("numero_1 cumple con la condicion ya que estan entre los parametros establecidos")
    else:
        print("numero_1 no cumple la condición ya que no estan entre los parametros establecidos")

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición
    if (numero_1 < 10 or numero_2 > -2):
        print("Se cumple la condicion al cumplirse en uno de los casos")
    else:
        print("Ni el numero_1 es menor a 10 ni numero_2 es mayor a -2")

def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    if texto_1 > texto_2:
        print("texto_1 es mayor que texto_2")
    elif texto_1 < texto_2:
        print("texto_1 es menor que texto_2")
    else:
        print("texto_1 y texto_2 son iguales")

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    largo_texto_1 = len(texto_1)
    largo_texto_2 = len(texto_2)
    if largo_texto_1 > largo_texto_2:
        print("texto_1 tiene mas cantidad de letras")
    elif largo_texto_1 < largo_texto_2:
        print("texto_2 tiene mas cantidad de letras")
    else:
        print("texto_1 y texto_2 tienen la misma cantidad de letras")


    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
    letra_texto_1 = texto_1[0]
    letra_texto_2 = texto_2[0]
    if letra_texto_1 > letra_texto_2:
        print("La primer letra de texto_1 es mayor que la primer letra de texto_2")
    elif letra_texto_1 < letra_texto_2:
        print("La primer letra de texto_1 es menor que la primer letra de texto_2")
    else:
        print("La primer letra de texto_1 es igual que la primer letra de texto_2")

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    if copia_texto_1 == texto_1:
        print("copia_texto_1 y texto_1 son iguales")
    else:
        print("copia_texto_1 y texto_1 son diferentes")

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
    if copia_texto_1 != texto_1:
        print("copia_texto_1 es diferente a texto_1")
    else:
        print("copia_texto_1 es igual a texto_1")

def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5) 
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"
    if numero_1 > 5:
        if numero_2 > 0:
            print("Resp=1")   # numero_2 es positivo
        elif numero_2 < 0:
            print("Resp=2")   # numero_2 es negativo
        else:
            print("numero_2 no es ni positivo ni negativo")
    elif numero_2 > 5:
        print("Resp=3")   # numero_2 es mayor que 5
    else:
        print("Resp=4")   # numero_2 no es mayor que 5


       

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor o igual a 90 --> imprimir A
    # Si el puntaje es mayor o igual a 80 --> imprimir B
    # Si el puntaje es mayor o igual a 70 --> imprimir C
    # Si el puntaje es mayor o igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados
    if puntaje >= 90:
        print("A")
    elif puntaje >= 80:   # "and puntaje < 90:"  esta parte de la sentencia no es necesaria
        print("B")        # aunque no modifica el resultado. Termina siendo redundante.
    elif puntaje >= 70 and puntaje < 80:
        print("C")
    elif puntaje >= 60 and puntaje < 70:
        print("D")
    elif puntaje > 0 and puntaje < 60:    
        print("F")
    # otra opcion de estructurar el anidado
    if puntaje >= 90:
        print("A")
    else:
        if  puntaje >= 80 and puntaje < 90:
            print("B")
        else:
            if puntaje >= 70 and puntaje < 80:
                print("C")
            else:
                if puntaje >= 60 and puntaje < 70:
                    print("D")
                else:
                    if puntaje > 0 and puntaje < 60:
                        print("F")




def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual  de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    if texto_1 > texto_2:
        print("texto_1 es mayor alfabeticamente")
    else:
        print("texto_2 es mayor alfabeticamente")

    num_texto_1 = int(texto_1)
    num_texto_2 = int(texto_2)
    if num_texto_1 > num_texto_2:
        print("num_texto_1 es mayor que num_texto_2")
    else:
        print("num_texto_2 es mayor que num_texto_1")


    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()

     # Mi analisis:
     #     estimo que en ambos casos se mantiene desigualdad porque en texto
     #     el numero 7 (siete) empieza con una letra de mayor valor que 5 (cinco)