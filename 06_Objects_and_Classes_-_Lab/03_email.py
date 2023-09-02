class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


list_of_mails = []
command_line = input()
while command_line != "Stop":
    elements = command_line.split(" ")
    sender = elements[0]
    receiver = elements[1]
    content = elements[2]
    email = Email(sender, receiver, content)
    list_of_mails.append(email)
    command_line = input()

index_to_print = input()
index_to_print = index_to_print.split(", ")
for index in index_to_print:
    index = int(index)
    list_of_mails[index].is_sent = True

for email in list_of_mails:
    print(email.get_info())
# for i in range(len(list_of_mails)):
#     print(list_of_mails[i].get_info())
