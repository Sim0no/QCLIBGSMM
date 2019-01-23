from math import atan as arco_tangente,pi,sin,cos
##Germán Simón Marín Mejía
##CNYT GRUPO 1, 2019-1
def suma(tupla1,tupla2):
    '''Retorna la suma de 2 numeros complejos, el primer elemento de cada
        tupla representa la parte real del numero,el otro elemento representa
        la parte imaginaria.
        (a1,b1i)+(a2,b2i) ----->(a1+a2,(b1+b2)i) ''' 
    a1,b1,a2,b2 = tupla1[0],tupla1[1],tupla2[0],tupla2[1]
    return (a1+a2,b1+b2)
def resta(tupla1,tupla2):
    '''Retorna la resta de 2 numeros complejos, el primer elemento de cada
        tupla representa la parte real del numero,el otro elemento representa
        la parte imaginaria.
        (a1,b1i)-(a2,b2i) ----->(a1-a2,(b1-b2)i) '''
    a1,b1,a2,b2 = tupla1[0],tupla1[1],tupla2[0],tupla2[1]
    return (a1-a2,b1-b2)
def multiplicacion(tupla1,tupla2):
    '''Retorna la multiplicación de 2 numeros complejos, el primer elemento de cada
        tupla representa la parte real del numero,el otro elemento representa
        la parte imaginaria.
        (a1,b1i)*(a2,b2i) ----->(a1*a2-b1*b2,(a1*b2+a2*b1)i)'''
    a1,b1,a2,b2 = tupla1[0],tupla1[1],tupla2[0],tupla2[1]
    return ((a1*a2)-(b1*b2),(a1*b2)+(a2*b1))
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
    return (a,b*-1)
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

def polar_grados(tupla):
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
def cartesiano_grados(tupla):
    '''Convierte un numero complejo de su forma polar a binomica/cartesiana,el primer elemento
        de la tupla representa la magnitud,el otro elemento representa
        la fase/direccion en grados. Retorna una tupla donde el primer elemento es la
        parte real del numnero, el otro elemento representa la parte imaginaria.'''
    magnitud,angulo = tupla[0],tupla[1]
    angulo = (angulo*pi)/180
    a = magnitud*cos(angulo)
    b = magnitud*sin(angulo)
    return (round(a,3),round(b,3))



        
