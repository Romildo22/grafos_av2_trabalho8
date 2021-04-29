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

matriz = lerCSV("Ativ8_Conexos.csv")
vis = [False]*len(matriz)

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
    
    pais = [] # Adiciona os vertices que estão sendo visitados
    pilha = []
    pilha.append(s)
    while(pilha):
        u = pilha.pop()
        if not(vis[u]):
            pais.append(u+1)
            vis[u] = True
            for i in range(len(matriz)):
                if(matriz[u][i] == 1):
                    if not(vis[i]):
                        pilha.append(i)
    return pais

def conexos():
    listCC = []
    for i in range(len(matriz)):
        if(vis[i] == False): 
            listCC.append(DFS_Iterativa(i))
    
    ordenada = sorted(listCC, key=len, reverse= True)
    for c in range(len(ordenada)):
        print("Componente conexo " + str(c+1) + ", tamanho = " +  str(len(ordenada[c])) + ", vertices: " + str(ordenada[c]))

conexos()
plotarGrafo(matriz, "matriz_atv_8")