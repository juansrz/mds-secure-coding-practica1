import sys
import re

patron = re.compile(r'''
    ^.*?\s+
    (?P<nivel>\S+)
    \s+\S+\s+---\s+\[
    (?P<hilo>[^\]]+)
    \]\s+
    (?P<clase>[^:]+)
    \s*:\s*
    (?P<mensaje>.*)
    $
''', re.VERBOSE)

for linea in sys.stdin:
    linea = linea.rstrip('\n')
    m = patron.match(linea)
    if m:
        nivel = m.group('nivel')
        hilo = m.group('hilo')
        clase = m.group('clase').strip().rsplit('.', 1)[-1]
        mensaje = m.group('mensaje').strip()
        print("\"{}\",\"{}\",\"{}\",\"{}\"".format(nivel, hilo, clase, mensaje))
