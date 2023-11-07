nome= str(input('Digite o seu nome completo: ')).strip()
x = nome.split()

list= []
list.append(x)

y= len(nome)-nome.count(' ')


print(f'Seu nome é', nome.upper(),'seu nome tem ', y,'letras, seu primeiro nome é' ,x[0], 'e tem' ,len(x[0]), 'letras ')
