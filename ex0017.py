from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo(graus):'))
rad = radians(angulo)

seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print(f'O ângulo de {angulo}° tem: ')
print(f'Seno: {seno:.2f} Cosseno: {cosseno:.2f} Tangente: {tangente:.2f}')