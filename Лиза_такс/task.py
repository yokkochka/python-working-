# 1

filename = "k7c-6.txt"
with open(filename, 'r') as file:
    content = file.read()

print(content.count("D"))


# 2
string = input("Введите строку типа ‘fgHjKKlpiKJghfJg’: ")
string = string.lower()
print(string)



# 3

filename = "k7c-6.txt"
with open(filename, 'r') as file:
    content = file.read()

count = 0
i = 0
len_str = len(content)
while i < len_str-2:
    if content[i] != content[i+1] and content[i+1] != content[i+2] and content[i+2] != content[i]:
        count += 1
    i += 1

print(count)
