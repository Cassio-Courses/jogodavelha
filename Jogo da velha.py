class variaveis:
    clear = '\n' * 100
    XO = {"a1": "", "b1": "", "c1": "", "a2": "", "b2": "", "c2": "", "a3": "", "b3": "", "c3": ""}
    win = 0
    c = 0


# variaveis
val = variaveis()


def game():
    print('{}'.format('-' * 20))
    print('{:>7}{:>3}{:>2}'.format('A', 'B', 'C'))
    print('1{:>6}{}{:^1}{}{:^1}'.format(val.XO['a1'], '│', val.XO['b1'], '│', val.XO['c1']))
    print('2{:>6}{}{:^1}{}{:^1}'.format(val.XO['a2'], '│', val.XO['b2'], '│', val.XO['c2']))
    print('3{:>6}{}{:^1}{}{:^1}'.format(val.XO['a3'], '│', val.XO['b3'], '│', val.XO['c3']))
    print('{}'.format('-' * 20))

def play():
    comeco = 0
    val.c = 0
    while (val.XO['a1'] == '' or val.XO['b1'] == '' or val.XO['c1'] == '' or val.XO['a2'] == '' or
           val.XO['b2'] == '' or val.XO['c2'] == '' or val.XO['a3'] == '' or val.XO['b3'] == '' or
           val.XO['c3'] == ''):
        verificationfun()
        if verificationfun()[0] == 1:
            print("Parabéns", end=" ")
            if verificationfun()[1] == "X":
                print('"X" ganhou')
            else:
                print('"O" ganhou')
            break
        verification = 0
        if comeco == 0:
            game()
            comeco = 1
        if val.c % 2 == 0:
            x = str(input('"O" Insira a posição'))
        else:
            x = str(input('"X" Insira a posição'))

        print('\n' * 100)
        a = val.c
        if x.lower().strip() == 'a1' or x.lower().strip() == '1a':
            if val.XO['a1'] == "":
                val.c += 1
                if val.c % 2 == 0:
                    val.XO['a1'] = 'X'
                elif val.c % 2 == 1:
                    val.XO['a1'] = 'O'

        elif x.lower().strip() == 'b1' or x.lower().strip() == '1b':
            if val.XO['b1'] == "":
                val.c += 1
                if val.c % 2 == 0:
                    val.XO['b1'] = 'X'
                elif val.c % 2 == 1:
                    val.XO['b1'] = 'O'

        elif x.lower().strip() == 'c1' or x.lower().strip() == '1c':
            if val.XO['c1'] == "":
                val.c += 1
                if val.c % 2 == 0:
                    val.XO['c1'] = 'X'
                elif val.c % 2 == 1:
                    val.XO['c1'] = 'O'

        elif x.lower().strip() == 'a2' or x.lower().strip() == '2a':
            if val.XO['a2'] == "":
                val.c += 1
                if val.c % 2 == 0:
                    val.XO['a2'] = 'X'
                elif val.c % 2 == 1:
                    val.XO['a2'] = 'O'

        elif x.lower().strip() == 'b2' or x.lower().strip() == '2b':
            if val.XO['b2'] == "":
                val.c += 1
                if val.c % 2 == 0:
                    val.XO['b2'] = 'X'
                elif val.c % 2 == 1:
                    val.XO['b2'] = 'O'


        elif x.lower().strip() == 'c2' or x.lower().strip() == '2c':
            if val.XO['c2'] == "":
                val.c += 1
                if val.c % 2 == 0:
                    val.XO['c2'] = 'X'
                elif val.c % 2 == 1:
                    val.XO['c2'] = 'O'

        elif x.lower().strip() == 'a3' or x.lower().strip() == '3a':
            if val.XO['a3'] == "":
                val.c += 1
                if val.c % 2 == 0:
                    val.XO['a3'] = 'X'
                elif val.c % 2 == 1:
                    val.XO['a3'] = 'O'

        elif x.lower().strip() == 'b3' or x.lower().strip() == '3b':
            if val.XO['b3'] == "":
                val.c += 1
                if val.c % 2 == 0:
                    val.XO['b3'] = 'X'
                elif val.c % 2 == 1:
                    val.XO['b3'] = 'O'

        elif x.lower().strip() == 'c3' or x.lower().strip() == '3c':
            if val.XO['c3'] == "":
                val.c += 1
                if val.c % 2 == 0:
                    val.XO['c3'] = 'X'
                elif val.c % 2 == 1:
                    val.XO['c3'] = 'O'

        else:
            print("Nenhum valor conhecido")
            verification = 1
        if a == val.c and verification == 0:
            print(val.clear)
            game()
            print(f"Já há valor preenchido na posição {x}")
        elif verification == 1:
            game()
            print(f'"{x}"" não existe, insira posição correta')
        else:
            game()


def verificationfun():
    # horizontal win
    winwho = ''
    if val.XO['a1'] == "X" and val.XO['b1'] == "X" and val.XO['c1'] == "X":
        winwho = 'X'
        val.win = 1
    elif val.XO['a1'] == "O" and val.XO['b1'] == "O" and val.XO['c1'] == "O":
        winwho = 'O'
        val.win = 1
    elif val.XO['a2'] == "X" and val.XO['b2'] == "X" and val.XO['c2'] == "X":
        winwho = 'X'
        val.win = 1
    elif val.XO['a2'] == "O" and val.XO['b2'] == "O" and val.XO['c2'] == "O":
        winwho = 'O'
        val.win = 1
    elif val.XO['a3'] == "X" and val.XO['b3'] == "X" and val.XO['c3'] == "X":
        winwho = 'X'
        val.win = 1
    elif val.XO['a3'] == "O" and val.XO['b3'] == "O" and val.XO['c3'] == "O":
        winwho = 'O'
        val.win = 1
    # Vertical wins
    if val.XO['a1'] == "X" and val.XO['a2'] == "X" and val.XO['a3'] == "X":
        winwho = 'X'
        val.win = 1
    elif val.XO['a1'] == "O" and val.XO['a2'] == "O" and val.XO['a3'] == "O":
        winwho = 'O'
        val.win = 1
    elif val.XO['b1'] == "X" and val.XO['b2'] == "X" and val.XO['b3'] == "X":
        winwho = 'X'
        val.win = 1
    elif val.XO['b1'] == "O" and val.XO['b2'] == "O" and val.XO['b3'] == "O":
        winwho = 'O'
        val.win = 1
    elif val.XO['c1'] == "X" and val.XO['c2'] == "X" and val.XO['c3'] == "X":
        winwho = 'X'
        val.win = 1
    elif val.XO['c1'] == "O" and val.XO['c2'] == "O" and val.XO['c3'] == "O":
        winwho = 'O'
        val.win = 1
    # Diagonals Wins
    elif val.XO['c1'] == "X" and val.XO['b2'] == "X" and val.XO['a3'] == "X":
        winwho = 'X'
        val.win = 1
    elif val.XO['c1'] == "O" and val.XO['b2'] == "O" and val.XO['a3'] == "O":
        winwho = 'O'
        val.win = 1
    elif val.XO['a1'] == "X" and val.XO['b2'] == "X" and val.XO['c3'] == "X":
        winwho = 'X'
        val.win = 1
    elif val.XO['a1'] == "O" and val.XO['b2'] == "O" and val.XO['c3'] == "O":
        winwho = 'O'
        val.win = 1
    return val.win, winwho


restart = 's'
while restart.strip().lower()[0] == 's':
    play()
    if verificationfun()[0] == 0:
        print("Empatou hihi sifudeu")
    elif verificationfun()[0] == 1 and val.c == 9:
        print("Parabéns", end=" ")
        if verificationfun()[1] == "X":
            print('"X" ganhou')
        else:
            print('"O" ganhou')
    val.win = 0
    val.c = 0
    val.XO = {"a1": "", "b1": "", "c1": "", "a2": "", "b2": "", "c2": "", "a3": "", "b3": "", "c3": ""}
    restart = input("Quer jogar de novo? [S/N]")
