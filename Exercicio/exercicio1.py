import time
import os


num = int(input('informe um numero:' ))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000

if len(str(num)) <= 4:
    print('analisando o número', num)
    print('Unidade', u )
    print('Dezena', d )
    print('Centena', c )
    print('Milhar', m )

else:
    print('O seu número precisa de 4 digitos')

time.sleep(4)
os.system('clear')
       