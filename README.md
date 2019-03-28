

# QCLIBGSMM

Librería de computación cuántica desarrollada por simón marín para el curso ciencias naturales y tecnologia, en el 2019-1

## Getting Started
Para que el programa funcione, guarde el archivo en la misma carpeta donde se ejecute su programa, para importarlo necesita hacerlo de la siguiente manera:
```
import complejo
```

### Prerequisites

Tener una version de python igual o superior a la 3.6.1
Tener Instalada alguna version de Numpy
### Examples


Importar
```
import complejo

```
##Probando algunas funcionalidades de nuestra libreria

Input
```
m5 = [[(3,2),(5,-1),(0,2)],[(0,0),(12,0),(6,-3)],[(2,0),(4,4),(9,3)]]
m6 = [[(1,0),(3,4),(5,-7)],[(10,2),(6,0),(2,5)],[(0,0),(1,0),(2,9)]]
complejo.productoTensor(m5,m6)

```

Output

```
[[(3.0, 2.0), (1.0, 18.0), (29.0, -11.0), (5.0, -1.0), (19.0, 17.0), (18.0, -40.0), (0.0, 2.0), (-8.0, 6.0), (14.0, 10.0)], [(26.0, 26.0), (18.0, 12.0), (-4.0, 19.0), (52.0, 0.0), (30.0, -6.0), (15.0, 23.0), (-4.0, 20.0), (0.0, 12.0), (-10.0, 4.0)], [(0.0, 0.0), (3.0, 2.0), (-12.0, 31.0), (0.0, 0.0), (5.0, -1.0), (19.0, 43.0), (0.0, 0.0), (0.0, 2.0), (-18.0, 4.0)], [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (12.0, 0.0), (36.0, 48.0), (60.0, -84.0), (6.0, -3.0), (30.0, 15.0), (9.0, -57.0)], [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (120.0, 24.0), (72.0, 0.0), (24.0, 60.0), (66.0, -18.0), (36.0, -18.0), (27.0, 24.0)], [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (12.0, 0.0), (24.0, 108.0), (0.0, 0.0), (6.0, -3.0), (39.0, 48.0)], [(2.0, 0.0), (6.0, 8.0), (10.0, -14.0), (4.0, 4.0), (-4.0, 28.0), (48.0, -8.0), (9.0, 3.0), (15.0, 45.0), (66.0, -48.0)], [(20.0, 4.0), (12.0, 0.0), (4.0, 10.0), (32.0, 48.0), (24.0, 24.0), (-12.0, 28.0), (84.0, 48.0), (54.0, 18.0), (3.0, 51.0)], [(0.0, 0.0), (2.0, 0.0), (4.0, 18.0), (0.0, 0.0), (4.0, 4.0), (-28.0, 44.0), (0.0, 0.0), (9.0, 3.0), (-9.0, 87.0)]]
```
##superPosition
Entra como parametro un vector y un numero n, retornamos la probabilidad de que nuestra particula
se encuentre en la posicion n.

Input

```        
v = [(-3,-1),(0,-2),(0,1),(2,0)]
complejo.superPosition(v,2)
```        
Output

```
0.052629

```     
##amplitudeOfTransition
La función recibe como parametro 2 escalares y 2 vectores, la función nos retorna
nos retorna un numero complejo que representa la amplitud de transición de un vector v1
a un vector v2

Input
``` 
a = [(0,(2)**0.5/2),(-(2)**0.5/2,0)]
b = [((2)**0.5/2,0),(0,(2)**0.5/2)]
complejo.amplitudeOfTransition(a,b)
``` 
Output
``` 
(0.0, -1.0000000000000002)
``` 


##varianza
Esta funcion calcula la varianza dada una matriz de estado y su correspondiente vector ket
retorna un numero complejo

Input
``` 
observador = [[(1,0),(0,-1)],[(0,1),(2,0)]]
ket = [((2)**0.5/2,0),(0,(2)**0.5/2)]
complejo.varianza(observador,ket)
``` 
Output
``` 
2.2500000000000013
``` 



## Authors

* **Simón Marín** (https://github.com/Simono2000)

