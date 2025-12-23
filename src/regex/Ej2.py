import re

line = input().strip()

pattern = r'\b(?:E[- ]?)?\d{4}[- ]?[A-Z]{3}\b'

matches = re.findall(pattern, line)

for plate in matches:
    print(plate)

