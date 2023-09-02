def loading_bar(number):
    number_decimal = number // 10
    if number_decimal < 10:
        graphic = f"{number}% [{'%' * number_decimal}{'.' * (10 - number_decimal)}]"
        print(graphic)
        text = "Still loading..."
        print(text)
    else:
        text = "100% Complete!\n""[%%%%%%%%%%]"
        print(text)


number = int(input())

loading_bar(number)
