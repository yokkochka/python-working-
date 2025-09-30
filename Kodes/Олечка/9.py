f = open('9.txt', 'r')

cnt = 0

# "1 2 3".split() -> ["1", "2", "3"]
for s in f:
    s = list(map(int, s.split()))
    s.sort()
    # print(s)

    povt = [x for x in s if s.count(x) > 1]
    nepovt = [x for x in s if s.count(x) == 1]

    # print("povt" , povt)
    # print("nepovt", nepovt)

    if len(povt) == 3 and sum(povt)**2 > sum(nepovt)**2:
        cnt += 1
print(cnt)

    