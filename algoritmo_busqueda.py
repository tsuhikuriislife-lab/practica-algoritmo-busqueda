import random

def numeroEncontrado():
    print(f"El numero está en la lista en la posicion: {centro}")
    print(f"Se encontro en {ciclo} ciclos.")
def ajusteFinal(centro, ciclo, final):
    final = centro - 1
    ciclo += 1
    return final, ciclo
def ajusteInicio(centro, ciclo, inicio):
    inicio = centro + 1
    ciclo += 1
    return inicio, ciclo

numeros = random.sample(range(0,100), 50)
numeros.sort()
print(numeros)
while True:
    numeroEscogido = int(input("Escriba el numero que desea verificar (0-100): "))
    if numeroEscogido in numeros:
        ciclo = 0
        inicio = 0
        final = len(numeros)-1
        while True:
            centro = (inicio+final)//2
            if numeroEscogido == numeros[centro]:
                numeroEncontrado()
                break
            elif numeroEscogido < numeros[centro]:
                final, ciclo = ajusteFinal(centro, ciclo, final)
                print(f"{numeroEscogido} es menor a {numeros[centro]}")
                continue
            else:
                inicio, ciclo = ajusteInicio(centro, ciclo, inicio)
                print(f"{numeroEscogido} es mayor a {numeros[centro]}")
                continue
    else:            
        print("El numero no esta en la lista.")
