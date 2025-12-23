import sys
import re

line = sys.stdin.readline().rstrip('\n')

pattern = re.compile(r'\b(\d{4})-(\d{2})-(\d{2})\b')

def replace_date(match):
    yyyy = match.group(1)
    mm = match.group(2)
    dd = match.group(3)
    return "{}.{}.{}".format(dd, mm, yyyy)

converted_line = re.sub(pattern, replace_date, line)

print(converted_line)
