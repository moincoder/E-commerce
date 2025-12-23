import re

# Read the file
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# First, revert any escaped quotes back
content = content.replace(r"{% static \'", "{% static '")
content = content.replace(r"\' %}", "' %}")

# Replace src="assets/..." with src="{% static 'assets/...' %}"
content = re.sub(r'src="assets/([^"]+)"', r"src=\"{% static 'assets/\1' %}\"", content)

# Replace href="assets/..." with href="{% static 'assets/...' %}"  
content = re.sub(r'href="assets/([^"]+)"', r"href=\"{% static 'assets/\1' %}\"", content)

# Write back
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed all static asset paths!")
