# Metodologías de Desarrollo Seguro – Práctica 1  
## Buenas prácticas de desarrollo, análisis binario, regex y CI con SonarCloud

---

## Estructura del repositorio

```text
.
├─ src/
│  ├─ 1.cpp                  # Ejercicio 1 – C/C++ (CWE-252: unchecked return value)
│  ├─ 1.exe                  # Binario para análisis con Ghidra
│  ├─ 2. VisitCounter.java   # Ejercicio 2 – Java (race condition, CWE-362)
│  ├─ 3.py                   # Ejercicio 3 – Gestión de usuarios y contraseñas (MD5 → bcrypt)
│  └─ 4.php                  # Ejercicio 4 – Eliminación de eval() y código duplicado
└─ docs/
   └─ Practica1_MDS.pdf      # Memoria completa de la práctica 
```
---

## 1. Buenas prácticas de desarrollo (Ejercicio 1)

### `1.cpp` – CWE-252: Unchecked Return Value

Programa en C/C++ que calcula el área de un rectángculo leyendo `ancho` y `alto`
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

## 2. Expresiones regulares (resumen de ejercicios)

La memoria `docs/Practica1_MDS.pdf` incluye una serie de ejercicios de
**expresiones regulares** aplicados a problemas típicos de validación y parsing:

### 2.1 Ejercicio 1 – Detección de años (4 dígitos)

- Patrón base tipo `\b\d{4}\b` para localizar números de exactamente 4 dígitos,
  interpretados como posibles años.
- Útil para extraer fechas de textos sin tener que parsear líneas completas.

### 2.2 Ejercicio 2 – Matrículas españolas con prefijo opcional

- Expresión que soporta el formato de matrícula moderna con 4 dígitos + 3 letras,
  con un posible prefijo `E-` o `E ` (p. ej. `E-1234 ABC` o `1234ABC`).  
- Estructura general: límite de palabra, prefijo opcional, 4 dígitos, separador
  opcional (`-` o espacio) y 3 letras mayúsculas.

### 2.3 Ejercicio 3 – Transformación de fechas `YYYY-MM-DD → DD.MM.YYYY`

- Se capturan año, mes y día con grupos: `(\d{4})-(\d{2})-(\d{2})`.  
- Después se reordena en la sustitución para generar `DD.MM.YYYY`, útil para
  normalizar formatos de fecha entre sistemas.

### 2.4 Ejercicio 4 – Correos URJC de alumnos y profesores

- Dos patrones diferentes:
  - **Alumnos:** inicial, punto, apellido, punto, año de matrícula y dominio
    `@alumnos.urjc.es` (p. ej. `j.suarez2018@alumnos.urjc.es`).  
  - **Profesores:** nombre.apellido con letras minúsculas y dominio `@urjc.es`.  
- Sirve para distinguir automáticamente el tipo de usuario a partir del email.

### 2.5 Ejercicio 5 – Direcciones postales en España

- Regex que reconoce direcciones tipo `C/ NombreCalle, Nº, CP`, admitiendo
  variantes como `Calle` o presencia/ausencia de “Nº” y espacios.  
- Extrae en grupos separados: nombre de la calle, número y código postal
  de 5 dígitos.

### 2.6 Ejercicio 6 – Parsing de líneas de log

- Expresión más compleja que trocea una línea de log en:
  - nivel (`INFO`, `ERROR`, …),
  - hilo,
  - clase o componente,
  - mensaje.  
- Se usan **grupos con nombre** (`?P<nivel>`, `?P<hilo>`, etc.) para construir
  un parser reutilizable en scripts de análisis de logs.

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



