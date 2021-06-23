class NumberListErr(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    data = input("Enter number: ")
    try:
        if data == "stop":
            break
        if not data.isdigit():
            raise NumberListErr("You entered not a number!")
        my_list.append(int(data))
    except NumberListErr as err:
        print(err)
print(my_list)
