


controle_escolha_sym = True
while controle_escolha_sym:
    escolher_sym = str(input('Escolha "X" ou "O":\n-> ')).strip().upper()
    if escolher_sym == 'X' or escolher_sym == 'O':
        controle_escolha_sym = False

player1 = escolher_sym
player2 = ''
player2 = 'O' if player1 == 'X' else 'X'

quad = []
for i in range(1,10):
    i = ' '
    quad.append(i)

restSpace = quad.count(' ')


def mostrarQuad():
    print(f'{quad[0]} |  {quad[1]}  | {quad[2]}')
    print(f'--|-----|--')
    print(f'{quad[3]} |  {quad[4]}  | {quad[5]}')
    print(f'--|-----|--')   
    print(f'{quad[6]} |  {quad[7]}  | {quad[8]}')

def jogadaPlayer(player):
    controle_escolha = True
    while controle_escolha:
        escolherPos = int(input(f'{player}-> '))
        if escolherPos >= 1  and escolherPos <= 9:
            if quad[escolherPos-1] == ' ':
                quad[escolherPos-1] = player
                controle_escolha = False
            elif quad[escolherPos-1] != ' ':
                print('Campo preenchido!')
                controle_escolha= True
        elif escolherPos < 1 or escolherPos > 9:
            print('Escolha entre 1 e 9')
            controle_escolha = True



jogada = True
while jogada:
    print(mostrarQuad())
    print(f'\nEscolha uma das posições para marcar o X/O\nAs posições começam em 1 até 9 da esquerda para a direita e de cima para baixo.')

    while restSpace >= 0:
        jogadaPlayer(player1)
        mostrarQuad()
        print(restSpace)
        jogadaPlayer(player2)
        mostrarQuad()
        print(restSpace)
        
    #if vencedor() == True:
        #print(vencedor())
    #jogada = False



