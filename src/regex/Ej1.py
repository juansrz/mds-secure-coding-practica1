import sys
import re

line = sys.stdin.readline().strip()

pattern = r"\b\d{4}\b"

years = re.findall(pattern, line)

for year in years:
    print(year)
