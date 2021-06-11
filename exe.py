import math
valorCompra = float(input('Valor da compra: '))
nParcelas = int(input('Número de parcelas: '))
taxa = 0.05*valorCompra
desconto = valorCompra-taxa
acrescimo = valorCompra+taxa
if nParcelas==1 and valorCompra>0:
    print(f'Valor final: {desconto:.2f}')
elif nParcelas>0 and nParcelas<=10 and valorCompra>0:
    print(f'Valor final: {acrescimo:.2f}')
    print(f'Parcelas: {acrescimo/nParcelas:.2f}')
else:
    print('Número de parcelas inválido')
#TESTE