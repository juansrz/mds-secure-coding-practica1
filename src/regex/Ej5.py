import re

regex = (
    r"(?:^|\s)"                                 
    r"(?:C/|Calle)\s+"                          
    r"([A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ]+(?:-[A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ]+)?)"  
    r",?\s*"                                     
    r"(?:[Nn](?:[º°])?\s*)?"                      
    r"(\d+)"                                     
    r",\s*"                                      
    r"(\d{5})"                                   
    r"(?=$|\s|[.,;])"
)

texto = input()

coincidencias = re.findall(regex, texto)

for calle, numero, cp in coincidencias:
    print(f"{cp}-{calle}-{numero}")
