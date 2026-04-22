salario = float(input('Digite o reajuste: '))
porcentual = float(input('Digite o porcentual: '))

reajuste =  salario * porcentual
novo_salario = salario + reajuste

print('Salário atual: R${:.2f}'.format(salario))
print('Reajuste: R${:.2f}'.format(reajuste))
print('Novo salário: R${:.2f}'.format(novo_salario))