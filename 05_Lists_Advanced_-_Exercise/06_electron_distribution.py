number_of_electrons = int(input())

shell = 0
current_shell_list = []
while number_of_electrons > 0:
    shell += 1
    max_electrons_in_current_shell = 2 * (shell ** 2)
    if number_of_electrons >= max_electrons_in_current_shell:
        electrons_in_current_shell = max_electrons_in_current_shell
    else:
        electrons_in_current_shell = number_of_electrons

    current_shell_list.append(electrons_in_current_shell)
    number_of_electrons -= electrons_in_current_shell

print(current_shell_list)
