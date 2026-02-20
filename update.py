import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove description lines in productsData array
content = re.sub(r'\n\s*description:\s*".*?",', '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Descriptions removed!")
