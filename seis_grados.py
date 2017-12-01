import collections
import heapq
from grafo import Grafo
import random
CONST_CANT_CAMINOS=1000
CONST_LARGO_CAM=100


def grafo_crear(nombre_archivo):
    """
    Crea un grafo de conexiones de actores a partir de un archivo de datos.

    PRE: Recibe el nombre de un archivo separado por comas que contenga de lineas:
        actor,pelicula,pelicula,pelicula
        que equivalen a: vertice,arista,arista,arista
    POST: Devuelve un grafo creado a partir de estos datos.
    """
    grafo=Grafo()
    with open(nombre_archivo) as archivo:#Mas adelante habra que ver como manejar esto
                                        #por lo del tema de que no entra en memoria...
        peliculas={}
        for linea in archivo:
            informacion=(linea.rstrip('\n')).split(',')
            grafo.agregar_vertice(informacion[0])
            for pelicula in informacion[1:]:
                lista=peliculas.get(pelicula,[])
                if not lista:
                    peliculas[pelicula]=lista
                lista.append(informacion[0])
    for pelicula,actores in peliculas.items():
        for i in range(len(actores)):
            for j in range(i+1,len(actores)):
                grafo.agregar_arista(actores[i],actores[j],pelicula)
                #Es horrible el orden de esto pero no se me ocurrio nada mejor...
                #Habra que ver otra forma de cambiarlo...
    return grafo


def camino(grafo, origen, llegada):
    """
    Devuelve el camino entre un actor de origen y uno de llegada.

    PRE: Recibe el grafo, un actor de origen y un actor de llegada.
    POST: Devuelve una lista ordenada de cadenas (películas) para llegar desde
        el origen hasta el final.
    """
    visitados={}
    padre={}
    resultado=[]
    cola=collections.deque()
    cola.append(origen)
    padre[origen]=None
    visitados[origen]=True
    visitados[llegada]=False
    while len(cola) and not visitados[llegada]:
        v=cola.popleft()
        for w in grafo.obtener_adyacentes(v):
            if not visitados.get(w,False):
                visitados[w]=True
                padre[w]=v
                if w==llegada:
                    break
                cola.append(w)
    actual=llegada
    while actual and visitados[llegada] and padre[actual]:
        aristas=grafo.obtener_arista(actual,padre[actual])
        resultado.append(aristas[0])
        actual=padre[actual]
    return resultado[::-1]



def actores_a_distancia(grafo, origen, n):
    """
    Devuelve los actores a distancia n del recibido.

    PRE: Recibe el grafo, el actor de origen y el número deseado.
    POST: Devuelve la lista de cadenas (actores) a n pasos del recibido.
    """
    resultado=[]
    visitados={}
    orden={}
    visitados[origen]=True
    orden[origen]=0
    cola=collections.deque()
    cola.append(origen)
    while len(cola):
        v=cola.popleft()
        if orden[v]==n:
            break
        for w in grafo.obtener_adyacentes(v):
            if not visitados.get(w,False):
                visitados[w]=True
                orden[w]=orden[v]+1
                cola.append(w)
                if orden[w]==n:
                    resultado.append(w)
    return resultado


def popularidad(grafo, actor):
    """
    Calcula la popularidad del actor recibido.

    PRE: Recibe el grafo y un actor de origen
    POST: Devuelve un entero que simboliza la popularidad: todos los adyacentes
        de los adyacentes del actor, multiplicado por su cantidad de peliculas
    """
    cant_actores=len(actores_a_distancia(grafo,actor,2))
    peliculas={}
    cant_peliculas=0
    for arista in grafo.obtener_aristas_v(actor):
        pelicula=arista[1]
        if not peliculas.get(pelicula,False):
            cant_peliculas +=1
            peliculas[pelicula]=True
    return cant_actores*cant_peliculas

def similares(grafo,origen, n):
    """
    Calcula los n actores más similares al actor de origen y los devuelve en una
    lista ordenada de mayor similitud a menor.

    PRE: Recibe el grafo, el actor de origen, y el n deseado
    POST: Devuelve una lista de los n actores no adyacentes más similares al
        pedido. La lista no debe contener al actor de origen.
    """
    vertices=grafo.obtener_vertices()
    if not vertices:
        raise ValueError('El grafo esta vacio')
    contador_v={}
    resultado=[]
    for i in range(CONST_CANT_CAMINOS):
        v=random.choice(vertices)
        recorrido=0
        _similares_visitar(grafo,contador_v,CONST_LARGO_CAM,recorrido,v)
    heap_min=[]
    actores=list(contador_v.items())
    cant_actores=len(actores)
    for i in range(n):
        actual=actores[i]
        heapq.heappush(heap_min,actual[::-1])#Invierto las posiciones de la tupla para que el heap compare las cantidades
    for i in range(n,cant_actores):
        actual=actores[i]
        if (actual[1]>heap_min[0][0]):
            heapq.heappushpop(heap_min,actual[::-1])
    for i in range(n):
        resultado.append((heapq.heappop(heap_min))[1])
    return resultado[::-1]

def _similares_visitar(grafo,contador_v,largo_cam,recorrido,origen):
    '''Funcion recursiva que recorre un camino del largo_cam de forma aleatoria
    y aumenta en 1 al contador de cada vertice que visita.'''
    if recorrido==largo_cam:
        return True
    cant=contador_v.get(origen,0)
    cant +=1
    contador_v[origen]=cant
    recorrido +=1
    adyacentes=grafo.obtener_adyacentes(origen)
    random.shuffle(adyacentes)
    for w in adyacentes:
        if(_similares_visitar(grafo,contador_v,largo_cam,recorrido,w)):
            return True
    return False
