import os
import time
import sys

def printglobo(tamanho, corte):

    largura_mapa = tamanho*2

    if os.name == "nt":
        os.system("")

    mapa = []
    for y in range(tamanho):
        linha = []
        for x in range(largura_mapa):
            if 3<x<7 and 3<y<7:
                linha += "O"
            else:
                linha += "#"
        mapa.append(linha)

    os.system("cls" if os.name == "nt" else "clear")
    sys.stdout.write("\033[?25l")

    tela_anterior = [["" for _ in range(tamanho)] for _ in range(tamanho)]
    deslocamento = 0
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            for y in range(tamanho):
                for x in range(tamanho):
                    dist_borda_y = min(y, tamanho-1-y)
                    dist_borda_x = min(x, tamanho-1-x)

                    if dist_borda_x + dist_borda_y < corte:
                        char_atual = "  "
                    else:
                        linha_atual = mapa[y % len(mapa)]
                        x_mapa = (x + deslocamento) % len(linha_atual)
                        char_atual = mapa[y][x_mapa] + "  "

                    if char_atual != tela_anterior[y][x]:
                        linha_ansi = y + 1
                        coluna_ansi = (x*2) + 1

                        sys.stdout.write(
                            f"\033[{linha_ansi};{coluna_ansi}H{char_atual}"
                        )
                        tela_anterior[y][x] = char_atual

            sys.stdout.flush()

            deslocamento = (deslocamento + 1) % largura_mapa
            time.sleep(0.15)

    except KeyboardInterrupt:
        sys.stdout.write(f"\033[{tamanho + 2};1H\033[?25h")
        sys.stdout.flush()

    printglobo(15, 3)