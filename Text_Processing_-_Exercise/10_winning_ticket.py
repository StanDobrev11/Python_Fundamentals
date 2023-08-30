def check_valid(ticket):
    if len(ticket) == 20:
        return True
    return False


def check_winning_symbols(half, lst, symbol):
    result = ''
    for idx, ch in enumerate(half):
        if ch == symbol:
            result += ch
        else:
            if len(result) == 0:
                continue
            if len(result) >= 6:
                lst.append(result)
            result = ''
        if len(result) == 10:
            lst.append(result)
            continue
        if idx == len(half) - 1 and len(result) >= 6:
            lst.append(result)
    return lst


tickets_list = [x.strip() for x in input().split(',')]
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets_list:
    if check_valid(ticket):
        first_half = ticket[:10]
        second_half = ticket[10:]
        list_symbols_first = []
        list_symbols_second = []
        for sym in winning_symbols:
            if sym not in first_half or sym not in second_half:
                continue
            list_symbols_first = check_winning_symbols(first_half, list_symbols_first, sym)
            list_symbols_second = check_winning_symbols(second_half, list_symbols_second, sym)

        if len(list_symbols_first) == 0 or len(list_symbols_second) == 0:
            print(f'ticket "{ticket}" - no match')
            continue

        min_length = min(len(list_symbols_first[0]), len(list_symbols_second[0]))
        if len(list_symbols_first[0]) == 10 and len(list_symbols_second[0]) == 10:
            print(f'ticket "{ticket}" - {10}{list_symbols_first[0][0]} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {min_length}{list_symbols_first[0][0]}')

    else:
        print('invalid ticket')
