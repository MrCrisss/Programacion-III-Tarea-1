# Programacion-III-Tarea-1
===== RESULTADOS =====
Lista ordenada (binaria): 0.0029 ms
Tabla Hash (set): 0.0003 ms
Arbol Binario: 0.0054 ms

-------------------------------------------------------------------------------------------
Estructura de datos | Tiempo Promedio (ms) | Memoria Aproximada Usada | Complejidad Teorica

Lista ordenada             0.0029 ms                 Media                    O(log n)

Tabla Hash (set)           0.0003 ms                 Alta                     O(1)

Arbol Binario              0.0054 ms                 Alta                     O(log n)

-----------------------------------------------------------------------------------------------

- La lista ordenada 
a pesar que divide los datos en partes mas pequeñas es necesario que los datos esten ordenaods para que tenga un proceso mas rapido

-Tabla hash 
La tabla al utilizar la funcion hash accede rapidamente a la posicion del elemento buscado haciendo mas eficaz el proceso de busques
aunque usa un mayor consumo de memoria debido a la estructa interna que este tiene.

-Arbol Binario 
A pesar que su complejidad teorica es similar a la lista ordena , puede llegar a ser eficiente , pero si este arbol llega a desvalancearse 
puede llevar a degradarse haciendo un caos.

---------------------------------------------------------------------------------------------------
La estructura mas eficiente fue la tabla hash ya que su metodo es marapido ya que no cambia el tiempo aunque hayan mas y mas datos 
su tiempo siempre tarda lo mismo , pero ojo este fue el mas eficacas ya que lo que se estaba haciendo era una busqueda de datos y este 
al hacelo por posicion fue una manera mas rapida de respuesta.
