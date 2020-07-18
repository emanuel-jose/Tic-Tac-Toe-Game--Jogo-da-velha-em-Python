import random


# Escolher entre X e O:
controle_incial = True
while controle_incial:
    player = str(input('Escolha "X" ou "O":\n-> ')).strip().upper()
    if player == 'X' or player == 'O':
        controle_incial = False


# Mostrar o quadro:
quad = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
print(f'{quad[0]} |  {quad[1]}  | {quad[2]}')
print(f'--|-----|--')
print(f'{quad[3]} |  {quad[4]}  | {quad[5]}')
print(f'--|-----|--')   
print(f'{quad[6]} |  {quad[7]}  | {quad[8]}')

# Jogada do Player
print(f'\nEscolha uma das posições para marcar o {player}\nAs posições começam em 1 até 9 da esquerda para a direita e de cima para baixo.')

controle_rodada = True
while controle_rodada:
    controle_escolha = True
    while controle_escolha:
        escolherPos = int(input('-> '))
        if escolherPos >= 1 and escolherPos <= 9:
            if quad[escolherPos-1] == ' ':
                quad[escolherPos-1] = player
                controle_escolha = False
            elif quad[escolherPos-1] != ' ':
                print('Campo já preenchido!')
                controle_escolha = True
        elif escolherPos < 1  or escolherPos > 10:
            print('Escolha entre 1 e 9')
            controle_escolha = True
                
        

    
    print(f'{quad[0]} |  {quad[1]}  | {quad[2]}')
    print(f'--|-----|--')
    print(f'{quad[3]} |  {quad[4]}  | {quad[5]}')
    print(f'--|-----|--')   
    print(f'{quad[6]} |  {quad[7]}  | {quad[8]}')    

    restSpace = quad.count(' ')
   

    # Jogada PC

    pc = ''
    if player == 'X':
        pc = 'O'
    elif player == 'O':
        pc = 'X'
    if restSpace > 0:
        print('\nComputador está escolhendo...\n')
        print('Pronto!')
        controle_escolhapc = True
        while controle_escolhapc:
            escolherPosPc = random.randint(0,8)
            if escolherPosPc != escolherPos and quad[escolherPosPc] == ' ':
                quad[escolherPosPc] = pc
                controle_escolhapc = False
            elif escolherPosPc == escolherPos and quad[escolherPosPc]!= ' ':
                controle_escolhapc = True

        print(f'{quad[0]} |  {quad[1]}  | {quad[2]}')
        print(f'--|-----|--')
        print(f'{quad[3]} |  {quad[4]}  | {quad[5]}')
        print(f'--|-----|--')   
        print(f'{quad[6]} |  {quad[7]}  | {quad[8]}')
    
    


   # Validando o vencedor:
   # horizontal
    h1 = [quad[0],quad[3],quad[6]]
    ph1 = h1.count(player)
    ch1 = h1.count(pc)

    h2 = [quad[1],quad[4],quad[7]]
    ph2 = h2.count(player)
    ch2 = h2.count(pc)

    h3 = [quad[2],quad[5],quad[8]]
    ph3 = h3.count(player)
    ch3 = h3.count(pc)

    # vertical
    v1 = [quad[0],quad[1],quad[2]]
    pv1 = v1.count(player)
    cv1 = v1.count(pc)

    v2 = [quad[3],quad[4],quad[5]]
    pv2 = v2.count(player)
    cv2 = v2.count(pc)

    v3 = [quad[6],quad[7],quad[8]]
    pv3 = v3.count(player)
    cv3 = v3.count(pc)

    # diagonal
    d1 = [quad[0],quad[4],quad[8]]
    pd1 = d1.count(player)
    cd1 = d1.count(pc)

    d2 = [quad[2],quad[4],quad[6]]
    pd2 = d2.count(player)
    cd2 = d2.count(pc)
    
    controle_reiniciar = False
    winPlay = False
    winPc = False

    if ph1 == 3 or ph2 == 3 or ph3 == 3 or pv1 == 3 or pv2 == 3 or pv3 == 3 or pd1 == 3 or pd2 == 3:
        winPlay = True
        print('Player Venceu! :D')
        controle_rodada = False
        controle_reiniciar = True
    elif ch1 == 3 or ch2 == 3 or ch3 == 3 or cv1 == 3 or cv2 == 3 or cv3 == 3 or cd1 == 3 or cd2 == 3:
        winPc = True
        print('Você perdeu! :(')
        controle_rodada = False
        controle_reiniciar = True
    
    # Velha
    if restSpace == 0 and winPlay == False and winPc == False:
        print('Deu Velha! :(')
        controle_rodada = False
        controle_reiniciar = True

    
    while controle_reiniciar:
        again = str(input('\nDeseja jogar novamente s/n\n-> ')).strip().upper()
        if again == 'S':
            quad.clear()
            quad = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            print(f'{quad[0]} |  {quad[1]}  | {quad[2]}')
            print(f'--|-----|--')
            print(f'{quad[3]} |  {quad[4]}  | {quad[5]}')
            print(f'--|-----|--')   
            print(f'{quad[6]} |  {quad[7]}  | {quad[8]}')
            controle_reiniciar = False
            controle_rodada = True
        elif again == 'N':
            print('By :(')
            controle_reiniciar = False
            controle_rodada = False
    
