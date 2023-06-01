def valid(jogador = True, gol = True):
    if jogador == True:
        jogador = jogador
    elif gol == True:
        gol = gol
    elif jogador == False:
        jogador = "<desconhecido>"
    elif gol == False:
        gol = 0
    return jogador, gol    
    
    
jogador = input("Nome do jogador: ")
gol = int(input("Número de gols: "))

print(valid(gol))
