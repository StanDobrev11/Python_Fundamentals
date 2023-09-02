import re

pattern = r'(?<=@)#+(?P<valid>[A-Z][A-Za-z0-9]{4,}[A-Z])@#+'

lines = int(input())

for _ in range(lines):
    line = input()
    data_str = re.finditer(pattern, line)
    barcode = ''
    for x in data_str:
        barcode = x.group('valid')

    if not barcode:
        print('Invalid barcode')
    else:
        digits = ''
        for letter in barcode:
            if letter.isdigit():
                digits += letter

        if digits:
            print(f'Product group: {digits}')
        else:
            print('Product group: 00')
