import re

a = "A man, a plan, a canal: Panama"

print((re.sub(r'[^a-zA-Z0-9\s]', '', a)).lower().replace(" ", ""))