def es_par(numero):
    if not numero:
        return "No es un número"
    return "Es par" if numero % 2 == 0 else "No es par"

numeros = [1,2,3,4,5,6,7,8,9]

for i, numero in enumerate(numeros) :
    print(f"El número: {numero} {es_par(numero)}")