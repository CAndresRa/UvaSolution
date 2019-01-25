from sys import stdin
from collections import deque


def bfs(nodo, limite):
	global grafo
	resul = 0
	cola = deque([])
	visitados = set()
	cola.append(nodo)
	distancia = {i: (float('inf') if i != nodo else 0) for i in grafo}
	if nodo in grafo:
		while len(cola) > 0:
			aux = cola.popleft()
			if aux not in visitados:
				if distancia[aux]+1 <= limite:
					for key in grafo[aux]:
						cola.append(key)
						distancia[key] = min(distancia[key], distancia[aux]+1)
				resul += 1
				visitados.add(aux)
	return resul


def main():
	global grafo
	caso = 1
	while True:
		try:
			n = int(stdin.readline())
			if n == 0:
				break
			else:
				grafo = {}
				while n > 0:
					lista_nodos = [int(x) for x in stdin.readline().split()]
					n -= (len(lista_nodos)//2)
					for i in range(0,len(lista_nodos),2):
						if lista_nodos[i] not in grafo and lista_nodos[i+1] not in grafo:
							grafo[lista_nodos[i]] = {lista_nodos[i+1]}
							grafo[lista_nodos[i+1]] = {lista_nodos[i]}
						elif lista_nodos[i] not in grafo and lista_nodos[i+1] in grafo:
							grafo[lista_nodos[i]] = {lista_nodos[i+1]}
							grafo[lista_nodos[i+1]].add(lista_nodos[i])
						elif lista_nodos[i] in grafo and lista_nodos[i+1] not in grafo:
							grafo[lista_nodos[i]].add(lista_nodos[i+1])
							grafo[lista_nodos[i+1]] = {lista_nodos[i]}
						else:
							grafo[lista_nodos[i]].add(lista_nodos[i+1])
							grafo[lista_nodos[i+1]].add(lista_nodos[i])
				boolean = True
				while boolean:
					queries = [int(x) for x in stdin.readline().split()]
					n = len(queries)
					if queries[-1]==queries[-2]==0:
						boolean = False
						n -= 2
					for i in range(0,n,2):
						x = bfs(queries[i], queries[i+1])
						print("Case {0}: {1} nodes not reachable from node {2} with TTL = {3}.".format(caso, len(grafo)-x, queries[i], queries[i+1]))
						caso += 1
				stdin.readline()
		except ValueError:
			pass


main()
