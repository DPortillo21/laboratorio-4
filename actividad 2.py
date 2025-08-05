def is_prime(n, divisor=2):
    print(f"Probando si {n} es divisible por {divisor}...\n")

    if n < 2:
        print(f"{n} no es primo (menor que 2).\n")
        return False
    if divisor * divisor > n:
        print(f"No se encontraron divisores: {n} es primo.\n")
        return True
    if n % divisor == 0:
        print(f"{n} es divisible por {divisor}: No es primo.\n")
        return False

    return is_prime(n, divisor + 1)

print("Resultado final:", is_prime(7)) 
print("Resultado final:", is_prime(9))  

def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)

print(sum_recursive(5))  




