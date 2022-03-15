from collections import namedtuple
import sys
from math import sqrt

def obtener_valores():

    Coeficientes = namedtuple('Coeficientes','a b c')

    try:

        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))

        cf = Coeficientes(a,b,c)

        return cf

    except ValueError:

        print('Los valores de "a" "b" y "c" deben ser numeros enteros')
        sys.exit(1)

def imprimir_ecuacion(cf):

    ecuacion = str()

    # Revisar valor de "a"
    if cf.a != 0:
        if cf.a == 1:
            ecuacion = 'x^2'
        elif cf.a == -1:
            ecuacion = '-x^2'
        else:
            ecuacion = str(cf.a) + 'x^2'

    # Revisar valor de "b"
    if cf.b != 0:
        if cf.b > 1:
            ecuacion = ecuacion + ' + ' + str(cf.b) + 'x'
        elif cf.b == 1:
            ecuacion = ecuacion + ' + x'
        elif cf.b == -1:
            ecuacion = ecuacion + ' - x'
        else:
            ecuacion = ecuacion + ' - ' + str(abs(cf.b)) + 'x'

    # Revisar valor de "c"
    if cf.c != 0:
        if cf.c > 1:
            ecuacion = ecuacion + ' + ' + str(cf.c) + ' = 0'
        else:
            ecuacion = ecuacion + ' - ' + str(abs(cf.c)) + ' = 0'

    # Imprimir ecuacion
    print(f'Calculando resultados para: {ecuacion}')

def evaluar(cf):

    divisor = 2 * cf.a
    discriminador = (cf.b * cf.b) - (4 * cf.a * cf.c)
    eval = False

    if divisor == 0:
        print('Valores INVALIDOS: Esta no es no es una ecuacion de segundo grado')

    elif discriminador < 0:
        print('Valores INVALIDOS: No se soportan resultados con numeros complejos')

    else:
        eval = True

    return eval

def calcular_resultado(cf):

    divisor = 2 * cf.a
    discriminador = (cf.b * cf.b) - (4 * cf.a * cf.c)

    x1 = (-cf.b + sqrt(discriminador)) / divisor
    x2 = (-cf.b - sqrt(discriminador)) / divisor

    if x1 == x2:
        print(f'Resultado: {x1}')
    else:
        print(f'Resultados: x1 = {x1} , x2 = {x2}')

if __name__ == '__main__':

    print('''
==============================================================
Programa que resuelve ecuaciones de segundo grado
Sigue la forma canonica para obtener los valores
de los coeficientes -- ax^2 + bx + c = 0 --
==============================================================
Escribe los valores de "a", "b" y "c" que corresponden
''')

    cf = obtener_valores()
    imprimir_ecuacion(cf)
    eval = evaluar(cf)
    if eval:
        calcular_resultado(cf)
