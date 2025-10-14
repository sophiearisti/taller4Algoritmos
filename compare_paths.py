## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import sys
from MeshViewer import *
import heapq
import math

'''

'''
def distance( a, b ):
   return sum( [ ( a[ i ] - b[ i ] ) ** 2 for i in range( len( a ) ) ] ) ** 0.5
# end def

'''
Esta hace el proceso de encontrar por el metodo de dijkstra (aunque se parece un poco a prim)
obtener el mejor camino segun cruscal basado en la cantida de vecinos
'''
def DijkstraShortest( G, start, end ):
   # Obtener vertices y aristas
    V, A = G
    
    #numero de vertices
    n = len(V)
    
    #no marcados para cada vertice iniciamos sin marcar
    M = [ False for i in range( n ) ]
    
    # este es el vecto a retornar
    VStar = [ -1 for i in range( n ) ]
    
    #cola de prioridad
    colaPrioridad = [(0, start, start)] # (costo, vertice)

    encontrado = False
    while len(colaPrioridad) > 0 and not encontrado:
      (costo, inicio, anterior) = heapq.heappop(colaPrioridad)
      
      #esta es la bandera para terminar el proceso
      if inicio == end:
        encontrado = True

      if not M[ inicio ]:
        M[ inicio ] = True
        VStar[ inicio ] = anterior
        
        #obtener el ultimo elemento de V y anadirle el peso de distancia
        vecinos =  A[inicio]

        for vecino in vecinos:
          #calcular la distancia entre el ultimo elemento de V y el vecino
          dist = distance(V[inicio], V[vecino])

          heapq.heappush(colaPrioridad, (costo + 1, vecino, inicio))
        # end for
      # end if
    # end while
    
    if not encontrado:
      print("No se encontró camino de", start, "a", end)
      return []
    #end if

    return backtrack(VStar, start, end)
# end def

'''
Esta hace el proceso de encontrar por el metodo de dijkstra (aunque se parece un poco a prim)
obtener el mejor camino segun cruscal basado en la distancia
'''
def DijkstraCheapest( G, start, end ):
    
   # Obtener vertices y aristas
    V, A = G
    
    #numero de vertices
    n = len(V)
    
    #no marcados para cada vertice iniciamos sin marcar
    M = [ False for i in range( n ) ]
    
    # este es el vecto a retornar
    VStar = [ -1 for i in range( n ) ]
    
    #cola de prioridad
    colaPrioridad = [(0, start, start)] # (costo, vertice)

    encontrado = False
    while len(colaPrioridad) > 0 and not encontrado:
      (costo, inicio, anterior) = heapq.heappop(colaPrioridad)
      
      #esta es la bandera para terminar el proceso
      if inicio == end:
        encontrado = True

      if not M[ inicio ]:
        M[ inicio ] = True
        VStar[ inicio ] = anterior
        
        #obtener el ultimo elemento de V y anadirle el peso de distancia
        vecinos =  A[inicio]

        for vecino in vecinos:
          #calcular la distancia entre el ultimo elemento de V y el vecino
          dist = distance(V[inicio], V[vecino])

          heapq.heappush(colaPrioridad, (costo + dist, vecino, inicio))
        # end for
      # end if
    # end while
    
    if not encontrado:
      print("No se encontró camino de", start, "a", end)
      return []
    #end if

    return backtrack(VStar, start, end)
#end def

'''
Esta hace el proceso de encontrar por el metodo de kruskal (aunque se parece un poco a prim)
obtener el mejor camino segun cruscal basado en la cantidad de vecinos
'''
def KruskalShortest(G, start, end):
    # Obtener vertices y aristas
    V, A = G

    #numero de vertices
    n = len(V)
    
    #no marcados para cada vertice iniciamos sin marcar
    M = [ False for i in range( n ) ]
    
    # este es el vecto a retornar
    VStar = [ -1 for i in range( n ) ]

    #cola de prioridad
    colaPrioridad = [(0, start, start)] # (costo, vertice)
    
    #mientras el ultimo elemento de V no se sea end
    encontrado = False

    #mientras el ultimo elemento de V no se sea end
    while colaPrioridad and not encontrado:
      ( costo, inicio, anterior ) = heapq.heappop( colaPrioridad )

      #esta es la bandera para terminar el proceso
      if inicio == end:
        encontrado = True
        
      if not M[ inicio ]:
        M[ inicio ] = True
      #end if 
        
        VStar[inicio] = anterior

        #obtener el ultimo elemento de V y anadirle el peso de distancia
        vecinos =  A[inicio]

        for vecino in vecinos:
          
          heapq.heappush(colaPrioridad, (1, vecino, inicio))
        #end for
    #end while 
         
    # Si no se encuentra el camino
    
    if not encontrado:
      print("No se encontró camino de", start, "a", end)
      return []
    #end if
  
    #hacer el backtracking
    return backtrack(VStar, start, end)
# end def

'''
Esta hace el proceso de encontrar por el metodo de kruskal (aunque se parece un poco a prim)
obtener el mejor camino segun cruscal basado en la distancia
'''

def KruskalCheapest( G, start, end):
    # Obtener vertices y aristas
    V, A = G

    #numero de vertices
    n = len(V)
    #no marcados para cada vertice iniciamos sin marcar
    M = [ False for i in range( n ) ]
    
    # este es el vecto a retornar
    VStar = [ -1 for i in range( n ) ]

    #cola de prioridad
    colaPrioridad = [(0, start, start)] # (costo, vertice)
    
    #mientras el ultimo elemento de V no se sea end
    encontrado = False

    #mientras el ultimo elemento de V no se sea end
    while colaPrioridad and not encontrado:
      ( costo, inicio, anterior ) = heapq.heappop( colaPrioridad )

      #esta es la bandera para terminar el proceso
      if inicio == end:
        encontrado = True
        
      if not M[ inicio ]:
        M[ inicio ] = True
        
        VStar[inicio] = anterior

        #obtener el ultimo elemento de V y anadirle el peso de distancia
        vecinos =  A[inicio]

        for vecino in vecinos:
          #calcular la distancia entre el ultimo elemento de V y el vecino
          dist = distance(V[inicio], V[vecino])
          
          heapq.heappush(colaPrioridad, (dist, vecino, inicio))
    
    #end while
         
    # Si no se encuentra el camino
    if not encontrado:
      print("No se encontró camino de", start, "a", end)
      return []
    #end if
  
    #hacer el backtracking
    return backtrack(VStar, start, end)
# end def

"""
Este hace el proceso de backtracking con el objetivo de crear el camino encontrado
"""
def backtrack(T, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = T[current]
    path.append(start)
    path.reverse()
    return path
# end def

'''
'''
def main( argv ):
  fname = argv[ 1 ]
  pId = int( argv[ 2 ] )

  # Read data
  viewer = MeshViewer( fname, opacity = 0.8 )
  V, A = viewer.graph( )

  # Correct pId
  pId = pId % len( V )

  # Get farthest point
  qId = pId
  fDist = 0
  for i in range( len( V ) ):
    d = distance( V[ pId ], V[ i ] )
    if fDist < d:
      fDist = d
      qId = i
    # end if
  # end for

  # Get paths
  P  = [ DijkstraShortest( ( V, A ), pId, qId ) ]
  P += [ DijkstraCheapest( ( V, A ), pId, qId ) ]
  P += [ KruskalShortest( ( V, A ), pId, qId ) ]
  P += [ KruskalCheapest( ( V, A ), pId, qId ) ]

  # Define colors
  C = [ ( 1, 0, 0 ), ( 0, 1, 0 ), ( 0, 0, 1 ), ( 0, 0, 0 ) ]
  for i in range( 4 ) :
    viewer.add_path( P[ i ], C[ i ] )
  # end for

  viewer.show( )
# end def

""" ==================================================================== """
if __name__ == '__main__':
  if len( sys.argv ) < 3:
    print(
        'Usage: ' + sys.argv[ 0 ] + ' file.obj pId',
        file = sys.stderr, flush = True
        )
    sys.exit( 1 )
  # end if
  main( sys.argv )
# end if

## eof - compare_paths.py
