import re

pattern = r'w{3}\.[a-zA-Z0-9\-]+\.[a-z]+((\.[a-z]+)?)+'

text = input()
result = []

while text:
    found_domain = re.finditer(pattern, text)
    found_domain = [domain.group() for domain in found_domain]
    # if len(found_domain) > 0:
    #     for domain in found_domain:
    #         result.append(domain)
    if found_domain:
        result.extend(found_domain)

    text = input()

for domain in result:
    print(domain)
