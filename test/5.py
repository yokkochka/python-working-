# 17301259

# 1)

# print('x y z w')

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not(not x or y) or z ) or not w) == 0:
#                     print(x, y, z, w)


# 2)

# print('x y z w')

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not(not w or y) or x) or not z) == 0:
#                     print(x, y, z, w)



# 3)

# print('x y z w')

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x or not y) and not (y == z) and not w) == 1:
#                     print(x, y, z, w)



# 4)

# print('x y z w')

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not (x and y) or (not z or w)) and ((w or x) or not y)) == 0:
#                     print(x, y, z, w)


# 5)

# print('x y z w')

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((w or not x) and (w == (not y)) and ((not w) or z)) == 1:
#                     print(x, y, z, w)


#  17495439

# 1)



# d = [y for x in (18, 91, 3, 43, 72, 115) for y in (x, x+0.1, x - 0.1)]
# r=[]
# for a1 in d:
#     for a2 in d:
#         if a2 >= a1 and all((18 <= x <= 91) <= ((not(3 <= x <= 43)) <= (((not(72 <= x <= 115)) and (not (a1 <= x <= a2))) <= (not (18 <= x <= 91)))) for x in d):
#             r += [a2-a1]
# print(round(min(r)))



# print('x y z w')

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F1 =  (x or not y) == (not z or w )
#                 F2 = (not x == y) and (not z or w)
#                 print(x, y, z, w, F1, F2)



# d = [y for x in (130, 171, 150, 185) for y in (x, x + 0.1, x - 0.1)]
# r = []
# for a1 in d:
#     for a2 in d:
#         if a2 >= a1:
#             if all(((130 <= x <= 171) <= (((150 <= x <= 185) and not (a1 <= x <= a2)) <=(not (130 <= x <= 171)))) for x in d):
#                 r += [a2 - a1]
# print(round(min(r)))
