COTACAO_USD = 5.15 #cotação referência
real = float(input('R$ Quanto você tem na carteria?'))
dolar = real / COTACAO_USD
print(f'Com  R$ {real:.2f} você pode comprar 'f'US$ {dolar:.2f}')