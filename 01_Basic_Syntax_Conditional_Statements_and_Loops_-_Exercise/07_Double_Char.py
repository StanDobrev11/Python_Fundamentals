while True:
    double_string = ""
    string = input()
    if string == "End":
        break
    elif string != "SoftUni":
        for letter in string:
            double_string += letter * 2
        print(double_string)
        