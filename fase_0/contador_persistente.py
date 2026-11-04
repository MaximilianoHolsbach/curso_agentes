import json # is a subset of JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data interchange format.

try:
    with open("datos.json", encoding="utf-8") as f:
        datos = json.load(f)
except FileNotFoundError:
    datos = {"visitas": 0} # Si no existe, empezamos de cero

datos["visitas"] = datos.get("visitas", 0) + 1
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)
print("Visitas: ", datos["visitas"])

