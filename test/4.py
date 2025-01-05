def min_discomfort(a, b, c, d):
    dop = min(b,d)
    b -= dop
    d -= dop

    a -= (a // 2) * 2
    c -= (c // 2) * 2

    dop = min(c,d)
    c -= dop
    d -= dop

    a -= min(a,b)
    c -= min(b,c)
    d -= min(a,d)
    b -= min(b,c)

    return a + b + c + d

a, b, c, d = map(int, input().split())
print(min_discomfort(a, b, c, d))




