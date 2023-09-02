def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


data_type = input()
data_value = input()
if data_type == "int":
    data_value = int(data_value)
    print(data_value * 2)
elif data_type == "real":
    data_value = float(data_value)
    print(f"{data_value * 1.5 :.2f}")
else:
    data_value = str(data_value)
    print(f"${data_value}$")
