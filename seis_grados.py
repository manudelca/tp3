from grafo import Grafo


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
        for actor in actores:
            grafo.agregar_arista()
    #Podria ir agregando pero serian muchas iteraciones o no...?
    

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
            if not visitados[w]:
                visitados[w]=True
                padre[w]=v
                if w==llegada:
                    break
                cola.append(w)
    actual=llegada
    while actual:
        #No puedo implementar una primitiva que sea obtener_arista???
    #Hay que ver que onda cuando tengo mas de una componente conexa

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
    orden_actual=0
    orden[origen]=orden_actual
    cola=collections.deque()
    cola.append(origen)
    while len(cola) and orden_actual<n:
        v=cola.popleft()
        orden_actual +=1
        for w in grafo.obtener_adyacentes(v):
            if not visitados.get(w,False):
                visitados[w]=True
                orden[w]=orden_actual
                cola.append(w)
                if orden_actual==n:
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
    for pelicula in #Aca me conviene una primitiva que me devuelva todas las aristas de un vertice
                    #hay que esperar a ver que contesta el chabon...


def similares(grafo,origen, n):
    """
    Calcula los n actores más similares al actor de origen y los devuelve en una
    lista ordenada de mayor similitud a menor.

    PRE: Recibe el grafo, el actor de origen, y el n deseado
    POST: Devuelve una lista de los n actores no adyacentes más similares al
        pedido. La lista no debe contener al actor de origen.
    """
    raise NotImplementedError
