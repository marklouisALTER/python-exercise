with open('sample.txt') as file:
    text = file.read()
    length = len(text)

print("The file is {} characters long".format(length))