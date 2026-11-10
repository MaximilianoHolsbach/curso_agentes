# ---------------------------------------------------------------
# EJERCICIO 8: De texto JSON a diccionario, con try/except
# Nivel 8 de 10
#
# Una API entrega texto en formato JSON; Python lo convierte en
# diccionario con json.loads() (es lo que hace r.json() por dentro).
#
# Con el texto de la prueba:
#   - Convertirlo a diccionario y mostrar type() del texto y del
#     resultado.
#   - Mostrar la temperatura.
#   - Cambiar el viento a 12.0 y mostrar el diccionario como texto
#     JSON bien indentado con:
#         json.dumps(datos, ensure_ascii=False, indent=2)
#   - Escribir leer_json_texto(texto): intenta convertir el texto;
#     si no es un JSON válido (json.JSONDecodeError), muestra
#     "JSON inválido:" con el error y devuelve None.
#   - Probarla con un texto mal formado (sobra una coma).
#
# Prueba:
#   texto_json = '{"ciudad": "Córdoba", "actual": {"temperatura": 25.6, "viento": 9.3}}'
#   datos = json.loads(texto_json)
#   print(type(texto_json), type(datos))
#   print(datos["actual"]["temperatura"])
#   datos["actual"]["viento"] = 12.0
#   print(json.dumps(datos, ensure_ascii=False, indent=2))
#   print(leer_json_texto('{"ciudad": "Mendoza",}'))
#
# Resultado esperado:
#   25.6
#   {
#     "ciudad": "Córdoba",
#     "actual": {
#       "temperatura": 25.6,
#       "viento": 12.0
#     }
#   }
#   JSON inválido: Illegal trailing comma before end of object: line 1 column 21 (char 20)
#   None
#
# Pista: el patrón es el mismo del ejemplo 0.C, pero capturando
# json.JSONDecodeError en lugar de FileNotFoundError:
#   try:
#       ...
#   except json.JSONDecodeError as e:
#       ...
# ---------------------------------------------------------------

import json


# ---------------------------------------------------------------
# FUNCIÓN PEDIDA
# ---------------------------------------------------------------
def leer_json_texto(texto):
    """Convierte un texto JSON en diccionario.
    Si el texto no es JSON válido, muestra el error y devuelve None.
    """
    # TODO 1: abrir un bloque try
    try:
        # - dentro: convertir "texto" con json.loads() y devolver el resultado
        return json.loads(texto)
    except json.JSONDecodeError as e:        
        # TODO 2: capturar json.JSONDecodeError como e
        #         - dentro: mostrar "JSON inválido:" junto con el error (e)
        #         - devolver None
        print("JSON inválido")
        return None
        


# ---------------------------------------------------------------
# DATOS DE PRUEBA
# ---------------------------------------------------------------
texto_json = '{"ciudad": "Córdoba", "actual": {"temperatura": 25.6, "viento": 9.3}}'


# ---------------------------------------------------------------
# PRUEBAS (en este orden)
# ---------------------------------------------------------------

# 1. Convertir el texto a diccionario
# TODO: datos = json.loads(...)
datos = leer_json_texto(texto_json)
# Mostrar el tipo del texto original y el tipo del resultado
# TODO: print(type(...), type(...))
print(type(texto_json), type(datos))

# 2. Mostrar la temperatura (entrar de afuera hacia adentro)
# Resultado esperado:
#   25.6
#   {
#     "ciudad": "Córdoba",
#     "actual": {
#       "temperatura": 25.6,
#       "viento": 12.0
#     }
#   }
datos_temperatura = datos.get("actual").get("temperatura")
print(f"{datos_temperatura}\n{json.dumps(datos, ensure_ascii=False, indent=2)}")
# TODO: print(...)

# 3. Cambiar el viento a 12.0 dentro de "actual"
# TODO: asignación al diccionario interno
datos["actual"]["viento"] = 12.0
# Mostrar el diccionario como texto JSON indentado
print(f"{json.dumps(datos, ensure_ascii=False, indent=2)}")

# 4. Probar leer_json_texto con un texto mal formado (sobra una coma)
texto_json_2 = '{"ciudad": "Córdoba",, "actual": {"temperatura": 25.6, "viento": 9.3}}'
datos_2 = leer_json_texto(texto_json_2)
# TODO: print(leer_json_texto(...))