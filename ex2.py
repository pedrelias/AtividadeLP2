A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
areaTriangulo = (A*C)/2.0
pi = 3.14159
areaCirculo = pi * (C**2)
areaTrapezio = ((A+B)*C)/2.0
areaQuadrado = B**2
areaRetangulo = A*B

print(f'TRIANGULO: {areaTriangulo:.3f}')
print(f'CIRCULO: {areaCirculo:.3f}')
print(f'TRAPEZIO: {areaTrapezio:.3f}')
print(f'QUADRADO: {areaQuadrado:.3f}')
print(f'RETANGULO: {areaRetangulo:.3f}')

