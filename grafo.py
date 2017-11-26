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
        '''Agrega el vertice recibido al grafo.'''
         if vertice not in self.dicc:
+            self.dicc[vertice]={}
+        #tendriamos que tirar una error en caso de else?

    def borrar_vertice(self,vertice):
        '''Borra el vertice del grafo. Levanta un error si no se encuentra'''
        if not vertice in self.dicc:
            raise ValueError('El vertice no se encuentra en el grafo')
        for adyacente in self.dicc[vertice]:
            (self.dicc[adyacente]).pop(vertice)

    def agregar_arista(self, v1, v2, info=None):
        '''Recibe los dos vertices a unir y la info adicional de la arista (None por defecto)
        y los une. Si los vertices no se encuentran en el grafo devuelve error.'''
        if not v1 in self.dicc or not v2 in self.dicc:
            raise ValueError('El o los vertices no se ecuentran')
        arista=_Arista(v1,v2,info)
        lista1=(self.dicc[v1]).get(v2,[])
        if not lista1:
            self.dicc[v1][v2]=lista1
        lista1.append(arista)
        lista2=(self.dicc[v2]).get(v1,[]):
        if not lista2:
            self.dicc[v2][v1]=lista2
        lista2.append(arista)

    def borrar_arista(self,v1,v2,info):
        '''Recibe dos vertices y elimina la arista entre ambos. Devuelve una tupla
        con una tupla representando una arista y la info de la arista ((v1,v2),info).
        Devuelve error en caso de no encontrarse'''
        if not v1 in self.dicc or not v2 in self.dicc:
            raise ValueError('El o los vertices no se ecuentran')
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
        if not v1 in self.dicc or not v2 in self.dicc:
            raise ValueError('El o los vertices no se ecuentran')
        return v2 in self.dicc[v1] and v1 in self.dicc[v2]

    def obtener_vertices(self):
        '''Devuelve una lista con los vertices del grafo'''
        return list(self.dicc)

    def obtener_aristas(self):
        '''Devuelve una lista con todas las aristas representadas como ((v1,v2),info)'''
        aristas={}
        for v in self.dicc:
            for adyacente in self.dicc[v]:
                lista_aristas=self.dicc[v][adyacente]
                for arista in lista_aristas:
                    arista_l=(arista.arista,arista.info)
                    if  not arista_l in aristas:
                        aristas[arista_l]=True
        return list(aristas)

    def obtener_arista(self,v1,v2):
        '''Recibe dos vertices y devuelve una lista con las aristas que los une.
        En caso de que no las haya, devuelve una lista vacia'''
        if not v1 in self.dicc or not v2 in self.dicc:
            raise ValueError('El o los vertices no se ecuentran')
        resultado=[]
        aristas=(self.dicc[v1]).get(v2,[])
        for arista in aristas:
            resultado.append((arista.arista,arista.info))
        return resultado

    def obtener_aristas_v(self,vertice):
        '''Recibe un vertice y devuelve una lista con todas las aristas
        conectadas al mismo.'''
        if not vertice in self.dicc:
            raise ValueError('El vertice no se encuentra en el grafo')
        resultado=[]
        for w,aristas in (self.dicc[vertice]).items():
            for arista in aristas:
                resultado.append((arista.arista,arista.info))
        return resultado
