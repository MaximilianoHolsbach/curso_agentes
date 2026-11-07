# Creá el diccionario persona = {"nombre": "Ana", "edad": 30, "ciudad": "Rosario"} y hacé:
#   • Mostrar el nombre usando persona["nombre"].
#   • Agregar la clave "email" con el valor "ana@ejemplo.com".
#   • Cambiar la edad a 31.
#   • Mostrar persona.get("telefono", "sin dato") y explicar por qué no da error.
#   • Mostrar si "ciudad" está en el diccionario y si "telefono" está.
#   • Recorrerlo con for clave, valor in persona.items() mostrando clave -> valor.
# Por último, escribí describir(p) que devuelve el texto
# "Ana tiene 31 años y vive en Rosario".
#
# Probalo con:
#   persona = {"nombre": "Ana", "edad": 30, "ciudad": "Rosario"}
#   print(persona["nombre"])
#   persona["email"] = "ana@ejemplo.com"
#   persona["edad"] = 31
#   print(persona.get("telefono", "sin dato"))
#   print("ciudad" in persona, "telefono" in persona)
#   for clave, valor in persona.items():
#       print(clave, "->", valor)
#   print(describir(persona))
#
# Resultado esperado:
#   Ana
#   sin dato
#   True False
#   nombre -> Ana
#   edad -> 31
#   ciudad -> Rosario
#   email -> ana@ejemplo.com
#   Ana tiene 31 años y vive en Rosario
#
# Pista: persona["telefono"] da error (KeyError) si la clave no existe;
# persona.get("telefono", "sin dato") devuelve el valor de reemplazo
# en vez de fallar.
# Dentro de un f-string con comillas dobles, usá comillas simples
# para la clave: f"{p['nombre']}".

persona = {"nombre": "Ana", "edad":30, "ciudad": "Rosario"}

persona["email"] = "ana@ejemplo.com"

persona["edad"] = 31

print(persona.get("nombre"))

print(persona.get("telefono", "sin dato")) # No da error porque la funcion get tiene una segundo argumento que indica que realizar en caso de con encontrar la clave

print("ciudad" in persona)

print("telefono" in persona)

for clave, valor in persona.items():
    print(clave, ": ", valor)

print(f"{persona.get("nombre")}, tiene {persona.get("edad")} años, y vive en {persona.get("ciudad")}.")