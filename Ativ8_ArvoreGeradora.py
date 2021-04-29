import csv
from igraph import Graph,plot

def lerCSV(caminho):
    matriz = []
    with open(caminho) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()
        for row in csv_reader:
            matriz = matriz + [row[1:]]
    
    matriz = [[int(j) for j in i] for i in matriz]
    return matriz

matriz = lerCSV("Ativ8_ArvoreGeradora.csv")
ag = []
for i in matriz:
        ag.append([0]*len(matriz))
pilha = []

def plotarGrafo(matriz, nome):
    g = Graph()
    g.add_vertices(len(matriz))
    for v1 in range(len(matriz)-1):
        for v2 in range(v1+1, len(matriz[v1])):
            if(matriz[v1][v2] == 1):
                g.add_edges([(v1,v2)])
    visual_style = {}
    visual_style["vertex_label"] = [str(x) for x in list(range(0+1, len(matriz)+1))]
    plot(g, **visual_style, target= nome + ".png")

def DFS_Iterativa(s):
    vis = [False]*len(matriz)
    pilha.append(s)
    pais = [] # Adiciona os vertices que estão sendo visitados

    while(pilha):
        u = pilha.pop()
        if not(vis[u]):
            if(pais): # Serve para quando for o inicio e não entrar nesse if
                ag[pais[-1]][u] = 1 # -1 para pegar o ultimo valor do vetor
                ag[u][pais[-1]] = 1
            pais.append(u)
            vis[u] = True
            tamanhoA = len(pilha)
            for i in range(len(matriz)):
                if(matriz[u][i] == 1):
                    if not(vis[i]):
                        pilha.append(i)
            if(tamanhoA == len(pilha)): # Se todos os vertices adjacentes de u já tenham sido visitados.
                pais.pop()
        else:
            pais.pop() # Pode acontecer do vertice adjacente não visitado de x também ser adjacente de y e fazer com que ele se repita na pilha.
        print("Pilha:",pilha, end=" ------/------ ")
        print("Pais:",pais)


DFS_Iterativa(0)
plotarGrafo(matriz, "matriz_atv_8")
plotarGrafo(ag, "ag_atv_8")