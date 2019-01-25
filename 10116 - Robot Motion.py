from sys import stdin
def main():

    f,c,inicio = [int(x) for x in stdin.readline().strip().split()]
    while f:
        movimientos = {'N': (-1, 0), 'E': (0, 1), 'W': (0, -1), 'S': (1, 0)}
        casillas = f*c
        laberinto = []
        visitados = [False]*(casillas)
        secuencia = []
        posx = 0
        posy = inicio-1
        for x in range(f):
            a = stdin.readline().strip()
            laberinto.append(a)
        for x in range(casillas):
            pos_actual = posx * c + posy
            if visitados[pos_actual]:
                momento_del_ciclo = secuencia.index(pos_actual)
                pasos = momento_del_ciclo
                pasos_antes = len(secuencia) - momento_del_ciclo
                print('{} step(s) before a loop of {} step(s)'.format(pasos,pasos_antes))
                break
              
          
            visitados[pos_actual] = True
            secuencia.append(pos_actual)
            movimientox,movimientoy = movimientos[laberinto[posx][posy]]
            new_posx = posx+movimientox
            new_posy = posy+movimientoy

            if 0 <= new_posx < f and 0 <= new_posy < c:
                posx, posy = new_posx,new_posy
            else:
                pasos = len(secuencia)
                print('{} step(s) to exit'.format(pasos))
                break
            flag = True
            for x in range(len(visitados)):
                if visitados[x] == False:
                    flag = False
            if flag:
                print('{} step(s) before a loop of {} step(s)'.format(0,(f*c)))
                break
            
                
        f,c,inicio = [int(x) for x in stdin.readline().strip().split()]
main()
    
