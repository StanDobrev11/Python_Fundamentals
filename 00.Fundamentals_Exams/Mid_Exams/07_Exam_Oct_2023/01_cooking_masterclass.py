from math import ceil
from decimal import Decimal


budget = Decimal(input())
students = Decimal(input())
flour_price = Decimal(input())
egg_price = Decimal(input())
apron_price = Decimal(input())

flour = Decimal(1)
eggs = Decimal(10)
apron = Decimal(1)

ttl_flour = flour * students
ttl_flour -= ttl_flour // 5

ttl_eggs = Decimal(eggs * students)
ttl_aprons = ceil(apron * students * Decimal('1.2'))


for_eggs = Decimal(ttl_eggs * egg_price)
for_apron = Decimal(ttl_aprons * apron_price)
for_flour = Decimal(ttl_flour * flour_price)

total_cost = for_flour + for_apron + for_eggs

money_needed = total_cost - budget


if budget >= total_cost:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    print(f"{money_needed:.2f}$ more needed.")

"""
50
2
1.0
0.10
10.0

100
25
4.0
1.0
6.0

946
19
12.05
0.42
27.89
"""
