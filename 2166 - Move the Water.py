from sys import stdin
from collections import deque


def water(first_nodo):
	global grafo, visitados, capacidad, destino, pos, parents
	cola = deque([first_nodo])
	while len(cola) != 0:
		nodo = cola.popleft()
		if nodo != destino:
			for i in range(1, 4):
				for j in range(-1, 2, 2):
					nodo2 = list(nodo)
					if capacidad[pos[i+j]] - nodo[pos[i+j]] >= nodo[pos[i]]:
						nodo2[pos[i]], nodo2[pos[i+j]] = 0, nodo[pos[i]]+nodo[pos[i+j]]
					else:
						nodo2[pos[i]], nodo2[pos[i+j]] = nodo[pos[i]]-(capacidad[pos[i+j]] - nodo[pos[i+j]]), capacidad[pos[i+j]]
					nodo2 = tuple(nodo2)
					if nodo2 not in visitados:
						parents[nodo2] = nodo
						visitados.add(nodo2)
						grafo[nodo].append(nodo2)
						grafo[nodo2] = []
						cola.append(nodo2)


def recorrido(nodo):
	global parents
	if parents[nodo] == nodo:
		return 0
	else:
		return 1 + recorrido(parents[nodo])


def main():
	global grafo, visitados, capacidad, destino, pos, parents
	pos = [2, 0, 1, 2, 0]
	while True:
		a1, a2, a3, a4, a5, a6, a7, a8, a9 = [int(x) for x in stdin.readline().split()]
		capacidad, inicio, destino = (a1, a2, a3), (a4, a5, a6), (a7, a8, a9)
		if capacidad[0] == 0:
			break
		elif inicio == destino:
			print(0)
		elif inicio == (0, 0, 0) and inicio != destino:
			print(-1)
		else:
			grafo, visitados, parents = {inicio: []}, {inicio}, {inicio: inicio}
			water(inicio)
			if destino in parents:
				print(recorrido(destino))
			else:
				print(-1)


main()
