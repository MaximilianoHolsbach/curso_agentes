# ---------------------------------------------------------------
# EJERCICIO: Lista de diccionarios
#
# Una lista de diccionarios es la forma más común en que una API
# entrega varios registros. Usar la lista "alumnos" de la prueba
# y escribir las siguientes funciones:
#
#   - promedio_alumno(alumno):
#       Devuelve el promedio de sus notas.
#       Si no tiene notas, devuelve 0.
#
#   - aprobados(alumnos, minimo=6):
#       Devuelve una lista con los nombres de los alumnos cuyo
#       promedio es mayor o igual a "minimo".
#
#   - mejor_alumno(alumnos):
#       Devuelve el nombre del alumno con mejor promedio.
#
# Prueba:
#   alumnos = [
#       {"nombre": "Ana", "notas": [7, 9, 6, 10]},
#       {"nombre": "Luis", "notas": [5, 4, 6]},
#       {"nombre": "Marta", "notas": []},
#   ]
#   for alumno in alumnos:
#       print(alumno["nombre"] + ":", promedio_alumno(alumno))
#   print(aprobados(alumnos))
#   print(mejor_alumno(alumnos))
#
# Resultado esperado:
#   Ana: 8.0
#   Luis: 5.0
#   Marta: 0
#   ['Ana']
#   Ana
#
# Pista: alumno["notas"] es una lista dentro del diccionario.
# Reutilizar promedio_alumno en las otras dos funciones.
# ---------------------------------------------------------------

def promedio_alumno(notas):
    if (len(notas) != 0):
        promedio = sum(notas) / len(notas)
    else:
        return 0   
    return promedio

def aprobados(alumnos, minimo = 6):
    alumnos_aprobados = []
    for alumno in alumnos:
        if(minimo <= alumno.get("promedio")):
            alumnos_aprobados.append(alumno["nombre"])
    return alumnos_aprobados

def mejor_alum(alumnos):
    mejor = 0
    alum = ""
    for a in alumnos:
        if (mejor < promedio_alumno(a.get("notas"))):
            mejor = promedio_alumno(a.get("notas"))
            alum = a.get("nombre")
    return alum


alumnos = [
    {"nombre": "Ana", "notas": [7, 9, 6, 10]},
    {"nombre": "Luis", "notas": [6, 10, 10]},
    {"nombre": "Marta", "notas": []},  # alumna sin notas cargadas
]

for alumno in alumnos:
    notas = alumno.get("notas")
    alumno["promedio"] = promedio_alumno(notas)
    print(f"Alumno: {alumno.get("nombre")} -> Promedio: {alumno.get("promedio")}")

alumnos_aprobados = aprobados(alumnos)

for a in alumnos_aprobados:
    print(f"Aprobó: {a}")

print(f"El mejor alumnos es: {mejor_alum(alumnos)}")
