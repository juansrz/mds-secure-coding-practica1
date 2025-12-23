# Metodologías de Desarrollo Seguro – Práctica 1  
## Buenas prácticas de desarrollo, análisis binario, regex y CI con SonarCloud

Práctica de la asignatura **Metodologías de Desarrollo Seguro (URJC)** orientada a aplicar
buenas prácticas de desarrollo seguro, análisis estático de binarios, expresiones
regulares y un flujo básico de integración continua con **SonarCloud** sobre WebGoat.

---

## Estructura del repositorio

```text
.
├─ src/
│  ├─ 1.cpp                   # Ejercicio 1 – C/C++ (CWE-252: unchecked return value)
│  ├─ 1.exe                   # Binario para análisis con Ghidra
│  ├─ 2. VisitCounter.java    # Ejercicio 2 – Java (race condition, CWE-362)
│  ├─ 3.py                    # Ejercicio 3 – Gestión de usuarios y contraseñas (MD5 → bcrypt)
│  ├─ 4.php                   # Ejercicio 4 – Eliminación de eval() y código duplicado
│  └─ regex/                  # Scripts Python con soluciones a los ejercicios de expresiones regulares
│      ├─ Ej1.py              # Años (4 dígitos)
│      ├─ Ej2.py              # Matrículas españolas con prefijo opcional
│      ├─ Ej3.py              # Conversión de fechas YYYY-MM-DD → DD.MM.YYYY
│      ├─ Ej4.py              # Correos URJC (alumnos/profesores)
│      ├─ Ej5.py            # Direcciones postales (calle, número, CP)
│      └─ Ej6.py            # Parsing de líneas de log a formato estructurado
└─ docs/
   └─ Practica1_MDS.pdf       # Memoria completa de la práctica 
```

> Nota: `1.exe` es el ejecutable proporcionado para el ejercicio de análisis
> con Ghidra.

---

## 1. Buenas prácticas de desarrollo (Ejercicios 1–4)

### `1.cpp` – CWE-252: Unchecked Return Value

Programa en C/C++ que calcula el área de un rectángulo leyendo `ancho` y `alto`
desde la entrada estándar.

- **Problema original:** se usaba `scanf` sin comprobar el valor de retorno
  (CWE-252), pudiendo continuar con valores no inicializados si la lectura fallaba.  
- **Solución implementada:** comprobación explícita del valor devuelto por
  `scanf` y gestión del error (mensaje y finalización segura) antes de usar las
  variables.

### `1.exe` – Análisis con Ghidra

Ejecutable asociado al mismo ejercicio:

- Se analiza con **Ghidra** para localizar cadenas en la sección de datos y encontrar
  un *secreto* codificado en hexadecimal que, interpretado como ASCII,
  revela la solución del ejercicio.
- El proceso completo está documentado en `docs/Practica1_MDS.pdf`.

### `2. VisitCounter.java` – CWE-362: Race Condition

Clase Java que mantiene un contador de visitas en un fichero
`visit_count.txt` con varios hilos concurrentes.

- **Problema original:** lectura y escritura concurrente sin sincronización
  en `incrementVisitCount`, lo que provoca condiciones de carrera e
  inconsistencias en el contador (CWE-362).  
- **Solución implementada:** protección de la sección crítica usando
  mecanismos de sincronización (`synchronized`/locks) para garantizar
  que solo un hilo actualice el fichero cada vez.

### `3.py` – Gestión de usuarios y contraseñas (MD5 → bcrypt)

Script en Python para crear usuarios y almacenar contraseñas.

- **Problema original:** uso de **MD5** para hashear contraseñas
  (algoritmo criptográfico débil).  
- **Solución implementada:** sustitución de MD5 por un algoritmo de hash
  resistente a fuerza bruta y diccionario (por ejemplo, `bcrypt`).

### `4.php` – Eliminación de `eval()` y código duplicado

Script PHP que evalúa una operación aritmética.

- **Problema original:** uso de `eval()` sobre una expresión construida,
  asociado a riesgo de code injection (**CWE-95**) y violación de principios
  de diseño como **DRY** y falta de modularidad.  
- **Solución implementada:** eliminación de `eval()` y refactor a operaciones
  directas (multiplicación) con lógica centralizada, mejorando claridad y
  mantenibilidad.

---

## 2. Expresiones regulares (Ej1–Ej6)

Además de la memoria `docs/Practica1_MDS.pdf`, en `src/regex/` se incluyen
scripts en Python que implementan las soluciones a los ejercicios de
**expresiones regulares**, orientados a validación y parsing de datos.

### `Ej1.py` – Detección de años (4 dígitos)

- Utiliza un patrón tipo `\b\d{4}\b` para localizar números de exactamente 4 dígitos,
  interpretados como posibles años.
- Imprime todos los años encontrados en la línea de entrada estándar.

### `Ej2.py` – Matrículas españolas con prefijo opcional

- Reconoce matrículas modernas con 4 dígitos + 3 letras, con prefijo opcional
  `E-` o `E ` (por ejemplo `E-1234 ABC`, `1234ABC`, `1234-ABC`).
- La expresión combina:
  - límite de palabra,
  - prefijo opcional,
  - bloque de 4 dígitos,
  - separador opcional (`-` o espacio),
  - bloque final de 3 letras mayúsculas.

### `Ej3.py` – Transformación de fechas `YYYY-MM-DD → DD.MM.YYYY`

- Usa grupos de captura `(\d{4})-(\d{2})-(\d{2})` para extraer `año`, `mes` y `día`.
- Reordena los grupos en la sustitución para generar `DD.MM.YYYY`.
- Útil para normalizar formatos de fecha entre sistemas o ficheros de log.

### `Ej4.py` – Correos URJC de alumnos y profesores

- Distingue dos formatos de correo:
  - **Alumnos:** `inicial.apellido.año@alumnos.urjc.es`.
  - **Profesores:** `nombre.apellido@urjc.es`.
- En función del patrón que casa, imprime un mensaje formateado indicando si
  se trata de un alumno (con su año de matrícula) o de un profesor.

### `Ej5.py` – Direcciones postales en España

- Reconoce direcciones del estilo `C/ NombreCalle, Número, CP`,
  admitiendo variantes como `Calle` y pequeños cambios en espacios.
- Extrae:
  - nombre de la calle,
  - número,
  - código postal (5 dígitos).
- Reestructura la salida en un formato normalizado, por ejemplo `CP-Calle-Número`.

### `Ej6.py` – Parsing de líneas de log

- Define una expresión regular con **grupos con nombre** (`?P<nivel>`,
  `?P<hilo>`, `?P<clase>`, `?P<mensaje>`) para trocear líneas de log tipo:
  `YYYY-MM-DD ... LEVEL ... --- [thread] class : message`.
- Genera una salida más estructurada, facilitando el análisis posterior de logs en scripts o herramientas externas.

---

## 3. Integración continua con WebGoat + SonarCloud

La tercera parte de la práctica consiste en configurar un flujo de
**Integración Continua (CI)** sobre un fork del proyecto **WebGoat** en GitHub:

- Repositorio: <https://github.com/juansrz/WebGoat>
- Integración con **SonarCloud** para:
  - analizar la calidad del código y vulnerabilidades,
  - detectar problemas como:
    - uso del `PasswordEncoder` por defecto en Spring Security,
    - construcción de consultas SQL concatenando datos de usuario (SQLi).
- Creación de una rama de corrección (por ejemplo `fix/security-vulnerabilities`),
  modificación de código (`BCryptPasswordEncoder`, `PreparedStatement`, etc.),
  y posterior **Pull Request** con un nuevo análisis de SonarCloud que
  pasa el *Quality Gate* sin vulnerabilidades nuevas.

---

