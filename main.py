
def printglobo(tamanho, corte,objx,objy):
    for y in range(tamanho):
        linha = ""
        for x in range(tamanho):
            dist_borda_y = min(y, tamanho-1-y)
            dist_borda_x = min(x, tamanho-1-x)

            if dist_borda_x + dist_borda_y < corte:
                linha += " "
            elif (x == objx and y == objy):
                linha += "O"
            else:
                linha += "#"
        print(linha)

printglobo(15, 3, 5, 5)