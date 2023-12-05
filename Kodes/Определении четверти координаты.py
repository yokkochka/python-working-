x = int(input("Введите координату OX"))
y = int(input("Введите координату OY"))

if (x>0) and (y>0):
    print( "I четверть")
elif (x<0) and (y>0):
    print( "II четверть") 
elif (x<0) and (y<0):
    print( "III четверть") 
elif (x>0) and (y<0):
    print( "IV четверть") 
else:
    print ("Введите координаты без нулевых значений (x и y не должны быть равны 0)")