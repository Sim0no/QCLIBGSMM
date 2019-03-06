from math import atan as arco_tangente,pi,sin,cos
##Germán Simón Marín Mejía
##CNYT GRUPO 1, 2019-1

def suma(tupla1,tupla2):
    '''Retorna la suma de 2 numeros complejos, el primer elemento de cada
        tupla representa la parte real del numero,el otro elemento representa
        la parte imaginaria.
        (a1,b1i)+(a2,b2i) ----->(a1+a2,(b1+b2)i) '''
    a1,b1,a2,b2 = tupla1[0],tupla1[1],tupla2[0],tupla2[1]
    return (float(a1+a2),float(b1+b2))


def resta(tupla1,tupla2):
    '''Retorna la resta de 2 numeros complejos, el primer elemento de cada
        tupla representa la parte real del numero,el otro elemento representa
        la parte imaginaria.
        (a1,b1i)-(a2,b2i) ----->(a1-a2,(b1-b2)i) '''
    a1,b1,a2,b2 = tupla1[0],tupla1[1],tupla2[0],tupla2[1]
    return (float(a1-a2),float(b1-b2))


def multiplicacion(tupla1,tupla2):
    '''Retorna la multiplicación de 2 numeros complejos, el primer elemento de cada
        tupla representa la parte real del numero,el otro elemento representa
        la parte imaginaria.
        (a1,b1i)*(a2,b2i) ----->(a1*a2-b1*b2,(a1*b2+a2*b1)i)'''
    a1,b1,a2,b2 = tupla1[0],tupla1[1],tupla2[0],tupla2[1]
    return (float((a1*a2)-(b1*b2)),float((a1*b2)+(a2*b1)))
def division(tupla1,tupla2):
    try:
        '''Retorna la division de 2 numeros complejos, el primer elemento de cada
            tupla representa la parte real del numero,el otro elemento representa
            la parte imaginaria.
            (a1,b1i)/(a2,b2i) ----->((a1*a2+b1*b2)/((a2)**2+(b2)**2),((a2*b1)-(a1*b2))/((a2)**2+(b2**2)))'''
        a1,b1,a2,b2 = tupla1[0],tupla1[1],tupla2[0],tupla2[1]
        return (round((a1*a2+b1*b2)/((a2)**2+(b2)**2),3),round(((a2*b1)-(a1*b2))/((a2)**2+(b2)**2),3))
    except ZeroDivisionError:print('La division entre estos 2 numeros no esta definida.')
        
        
def modulo(tupla):
    '''Retorna el modulo de un numero complejo, el primer elemento de la
            tupla representa la parte real del numero,el otro elemento representa
            la parte imaginaria.
            |tupla| = |a + bi| -------> ((a)**2+(b)**2)**0.5'''
    a,b = tupla[0],tupla[1]
    return ((a)**2+(b)**2)**0.5


def conjugado(tupla):
    '''Retorna el conjugado de un numero complejo, el primer elemento de la
            tupla representa la parte real del numero,el otro elemento representa
            la parte imaginaria.
            conjugado(a + bi) -----> a - bi'''
    a,b = tupla[0],tupla[1]
    return (float(a),float(b*-1))


def polar(tupla):
    '''Convierte un numero complejo de su forma binomica/cartesiana a polar,el primer elemento
        de la tupla representa la parte real del numero,el otro elemento representa
        la parte imaginaria. Retorna una tupla donde el primer elemento es la
        magnitud y el segundo la fase/direccion en radianes.'''
    a,b = tupla[0],tupla[1]
    z = modulo(tupla)
    angulo = arco_tangente(b/a)
    return (round(z,3),round(angulo,3))


def cartesiano(tupla):
    '''Convierte un numero complejo de su forma polar a binomica/cartesiana,el primer elemento
        de la tupla representa la magnitud,el otro elemento representa
        la fase/direccion en radianes. Retorna una tupla donde el primer elemento es la
        parte real del numnero, el otro elemento representa la parte imaginaria.'''
    magnitud,angulo = tupla[0],tupla[1]
    a = magnitud*cos(angulo)
    b = magnitud*sin(angulo)
    return (round(a,3),round(b,3))


def fase(tupla):
    '''Retorna la fase/direccion (en radianes) de un numero complejo.'''
    a,b = tupla[0],tupla[1]
    angulo = arco_tangente(b/a)
    return (round(angulo,3))


def polarGrados(tupla):
    '''Convierte un numero complejo de su forma binomica/cartesiana a polar,el primer elemento
        de la tupla representa la parte real del numero,el otro elemento representa
        la parte imaginaria. Retorna una tupla donde el primer elemento es la
        magnitud y el segundo la fase/direccion en grados.'''
    a,b = tupla[0],tupla[1]
    z = modulo(tupla)
    arco = arco_tangente(b/a)
    arco = (arco*180)/pi
    if a == 0 and b == 0: angulo = 0
    elif b == 0 and a > 0: angulo = 0
    elif b == 0 and a < 0: angulo = 180
    elif a == 0 and b > 0: angulo = 90
    elif a == 0 and b < 0: angulo = 270
    elif a > 0 and b >0:angulo = arco
    elif a < 0 and b < 0: angulo = 180 + arco
    elif a < 0: angulo = 180 + arco
    elif b < 0: angulo = 360 + arco
    return (round(z,3),round(angulo,3))


def cartesianoGrados(tupla):
    '''Convierte un numero complejo de su forma polar a binomica/cartesiana,el primer elemento
        de la tupla representa la magnitud,el otro elemento representa
        la fase/direccion en grados. Retorna una tupla donde el primer elemento es la
        parte real del numnero, el otro elemento representa la parte imaginaria.'''
    magnitud,angulo = tupla[0],tupla[1]
    angulo = (angulo*pi)/180
    a = magnitud*cos(angulo)
    b = magnitud*sin(angulo)
    return (round(a,3),round(b,3))

##############VECTORES Y MATRICES

def sumaVectores(vector1,vector2):
    '''Se ingresa cada vector como [],
    cada componente de el vector es una tupla que contiene
    parte real y parte imaginaria, retorna la suma de los 2
    vectores complejos.'''
    if len(vector1) != len(vector2):
        return 'La suma entre estos 2 vecotres no esta definida'
    aux = []
    for i in range(len(vector1)):
        aux.append(suma(vector1[i],vector2[i]))
    return aux     


def restaVectores(vector1,vector2):
    '''Se ingresa cada vector como [],
    cada componente de el vector es una tupla que contiene
    parte real y parte imaginaria, retorna la resta de
    los 2 vecotres complejos'''
    if len(vector1) != len(vector2): raise 'La suma entre estos 2 vecotres no esta definida'
    aux = []
    for i in range(len(vector1)):
        aux.append(resta(vector1[i],vector2[i]))
    return aux


def multiplicacionVectorEscalar(vector,escalar):
    '''Se ingresa el vector como [],y el escalar conmplejo
    como tupla,cada componente de el vector es una tupla que
    contiene parte real y parte imaginaria, retorna la multiplicación
    del vector complejo por e escalar complejo'''
    aux = []
    for i in range(len(vector)):
        aux.append(multiplicacion(vector[i],escalar))
    return aux


def sumaMatricesComplejas(matriz1,matriz2):
    '''Entran 2 matrices de M x N, retorna la suma de cada matriz
    compleja.'''
    if (len(matriz1) != len(matriz2)) or (len(matriz1[0]) != len(matriz2[0])):raise 'La suma entre estas 2 matrices no esta definida'
    aux = []
    for i in range(len(matriz1)):
        aux.append(sumaVectores(matriz1[i],matriz2[i]))
    return aux
    

def restaMatricesComplejas(matriz1,matriz2):
    '''Entran 2 matrices de M x N, retorna la resta de cada matriz
    compleja.'''
    if (len(matriz1) != len(matriz2)) or (len(matriz1[0]) != len(matriz2[0])):raise 'La suma entre estas 2 matrices no esta definida'
    aux = []
    for i in range(len(matriz1)):
        aux.append(restaVectores(matriz1[i],matriz2[i]))
    return aux


def multiplicacionMatrizEscalar(matriz,escalar):
    '''Se ingresa la matriz ,y el escalar conmplejo
    como tupla,cada componente de la matriz es un vector complejo, retorna la multiplicación
    de la matriz compleja por e escalar complejo'''
    aux = []
    for i in range(len(matriz)):
        aux.append(multiplicacionVectorEscalar(matriz[i],escalar))
    return aux[[(7,0),(6,5)],[(6,-5),(0,-3)]]


def matrizTranspuesta(matriz):
    '''Entra una matriz MxN, retorna su mtariz transpuesta asociada NxM'''
    aux = []
    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        aux.append(fila)
    return aux


def matrizConjugada(matriz):
    '''Entra una matriz , retorna su mtariz conjugada asociada '''
    aux = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[0])):
            fila.append(conjugado(matriz[i][j]))
        aux.append(fila)
    return aux


def matrizAdjunta(matriz):
    '''Entra una matriz, retorna la matriz adjunta asociada'''
    return matrizTranspuesta(matrizConjugada(matriz))


def multiplicacionMatrices(matriz1,matriz2):
    '''Entran 2 matrices, una de M x I, la otra de I X N, retorna
        la multiplicacion de lamatriz1 por la matriz 2 de dimension M X N'''
    if (len(matriz1[0]) != len(matriz2)): raise 'La multiplicación de matrices no está definida para estas matrices'
    aux = []
    for i in range(len(matriz1[0])):
        aux.append( [None] * len(matriz2))
    for i in range(len(matriz1[0])):
        for j in range(len(matriz2)):
            summ = (0,0)
            for k in range(len(matriz2[0])):
                summ = suma(multiplicacion(matriz1[k][i],matriz2[j][k]),summ)
            aux[i][j] = summ
    return aux



def productoInternoVectores(vector1,vector2):
    '''Se ingresan 2 vectores complejos de longitud n, retorna el producto interno entre estos'''
    if len(vector1) != len(vector2): raise 'Los vectores no tienen la misma longitud, su producto interno no esta definido'
    aux = (0,0)
    for i in range(len(vector1)): 
        aux = suma(aux,multiplicacion(vector1[i],vector2[i]))
    return aux;


def moduloVector(vector):
    '''Se ingresa un vector complejo, retorna el modulo del vector'''
    aux = (0,0)
    for i in vector:
        aux = suma(aux,(modulo(i),0))
    return round(aux[0],3)

def distanciaEntreVectores(vector1,vector2):
    '''Se ingresan 2 vectores complejos de longitud n, retorna la distancia entre estos'''
    if len(vector1) != len(vector2): raise 'Los vectores no tienen la misma longitud, su producto interno no esta definido'
    return moduloVector(restaVectores(vector1,vector2))

        
def esHermitiana(matriz):
    '''Entra una matriz cuadrada, Retorna verdadero  si la matriz es hermitiana(igual a su propia traspuesta conjugada)'''
    if len(matriz) != len(matriz[0]):  raise 'La matriz no es cuadrada'
    return matriz == matrizAdjunta(matriz)


def esUnitaria(matriz):
    '''Entra una matriz cuadrada, Retorna verdadero  si la matriz es unitaria'''
    if len(matriz) != len(matriz[0]):  raise 'La matriz no es cuadrada'
    i = [[(float(0),float(0)) for w in range(len(matriz))]for j in range(len(matriz))]
    for k in range(len(i)):
        i[k][k] = (float(1),float(0))
    return multiplicacionMatrices(matriz,matrizAdjunta(matriz)) == multiplicacionMatrices(matrizAdjunta(matriz),matriz) == i


def productoTensor(matriz1,matriz2):
    '''Entran 2 matrices, retorna el producto tensor entre estos'''
    aux = []
    subLista = []
    conta = len(matriz2)
    for i in matriz1:
        valorB = 0
        valorA = 0
        while valorA < conta:
            for num1 in i:
                for num2 in matriz2[valorB]:
                    subLista.append(multiplicacion(num1,num2))
            aux.append(subLista)
            subLista = []
            valorA +=1
            valorB += 1
    return aux



#######de lo clásico a lo cuántico

def marbels(matrizAdj, estadoInicial, clicks):
    '''Se simula el experimento de  las canicas despues de varios clicks'''
    while clicks > 0:
        clicks -= 1
        aux = []
        for i in range(len(matrizAdj)):
            sume = (0,0)
            for j in range(len(estadoInicial)):
               sume = suma(sume,multiplicacion(estadoInicial[j],matrizAdj[i][j]))
            aux.append(sume)
        estadoInicial  = aux
    return aux


def barras(matrizAdj, estadoInicial, clicks):
    '''Se simula el experimento de  barra con una cantidad de clicks'''
    while clicks > 0:
        clicks -= 1
        aux = []
        for i in range(len(matrizAdj)):
            sume = (0,0)
            for j in range(len(estadoInicial)):
               sume = suma(sume,multiplicacion(estadoInicial[j],matrizAdj[i][j]))
            aux.append(sume)
        estadoInicial  = aux
    return aux


def dobleRendija(matriz,clicks):
    '''Se realiza el esperimento de la doble rendija'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for x in range(clicks):
                matriz[i][j] = multiplicacion(matriz[i][j],matriz[i][j])
            matriz[i][j] = modulo(matriz[i][j])
    return matriz
