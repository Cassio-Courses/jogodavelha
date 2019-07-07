import os
from time import sleep

class variaveis():
    clear = '\n' * 100
    XO={"a1":"", "b1":"", "c1":"", "a2":"", "b2":"", "c2":"", "a3":"", "b3":"", "c3":""}
def game():
    print('{}'.format('-'*20))
    print('{:>7}{:>3}{:>2}'.format('A','B','C'))
    print('1{:>6}{}{:^1}{}{:^1}'.format(val.XO['a1'],'│',val.XO['b1'],'│',val.XO['c1']))
    print('2{:>6}{}{:^1}{}{:^1}'.format(val.XO['a2'],'│',val.XO['b2'],'│',val.XO['c2']))
    print('3{:>6}{}{:^1}{}{:^1}'.format(val.XO['a3'],'│',val.XO['b3'],'│',val.XO['c3']))
    print('{}'.format('-'*20))
val=variaveis()
#variaveis
c=0
verification=0
comeco=0
#val.XO['a1'] val.XO['b1'] val.XO['c1'] val.XO['a2'] val.XO['b2']
#val.XO['c2'] val.XO['a3'] val.XO['b3'] val.XO['c3']
print(val.XO['a1'])

while (val.XO['a1']=='' or val.XO['b1']=='' or val.XO['c1']=='' or val.XO['a2']=='' or
val.XO['b2']=='' or val.XO['c2']=='' or val.XO['a3']=='' or val.XO['b3']=='' or
val.XO['c3']==''):

    verification=0
    if comeco==0:
        game()
        comeco=1
    x=str(input("Insira a posição que você deseja inserir"))

    print('\n'*100)
    a=c
    if x.lower().strip() == 'a1' or x.lower().strip() =='1a':
        if val.XO['a1'] == "":
            c += 1
            if c % 2== 0:
                val.XO['a1'] = 'X'
            elif c % 2== 1:
                val.XO['a1'] = 'O'

    elif x.lower().strip() == 'b1' or x.lower().strip() =='1b':
        if val.XO['b1'] == "":
            c += 1
            if c % 2== 0:
                val.XO['b1'] = 'X'
            elif c % 2== 1:
                val.XO['b1'] = 'O'

    elif x.lower().strip() == 'c1' or x.lower().strip() =='1c':
        if val.XO['c1'] == "":
            c += 1
            if c % 2== 0:
                val.XO['c1'] = 'X'
            elif c % 2== 1:
                val.XO['c1'] = 'O'

    elif x.lower().strip() == 'a2' or x.lower().strip() =='2a':
        if val.XO['a2'] == "":
            c += 1
            if c % 2== 0:
                val.XO['a2'] = 'X'
            elif c % 2== 1:
                val.XO['a2'] = 'O'

    elif x.lower().strip() == 'b2' or x.lower().strip() =='2b':
        if val.XO['b2'] == "":
            c += 1
            if c % 2== 0:
                val.XO['b2'] = 'X'
            elif c % 2== 1:
                val.XO['b2'] = 'O'


    elif x.lower().strip() == 'c2' or x.lower().strip() =='2c':
        if val.XO['c2'] == "":
            c += 1
            if c % 2== 0:
                val.XO['c2'] = 'X'
            elif c % 2== 1:
                val.XO['c2'] = 'O'

    elif x.lower().strip() == 'a3' or x.lower().strip() =='3a':
        if val.XO['a3'] == "":
            c += 1
            if c % 2== 0:
                val.XO['a3'] = 'X'
            elif c % 2== 1:
                val.XO['a3'] = 'O'

    elif x.lower().strip() == 'b3' or x.lower().strip() =='3b':
        if val.XO['b3'] == "":
            c += 1
            if c % 2== 0:
                val.XO['b3'] = 'X'
            elif c % 2== 1:
                val.XO['b3'] = 'O'

    elif x.lower().strip() == 'c3' or x.lower().strip() =='3c':
        if val.XO['c3'] == "":
            c += 1
            if c % 2== 0:
                val.XO['c3'] = 'X'
            elif c % 2== 1:
                val.XO['c3'] = 'O'

    else:
        print("Nenhum valor conhecido")
        verification=1
    if a == c and verification==0:
        print(val.clear)
        game()
        print(f"Já há valor preenchido na posição {x}")
    elif verification==1:
        game()
        print(f'"{x}"" não existe, insira posição correta')
    else:
        game()

game()
