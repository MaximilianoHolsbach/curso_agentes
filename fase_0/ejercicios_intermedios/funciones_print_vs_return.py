# Escribí tres funciones:
#   • es_impar(n): devuelve True si el número es impar y False si no.
#   • area_rectangulo(base, altura): devuelve el área.
#   • saludar(nombre): devuelve (no imprime) el texto "Hola, Ana!"
#     cuando recibe "Ana".
#
# Después escribí doble_con_return(n), que devuelve n * 2, y
# doble_con_print(n), que imprime n * 2 pero no tiene return.
# Guardá el resultado de cada una en las variables a y b, y mostrá
# qué contiene cada variable. ¿Por qué b no vale lo mismo que a?
#
# Probalo con:
#   print(es_impar(3), es_impar(8))
#   print(area_rectangulo(5, 3))
#   print(saludar("Ana"))
#   a = doble_con_return(4)
#   b = doble_con_print(4)
#   print("a vale:", a)
#   print("b vale:", b)
#
# Resultado esperado:
#   True False
#   15
#   Hola, Ana!
#   8
#   a vale: 8
#   b vale: None

def es_impar(n):
    if(n % 2 != 0):
        return True
    else:
        return False

def area_rectanculo(base, altura):
    return base * altura

def saludo(nombre):
    return f"Hola, {nombre}!"

def doble_con_return(n):
    return n * 2 

def doble_con_print(n):
    print(n * 2)

print(es_impar(3), es_impar(8))

print(area_rectanculo(5, 3))

print(saludo("Ana"))

a = doble_con_return(4)

b = doble_con_print(4) # Una función sin return devuelve None

print(f"a vale {a}")

print(f"b vale {b}")