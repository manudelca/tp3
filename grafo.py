import collections

class _Arista:
    '''Representacion de una arista de un grafo. Une dos vertices'''

    def __init__(self,v1,v2,info):
        '''Constructor de la arista. Recibe la info a guardar y los dos vertices
        a unir.'''
        self.arista=(v1,v2)
        self.info=info

class Grafo:
    '''Representacion de un grafo no dirigido. Las aristas no poseen peso. No admite
    vertices repetidos.'''

    def __init__(self):
        '''Constructor de un grafo'''
        self.dicc={}

    def agregar_vertice(self,vertice):
        '''Agrega el vertice recibido al grafo.'''#No se pueden repetir vertices???
        self.dicc[vertice]={}

    def borrar_vertice(self,vertice):
        '''Borra el vertice del grafo. Levanta un error si no se encuentra'''
        if not vertice in self.dicc:
            raise ValueError('El vertice no se encuentra en el grafo')#Que error levanto??
        for adyacente in self.dicc[vertice]:
            (self.dicc[adyacente]).pop(vertice)

    def agregar_arista(self, v1, v2, info=None):
        '''Recibe los dos vertices a unir y la info adicional de la arista (None por defecto)
        y los une. Si los vertices no se encuentran en el grafo devuelve error.'''
        if not v1 in self.dicc:
            raise ValueError('El vertice {} no se encuentra en el grafo'.format(v1))
        if not v2 in self.dicc:
            raise ValueError('El vertice {} no se encuentra en el grafo'.format(v2))
        arista=_Arista(v1,v2,info)
        lista1=(self.dicc[v1]).get(v2,[])
        lista1.append(arista)
        lista2=(self.dicc[v2]).get(v1,[])
        lista2.append(arista)

    def borrar_arista(self,v1,v2):
        '''Recibe dos vertices y elimina la arista entre ambos. Devuelve una tupla
        con una tupla representando una arista y la info de la arista ((v1,v2),info).
        Devuelve error en caso de no encontrarse'''
        if not v1 in self.dicc:
            raise ValueError('El vertice {} no se encuentra en el grafo'.format(v1))
        if not v2 in self.dicc:
            raise ValueError('El vertice {} no se encuentra en el grafo'.format(v2))
        arista=(self.dicc[v1]).get(v2,None)
        if not arista:
            raise ValueError('La arista no existe')
        (self.dicc[v1]).pop(v2)
        (self.dicc[v2]).pop(v1)
        return (arista.arista,arista.info)

    def obtener_adyacentes(self,vertice):
        '''Recibe un vertice y devuelve una lista con los adyacentes al mismo.
        Devuelve un error si no se encuentra el vertice en el grafo.'''
        if not vertice in self.dicc:
            raise ValueError('El vertice no se encuentra en el grafo')
        return list((self.dicc[vertice]))

    def es_adyacente(self,v1,v2):
        '''Recibe dos vertices y devuelve True en caso de que sean adyacentes.
        False en caso de que no. Devuelve un error en caso de no encontrarse el vertice.'''
        if not v1 in self.dicc:
            raise ValueError('El vertice no se encuentra en el grafo')
        if not v2 in self.dicc:
            raise ValueError('El vertice no se encuentra en el grafo')
        return v2 in self.dicc[v1]

    def obtener_vertices(self):
        '''Devuelve una lista con los vertices del grafo'''
        return list(self.dicc)

    def obtener_aristas(self):
        '''Devuelve una lista con todas las aristas representadas como ((v1,v2),info)'''
        aristas={}
        for v in self.dicc:
            for adyacente in self.dicc[v]:
                lista_aristas=self.dicc[v][adyacente]
                for elem in lista_aristas:
                    arista_l=(elem.arista,elem.info)
                    if  not arista_l in aristas:
                        aristas[arista_l]=True
        return list(aristas)

    def obtener_arista(self,v1,v2):
        '''Recibe dos vertices y devuelve una lista con las aristas que los une'''
        #Hay que controlar los errores
        resultado=[]
        for arista in self.dicc[v1][v2]:
            resultado.append(arista.arista,arista.info)
        return resultado

#def bfs(grafo,origen):
#    '''Recibe un grafo y un origen y recorre por capas el grafo. Devuelve un
#    diccionario con los padres de cada vertice y otro con el orden de cada vertice.'''
#    visitados={}
#    padre={}
#    orden={}
#    q=collections.deque()
#    q.append(origen)
#    visitados[origen]=True
#    orden[origen]=0
#    padre[origen]=None
#    while len(q):
#        v=q.popleft()
#        for w in grafo.obtener_adyacentes(v):
#            if not w in visitados:
#                visitados[w]=True
#                padre[w]=v
#                orden[w]=orden[v]+1
#                q.append(w)
#    return padre,orden

#def dfs(grafo,origen):
#    '''Recibe un grafo y un origen y recorre por profundidad el grafo. Devuelve
#    un diccionario con los padres de cada de vertice y otro con el orden de cada
#    vertice.'''
#    visitados={}
#    padre={}
#    orden={}
#    dfs_visitar(grafo,origen,visitados,padre,orden)
#    return padre,orden


#def dfs_visitar(grafo,v,visitados,padre,orden):
#    '''Funcion recursiva de dfs'''
#    visitados[v]=True
#    for w in grafo.obtener_adyacentes(v):
#        if w not in visitados:
#            padre[w]=v
#            orden[v]=orden.get(v,0)+1
#            dfs_visitar(grafo,w,visitados,padre,orden)
