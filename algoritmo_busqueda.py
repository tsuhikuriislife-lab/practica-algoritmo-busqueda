numeros = ["1","4" , "8", "14", "18", "22", "26", "36", "56", "62", "74", "86", "92", "100"]

inicio = 0
final = len(numeros)-1

while True:
    numeroEscogido = input("Escriba el numero que desea verificar (0-100): ")
    if numeroEscogido in numeros:
        ciclo = 0
        while True:
            centro = (inicio+final)//2
            if numeroEscogido < numeros[centro]:
                final = centro
                ciclo += 1
                print(f"{numeroEscogido} es menor a {numeros[centro]}")
                continue
            elif numeroEscogido > numeros[centro]:
                inicio = centro
                ciclo += 1
                print(f"{numeroEscogido} es mayor a {numeros[centro]}")
                continue
            elif numeroEscogido == numeros[centro]:
                print(f"El numero está en la lista en la pocicion: {centro}")
                print(f"Se encontro en {ciclo} ciclos.")
                break
    else:
        print("El numero no esta en la lista.")
