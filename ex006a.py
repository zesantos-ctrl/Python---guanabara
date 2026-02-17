
#Desafio 1
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

s = n1 + n2

print('A soma entre {} e {} é {} '.format(n1,n2,s))

#Desafio 2
n = input('Digite algo: ')
print(n.isnumeric())
print(n.isalpha())
print(n.isdecimal())
print(n.islower())
print(n.isupper())