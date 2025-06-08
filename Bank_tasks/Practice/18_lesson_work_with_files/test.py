file = open('data.txt', 'r')
head = file.readline()
body = file.readlines()

# print(head)
# print(body)
max_r = -1000
max_m = -1000
max_i = -1000
print(body)
for i in body:
    r = int(i.split(',')[0].replace("\n", "").strip())
    m = int(i.split(',')[1].replace("\n", "").strip())
    info = int(i.split(',')[2].replace("\n", "").strip())
    if r > max_r:
        max_r = r
    if m > max_m:
        max_m = m
    if info > max_i:
        max_i = info
print(max_r,max_m, max_i)
