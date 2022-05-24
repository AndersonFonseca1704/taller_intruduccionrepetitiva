print("-------------------------------------")
print("----Determinar-si-esprimo-o-no-------")
print("-------------------------------------")

n = int(input("Introduce un número entero positivo : "))
i = n
while n % i != 0:
    i=n
    
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
