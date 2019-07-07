import os
from time import sleep
class variaveis():
    clear = '\n'*100
    XO={"a11":"", "a12":"", "a13":"", "a21":"", "a22":"", "a23":"", "a31":"", "a32":"", "a33":""}
def game():
    print('{}'.format('-'*20))
    print('{:>8}{}{:^1}{}{:^1}'.format(val.XO['a11'],'│',val.XO['a12'],'│',val.XO['a13']))
    print('{:>8}{}{:^1}{}{:^1}'.format(val.XO['a21'],'│',val.XO['a22'],'│',val.XO['a23']))
    print('{:>8}{}{:^1}{}{:^1}'.format(val.XO['a31'],'│',val.XO['a32'],'│',val.XO['a33']))
    print('{}'.format('-'*20))
val=variaveis()
#variaveis
c=0

#val.XO['a11'] val.XO['a12'] val.XO['a13'] val.XO['a21'] val.XO['a22']
#val.XO['a23'] val.XO['a31'] val.XO['a32'] val.XO['a33']
print(val.XO['a11'])

while (val.XO['a11']=='' or val.XO['a12']=='' or val.XO['a13']=='' or val.XO['a21']=='' or
val.XO['a22']=='' or val.XO['a23']=='' or val.XO['a31']=='' or val.XO['a32']=='' or
val.XO['a33']==''):
    x=input("Insira a posição que você deseja inserir ")
    c+=1

    if x == 'a11':
        if c % 2== 0:
            val.XO['a11'] = 'X'
        elif c % 2== 1:
            val.XO['a11'] = 'O'
    elif x == 'a12':
        if c % 2== 0:
            val.XO['a12'] = 'X'
        elif c % 2== 1:
            val.XO['a12'] = 'O'
    elif x == 'a13':
        if c % 2== 0:
            val.XO['a13'] = 'X'
        elif c % 2== 1:
            val.XO['a13'] = 'O'
    elif x == 'a21':
        if c % 2== 0:
            val.XO['a21'] = 'X'
        elif c % 2== 1:
            val.XO['a21'] = 'O'
    elif x == 'a22':
        if c % 2== 0:
            val.XO['a22'] = 'X'
        elif c % 2== 1:
            val.XO['a22'] = 'O'
    elif x == 'a23':
        if c % 2== 0:
            val.XO['a23'] = 'X'
        elif c % 2== 1:
            val.XO['a23'] = 'O'
    elif x == 'a31':
        if c % 2== 0:
            val.XO['a31'] = 'X'
        elif c % 2== 1:
            val.XO['a31'] = 'O'
    elif x == 'a32':
        if c % 2== 0:
            val.XO['a32'] = 'X'
        elif c % 2== 1:
            val.XO['a32'] = 'O'
    elif x == 'a33':
        if c % 2== 0:
            val.XO['a33'] = 'X'
        elif c % 2== 1:
            val.XO['a33'] = 'O'
    else: print("Nenhum valor conhecido")

    game()
