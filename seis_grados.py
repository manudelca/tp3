import collections
import heapq
from grafo import Grafo
import random
CONST_CANT_CAMINOS=100
CONST_PORCENT_VERT=10


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
    #En los random walks solo me importa el que esta al final del recorrido o cuento
    #a todos los del reorrido? Ahora esta programado para que cuente solo el del final
    vertices=grafo.obtener_vertices()
    if not vertices:
        raise ValueError('El grafo esta vacio')
    contador_v={}
    resultado=[]
    largo_cam=(grafo.vertices_total())*CONST_PORCENT_VERT//100
    for i in range(CONST_CANT_CAMINOS):#La cantidad de caminos siempre tendra que ser mayor a las similitudes pedidas...
        v=random.choice(vertices)
        recorrido=0
        visitados={}
        _similares_visitar(grafo,contador_v,largo_cam,recorrido,v,visitados)#Deberia controlar que no devuelva False? Que podria pasar?
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

def _similares_visitar(grafo,contador_v,largo_cam,recorrido,origen,visitados):
    '''Funcion recursiva que recorre un camino del largo_cam de forma aleatoria
    y cuando termina el aumenta en 1 al contador del vertice de llegada.'''
    if recorrido==largo_cam:
        cant=contador.get(origen,0)
        cant +=1
        contador[origen]=cant
        return True
    visitados[origen]=True
    recorrido +=1
    adyacentes=grafo.obtener_adyacentes(origen)
    if not adyacentes:
        return False
    while adyacentes:
        w=random.choice(adyacentes)
        adyacentes.remove(w)#Esto tiene pinta de muy poco optimo...
        if w not in visitados:#Deberia verificar que no haya sido visitado? Porque si lo hago no es 100% random...
            if(_similares_visitar(grafo,contador_v,largo_cam,recorrido,origen,visitados)):
                return True
    return False
