import math

angulo = float(input('Digite o valor do angulo: '))

rad = math.radians(angulo)


print("Seno: {:.2f} ".format( math.sin(rad), math.ceil(rad)))
print("Cosseno: {:.2f} ".format( math.cos(rad), math.ceil(rad)))
print("Tangente: {:.2f} ".format( math.tan(rad), math.ceil(rad)))
