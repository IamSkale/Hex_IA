# Proyecto de IA de Hex

**Diego Hernández Rodríguez C311**

HEX es un juego de conexión para dos jugadores en un tablero. En este caso, usamos el formato *even-r*, desplazando las filas pares. El jugador 1 (🔴) busca conectar los lados izquierdo y derecho, mientras que el jugador 2 (🔵) intenta conectar los lados superior e inferior.

---

## Estrategia de la IA

Este proyecto consiste en implementar una IA para dicho juego que tome la mejor jugada en cada turno. Para ello, he utilizado una **estrategia de ponderación**, que consiste en asignar valores a las casillas:

- **0** a las casillas propias  
- **1** a las casillas vacías  
- **Infinito** a las casillas enemigas  

De esta forma, empleamos el algoritmo de **Dijkstra** para calcular el camino de costo mínimo entre los bordes que debe unir el jugador, obteniendo así la jugada óptima.

Esta ponderación refleja la naturaleza del juego:
- Las fichas propias ya forman parte de la red de conexión.
- Las vacías representan futuros movimientos.
- Las enemigas actúan como barreras que bloquean el paso.

---

## Ventajas

- **Visión a largo plazo**: Considera el impacto de cada jugada en la conectividad general.
- **Defensiva implícita**: Al minimizar la distancia propia, indirectamente se bloquean caminos enemigos.
- **Óptimo local garantizado**: En cada turno, se selecciona la jugada que más acerca a la victoria según el modelo.

---

## Desventajas

- **Naturaleza *greedy***: Es miope, puesto que no considera jugadas futuras.
- **No anticipa respuestas enemigas**: No utiliza árboles de búsqueda ni minimax.

---

## Conclusión

La estrategia implementada demuestra cómo un algoritmo clásico de teoría de grafos puede adaptarse efectivamente a un problema de juego abstracto como HEX. El uso de Dijkstra con ponderación de celdas proporciona una heurística sólida para evaluar la conectividad del tablero, permitiendo a la IA tomar decisiones informadas que minimizan la distancia hacia la victoria.
