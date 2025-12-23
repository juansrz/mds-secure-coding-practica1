import sys
import re

line = sys.stdin.readline().rstrip('\n')

pattern = re.compile(
    r'([a-z])\.([a-z]{2,})\.(\d{4})@alumnos\.urjc\.es'  # alumno
    r'|'
    r'([a-z]+)\.([a-z]+)@urjc\.es'                     # profesor
)

matches = pattern.finditer(line)

for match in matches:
    if match.group(1) is not None:
        apellido = match.group(2)
        año = match.group(3)
        print(f"alumno {apellido} matriculado en {año}")
    else:
        nombre = match.group(4)
        apellido = match.group(5)
        print(f"profesor {nombre} apellido {apellido}")
