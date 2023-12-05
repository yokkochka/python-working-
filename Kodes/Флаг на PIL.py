from PIL import Image
img = Image.new("RGBA", (500, 255))
color = 255, 0, 0, 255

# Боковые полосы флага
for w in range(0, 100):
    for h in range(0, 255):
        img.putpixel((w, h), color)
for w in range(405, 500):
    for h in range(0, 255):
        img.putpixel((w, h), color)

# Каркас
for w in range(250, 255):
    for h in range(20, 230):
        img.putpixel((w, h), color)
for w in range(200, 305):
    for h in range(100, 185):
        img.putpixel((w, h), color)
for w in range(225, 280):
    for h in range(55, 100):
        img.putpixel((w, h), color)
        
# Оформление вехней части рисунка флага

# Нижняя часть
for w in range(220, 225):
    for h in range(50, 90):
        img.putpixel((w, h), color)
for w in range(215, 220):
    for h in range(45, 65):
        img.putpixel((w, h), color)
        
for w in range(280, 285):
    for h in range(50, 90):
        img.putpixel((w, h), color)
for w in range(285, 290):
    for h in range(45, 65):
        img.putpixel((w, h), color)

# Верхняя часть
for w in range(235, 240):
    for h in range(50, 55):
        img.putpixel((w, h), color)
for w in range(240, 245):
    for h in range(45, 55):
        img.putpixel((w, h), color)
for w in range(245, 250):
    for h in range(35, 55):
        img.putpixel((w, h), color)
        
for w in range(255, 260):
    for h in range(35, 55):
        img.putpixel((w, h), color)
for w in range(260, 265):
    for h in range(45, 55):
        img.putpixel((w, h), color)
for w in range(265, 270):
    for h in range(50, 55):
        img.putpixel((w, h), color)



# Оформление левой части рисунка флага

for w in range(160, 200):
    for h in range(95, 140):
        img.putpixel((w, h), color)

# Верхушка данной части
for w in range(155, 160):
    for h in range(90, 110):
        img.putpixel((w, h), color)
for w in range(160, 170):
    for h in range(90, 95):
        img.putpixel((w, h), color)
for w in range(150, 155):
    for h in range(130, 135):
        img.putpixel((w, h), color)
for w in range(155, 160):
    for h in range(125, 140):
        img.putpixel((w, h), color)
        
# Правая часть
for w in range(185, 190):
    for h in range(90, 95):
        img.putpixel((w, h), color)
for w in range(190, 195):
    for h in range(80, 95):
        img.putpixel((w, h), color)
for w in range(195, 200):
    for h in range(85, 95):
        img.putpixel((w, h), color)
for w in range(200, 205):
    for h in range(90, 100):
        img.putpixel((w, h), color)
for w in range(205, 210):
    for h in range(95, 100):
        img.putpixel((w, h), color)
for w in range(210, 215):
    for h in range(100, 100):
        img.putpixel((w, h), color)

# Левая часть
for w in range(165, 200):
    for h in range(140, 145):
        img.putpixel((w, h), color)
for w in range(175, 200):
    for h in range(145, 150):
        img.putpixel((w, h), color)
for w in range(180, 200):
    for h in range(150, 155):
        img.putpixel((w, h), color)
for w in range(185, 200):
    for h in range(155, 160):
        img.putpixel((w, h), color)
for w in range(190, 200):
    for h in range(160, 165):
        img.putpixel((w, h), color)


# Оформление правой части рисунка флага

for w in range(305, 345):
    for h in range(95, 140):
        img.putpixel((w, h), color)

# Верхушка данной части
for w in range(345, 350):
    for h in range(90, 110):
        img.putpixel((w, h), color)
for w in range(335, 345):
    for h in range(90, 95):
        img.putpixel((w, h), color)
        
for w in range(350, 355):
    for h in range(130, 135):
        img.putpixel((w, h), color)
for w in range(345, 350):
    for h in range(130, 140):
        img.putpixel((w, h), color)
        
# Левая часть
for w in range(320, 325):
    for h in range(90, 95):
        img.putpixel((w, h), color)
for w in range(315, 320):
    for h in range(80, 95):
        img.putpixel((w, h), color)
for w in range(310, 315):
    for h in range(85, 95):
        img.putpixel((w, h), color)
for w in range(305, 310):
    for h in range(90, 100):
        img.putpixel((w, h), color)
for w in range(300, 305):
    for h in range(95, 100):
        img.putpixel((w, h), color)
for w in range(295, 300):
    for h in range(100, 100):
        img.putpixel((w, h), color)

# Правая часть
for w in range(305, 340):
    for h in range(140, 145):
        img.putpixel((w, h), color)
for w in range(305, 330):
    for h in range(145, 150):
        img.putpixel((w, h), color)
for w in range(305, 325):
    for h in range(150, 155):
        img.putpixel((w, h), color)
for w in range(305, 320):
    for h in range(155, 160):
        img.putpixel((w, h), color)
for w in range(305, 315):
    for h in range(160, 165):
        img.putpixel((w, h), color)
img.show()
