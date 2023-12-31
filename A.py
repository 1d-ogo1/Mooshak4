n, t = map(int, input().split())    # n --> Numero de nóz / t --> Numero de Troços(ramos)
#   Informação dos troços é dada com quatro inteiros
troco = {}
percursos = []
minimo = 0
maximo = 0
x = 0

for k in range(t):  # Associação do input sobre a informação dos troços em dicionarios
    m = list(map(int, input().split()))
    a = (m[0], m[1])
    b = m[2]
    troco[a] = b

caminho = list(map(int, input().split()))   # lista com o caminho percorrido

while caminho[0] != 0:  # Loop para assimilação da temperatura por cada percurso e print do output

    anterior = caminho[1]

    for k in range(2, len(caminho), 1):

        if ((anterior, caminho[k]) in troco) and x == 0:
            minimo = troco[(anterior, caminho[k])]
            maximo = troco[(anterior, caminho[k])]
            x = 1

        elif ((caminho[k], anterior) in troco) and x == 0:
            minimo = troco[(caminho[k], anterior)]
            maximo = troco[(caminho[k], anterior)]
            x = 1

        elif ((anterior, caminho[k]) in troco) and troco[(anterior, caminho[k])] < minimo:
            minimo = troco[(anterior, caminho[k])]

        elif ((caminho[k], anterior) in troco) and troco[(caminho[k], anterior)] < minimo:
            minimo = troco[(caminho[k], anterior)]

        elif ((anterior, caminho[k]) in troco) and troco[(anterior, caminho[k])] > maximo:
            maximo = troco[(anterior, caminho[k])]

        elif ((caminho[k], anterior) in troco) and troco[(caminho[k], anterior)] > maximo:
            maximo = troco[(caminho[k], anterior)]

        anterior = caminho[k]

    print(minimo, maximo)
    x = 0

    caminho = list(map(int, input().split()))
