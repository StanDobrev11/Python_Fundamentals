budget = int(input())
while budget >= 0:
    item = input()
    if item == "End":
        print("You bought everything needed.")
        break
    else:
        item = int(item)
    budget -= item
    if budget < 0:
        print("You went in overdraft!")
        break
