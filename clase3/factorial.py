def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

resultado = factorial(5)
print(f"La factorial de 5 es {resultado}")