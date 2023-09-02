software_version = input()

software_version = int("".join(software_version.split('.')))
next_version = software_version + 1
next_version = ".".join(list(str(next_version)))
print(next_version)
