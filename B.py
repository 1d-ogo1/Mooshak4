#   Criar um dicionario que guarde a informação do comprimento de cada percurso
#   Criar um dicionario que guarde quantos nóz estão adejacente a um certo nó


p, n = map(int, input().split())    # p--> numero de trajeto, n --> numero de nóz
caminhos = {}

for k in range(p):
    s = list(map(int, input().split()))
    total_comp = 0
    for i in range(1, len(s)-2, 2):     # Loop construtor do dicionario caminhos com os segmentos e os seus comprimentos
        caminhos[(s[i], s[i+2])] = s[i+1]
        total_comp += s[i+1]

    print("Trajeto %s: %d" % (k+1, total_comp))

for k in range(1, n+1):
    total_corr = 0
    x = 1
    while x <= n:   # Analise do numero de vertices adejacentes a cada vertice não repetindo vertices iguais
        if (k, x) in caminhos:
            total_corr += 1
        elif (x, k) in caminhos:
            total_corr += 1
        x += 1

    print("No %d: %d" % (k, total_corr))
