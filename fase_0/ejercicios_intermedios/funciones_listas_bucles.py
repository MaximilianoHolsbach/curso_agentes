# Escribí estas funciones. En ninguna uses max().
#   • maximo(lista): devuelve el número más grande. Si la lista está vacía, devuelve None.
#   • contar_mayores(lista, limite): cuántos números de la lista son mayores que limite.
#   • sumar_pares(lista): suma solo los números pares de la lista.
# Probalo con:
#   notas = [7, 9, 6, 10, 4]
#   print(maximo(notas), maximo([]))
#   print(contar_mayores(notas, 6))
#   print(sumar_pares(notas))
# Resultado esperado:
#   10 None
#   3
#   20

def maximo(lista):
    valor = 0
    if (len(lista)!= 0):
        for i in lista:
            if(valor < i):
                valor = i
        return valor
    else:
        return None

notas = [7,9,6,10,4]
vacia = []

print(maximo(notas))
print(maximo(vacia))

def contar_mayores(lista, limite):
    cont = 0
    if (len(lista)!= 0):
        for i in lista:
            if(limite < i):
                cont += 1
        return cont
    else:
        return None

print(contar_mayores(notas, 6))

def sumar_pares(lista):
    valor = 0
    for i in lista:
        if(i % 2 == 0):
            valor += i
    return valor

print(sumar_pares(notas))
