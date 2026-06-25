preco = float(input("R$ Preco do produto: "))
if preco > 100.00:
    desconto = preco * 0.10
    print(f"\nPreco Original: R$ {preco:.2f}")
    print(f"Desconto aplicado: R$ {desconto:.2f}")

    print(f"Preço final: R$ {preco - desconto:.2f}")
else:
    desconto = preco * 0.00
    print(f"Desconto aplicado: R$ {desconto:.2f}")

    print(f"Preço final: R$ {preco - desconto:.2f}")
