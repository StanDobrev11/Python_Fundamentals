sequence = input()

count = 0
current_result = ""
final_result = ''
unique_symbols = set()
for idx, symbol in enumerate(sequence):
    if idx < len(sequence) - 1:
        if sequence[idx].isdigit() and sequence[idx + 1].isdigit():
            multiplier = int(sequence[idx] + sequence[idx + 1])
            current_result *= multiplier
            final_result += current_result
            current_result = ''
            continue
    if symbol.isdigit():
        multiplier = int(symbol)
        current_result *= multiplier
        final_result += current_result
        current_result = ''
        continue
    unique_symbols.add(symbol.lower())
    current_result += symbol.upper()

print(f'Unique symbols used: {len(unique_symbols)}')
print(final_result)
