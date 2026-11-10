# ---------------------------------------------------------------
# EJERCICIO: Diccionarios anidados
#
# La respuesta de una API suele tener diccionarios dentro de
# diccionarios. Con la variable "respuesta" de la prueba (datos
# inventados, con la misma forma que una respuesta de clima):
#
#   - Mostrar la latitud, que está dentro de "coordenadas".
#   - Mostrar la temperatura junto con su unidad
#     ("Temperatura: 21.4 °C"), sacando ambos datos del diccionario.
#   - Agregar la clave "humedad" con el valor 63 dentro de "actual"
#     y mostrar ese diccionario.
#   - Mostrar la presión con .get(), con "sin dato" como reemplazo,
#     porque esa clave no existe.
#   - Escribir resumen(r) que devuelve
#     "Buenos Aires: 21.4 °C, viento 9.7 km/h".
#
# Prueba:
#   respuesta = {
#       "ciudad": "Buenos Aires",
#       "coordenadas": {"latitud": -34.61, "longitud": -58.38},
#       "actual": {"hora": "2026-11-05T22:00", "temperatura": 21.4, "viento": 9.7},
#       "unidades": {"temperatura": "°C", "viento": "km/h"},
#   }
#   print(respuesta["coordenadas"]["latitud"])
#   temp = respuesta["actual"]["temperatura"]
#   unidad = respuesta["unidades"]["temperatura"]
#   print("Temperatura:", temp, unidad)
#   respuesta["actual"]["humedad"] = 63
#   print(respuesta["actual"])
#   print(respuesta["actual"].get("presion", "sin dato"))
#   print(resumen(respuesta))
#
# Resultado esperado:
#   -34.61
#   Temperatura: 21.4 °C
#   {'hora': '2026-11-05T22:00', 'temperatura': 21.4, 'viento': 9.7, 'humedad': 63}
#   sin dato
#   Buenos Aires: 21.4 °C, viento 9.7 km/h
#
# Pista: se entra de afuera hacia adentro, una clave por vez:
#   respuesta["coordenadas"]["latitud"].
#   Si tenés dudas, mostrá primero respuesta["actual"] y después
#   pedí la clave que querés.
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# DATOS DE PRUEBA
# ---------------------------------------------------------------
respuesta = {
    "ciudad": "Buenos Aires",
    "coordenadas": {"latitud": -34.61, "longitud": -58.38},
    "actual": {"hora": "2026-11-05T22:00", "temperatura": 21.4, "viento": 9.7},
    "unidades": {"temperatura": "°C", "viento": "km/h"},
}


# ---------------------------------------------------------------
# FUNCIÓN PEDIDA
# ---------------------------------------------------------------
def resumen(r):
    """Devuelve un texto con el formato:
    "Buenos Aires: 21.4 °C, viento 9.7 km/h"
    """
    ciudad = r.get("ciudad")
    temperatura = r.get("actual").get("temperatura")
    unidad = r.get("unidades").get("temperatura")
    viento = r.get("actual").get("viento")
    unidad_viento = r.get("unidades").get("viento")
    return (f"{ciudad}: {temperatura}{unidad}, {viento} {unidad_viento}")
print(resumen(respuesta ))

# ---------------------------------------------------------------
# PRUEBAS (en este orden)
# ---------------------------------------------------------------

# 1. Mostrar la latitud (dentro de "coordenadas")
print(respuesta.get("coordenadas").get("latitud"))

# 2. Mostrar la temperatura con su unidad: "Temperatura: 21.4 °C"
temperatura = respuesta.get("actual").get("temperatura")
unidad_temperatura = respuesta.get("unidades").get("temperatura")
print(f"{temperatura}{unidad_temperatura}")

# 3. Agregar la clave "humedad" con valor 63 dentro de "actual"
respuesta.get("actual")["humedad"] = 63
# Mostrar el diccionario "actual" completo
print(respuesta.get("actual"))

# 4. Mostrar la presión con .get() y "sin dato" como reemplazo
print(f"presion: {respuesta.get("presion", "sin dato")}")

# 5. Mostrar el resumen
print(resumen(respuesta ))