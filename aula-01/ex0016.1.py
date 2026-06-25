from math import hypot
co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
hi = hypot(co, ca)
print(f"A hipotenusa mede {hi:.2f}")