import subprocess
import os

p = subprocess.run(["ping", "lanacion.com"], capture_output=True, encoding="cp850")
# print(p.stdout)

texto = p.stdout

pos_inicio = texto.find("[") + 1
pos_fin = texto.find("]") - 1
final = pos_inicio

print(texto[pos_inicio:pos_fin])