def promedio(numeros):
    if not numeros: 
        return 0
    return sum(numeros)/len(numeros)

notas = [7,8,9,10]

print("Promedio: ", promedio(notas))

alumno = {"nombre":"Ana", "notas": notas}

for clave, valor in alumno.items(): # Return a set-like object providing a view on the dict's items.
    print(clave, "->", valor)