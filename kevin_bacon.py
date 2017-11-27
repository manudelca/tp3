import seis_grados



#INICIO PARA CREAR GRAFO -> lo guarda en variable datos

while true:
  entrada = raw_input()
  entrada_procesada = entrada.rstrip('\n')).split(' ')
  if entrada_procesada[0] == 'camino_hasta_KB':
    camino_min(datos,'Bacon Kevin',entrada_procesada[1])
  elif entrada_procesada[0] == 'bacon_numer':
     raise NotImplementedError
  elif entrada_procesada[0] == 'bacon_number_mayor_a_6':
     raise NotImplementedError
  elif entrada_procesada[0] == 'bacon_number_infinito':
     raise NotImplementedError
  elif entrada_procesada[0] == 'KBN_promedio':
     raise NotImplementedError
  elif entrada_procesada[0] == 'similares_a_KB':
     raise NotImplementedError
  elif entrada_procesada[0] == 'popularidad_contra_KB':
     raise NotImplementedError
  elif entrada_procesada[0] == 'cantidad_peliculas':
     raise NotImplementedError
  elif entrada_procesada[0] == 'cantidad_actores':
     raise NotImplementedError
  else:
      break
      
    
    
    
    
def camino_min(datos,origen,llegada):
  camino = camino(datos,origen,llegada)
  for pelicula in camino:      #CREO QUE CAMINO ME DEVUELVE SÓLO LAS PELICULAS Y FALTARÍA EL ACTOR QUE CONECTA
     #IMPRIME 'DESTINO' ACTUÓ CON 'ORIGEN' EN 'PELICULA(AÑO)'
     #LO IDEAL SERIA UNA LISTA CON[['ACTOR DESTINO','ACTOR ORIGEN','PELICULA'],['ACTOR DESTINO','ACTOR ORIGEN','PELICULA']]
     print(pelicula[1]," actuó con ",pelicula[0]," en ",pelicula[2],".") 
  
