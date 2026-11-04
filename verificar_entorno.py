import importlib
import os
import sys

from dotenv import load_dotenv

load_dotenv()
print(f"Python{sys.version.split()[0]}")

paquetes = ["anthropic","requests","dotenv","pandas","matplotlib","docx","playwright","fastapi","uvicorn"]

faltan = []

for p in paquetes:
    try:
        importlib.import_module(p)
        print(f"[OK] {p}")
    except ImportError:
        print(f"[FALTA] {p}")
        faltan.append(p)

if os.getenv("ANTHROPIC_API_KEY"):
    print("[OK] ANTHROPIC_API_KEY definida")
else:
    print("[FALTA] ANTHROPIC_API_KEY")
    faltan.append("ANTHROPIC_API_KEY")
sys.exit(1 if faltan else 0)