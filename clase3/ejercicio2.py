"""
Calcular multiplicacion con sums y division con restas
"""

print("Multiplicación de sumas")
def suma(n1,n2):
    if n2 == 1:
        return n1
    return n1 + suma(n1,n2-1)

total = suma(3,5)
print(f"resultado {total}")