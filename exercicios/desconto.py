valor = float(input('Digite o valor da compra: '))


desconto = valor - (valor * 10) / 100

print('O desconto da compra {} foi de {:.2f} '.format(valor, desconto))