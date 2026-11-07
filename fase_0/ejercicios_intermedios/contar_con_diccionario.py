# Escribí contar_letras(texto): devuelve un diccionario con cuántas veces
# aparece cada letra. Tiene que ignorar los espacios y no distinguir
# mayúsculas de minúsculas.
# Después escribí letra_mas_frecuente(conteo): recibe ese diccionario y
# devuelve una tupla (letra, veces) con la letra que más aparece.
#
# Probalo con:
#   conteo = contar_letras("Banana split")
#   print(conteo)
#   print(letra_mas_frecuente(conteo))
#
# Resultado esperado:
#   {'b': 1, 'a': 3, 'n': 2, 's': 1, 'p': 1, 'l': 1, 'i': 1, 't': 1}
#   ('a', 3)
#
# Pista: Es el mismo patrón de conteo del manual:
# conteo[letra] = conteo.get(letra, 0) + 1.
# Para saltear los espacios usá if letra == " ": continue.

def contar_letras(texto):
    texto = texto.strip().lower()
    cont={}
    valor = 0
    for i in texto:
        if(i != " "):
            cont[i] = cont.get(i, 0) + 1
    return cont

frase = "Banana split"

print(contar_letras(frase))


