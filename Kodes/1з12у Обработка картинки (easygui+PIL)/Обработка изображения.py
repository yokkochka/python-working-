
import sys

from easygui import *
from PIL import Image, ImageColor, ImageFilter

#  Функция для фильтров улучшения

def filter(image, filter):
    img = Image.open(image)
    if filter == 'SMOOTH':
        out_img = img.filter(ImageFilter.SMOOTH)
        out_img.save('SMOOTH_filter.png')
    elif filter == 'SHARPEN':
        out_img = img.filter(ImageFilter.SHARPEN)
        out_img.save('SHARPEN_filter.png')
    elif filter == 'EMBOSS':
        out_img = img.filter(ImageFilter.EMBOSS)
        out_img.save('EMBOSS_filter.png')
    elif filter == 'DETAIL':
        out_img = img.filter(ImageFilter.DETAIL)
        out_img.save('DETAIL_filter.png')
    msgbox('Операция успешно выполненна')
    out_img.show()
    
#  Функция обрезка

def crop(image, x1, y1, x2, y2):
    img = Image.open(image)
    crop_img = img.crop((x1, y1, x2, y2))
    crop_img.save('cropped.png')
    
    msgbox('Операция успешно выполненна')
    crop_img.show()
    
#  Функция марки

def mark(image, size):
    img = Image.open(image)
    width, height = img.size
    for i in range(10, size):
        for j in range(10, size):
            img.putpixel((i, j), (0, 255, 0))
    
    msgbox('Операция успешно выполненна')
    img.show()
    
#  Функция изменения размера    
    
def resize(image, width, height):
    img = Image.open(image)
    result = img.resize((width, height))
    result.save('result.png')
    
    msgbox('Операция успешно выполненна')
    result.show()    
    
#  Функция конвертации   
    
def conversion(image):
    img = Image.open(image)
    img.save('converted.png', 'png')
    msgbox('Операция успешно выполненна')
    
#  Функция фотофильтра (ч/б, негатив) КАПИПАСТ

def color_filter(filepath, filter):
    img = img = Image.open(filepath)
    out_img = Image.new('RGB', img.size)
    width, height = img.size
    
    if filter == 'Черно-белый фильтр':
        for w in range(width):
            for h in range (height):
                r, g, b = img.getpixel((w, h))
                out_img.putpixel((w, h), ((r + g + b) // 3))
                out_img.save('black_and_white_filter.png')
    elif filter == 'Негатив':
        for w in range(width):
            for h in range (height):
                r, g, b = img.getpixel((w, h))
                out_img.putpixel((w, h), (255 - r, 255 - g, 255 - b))
                out_img.save('negative_filter.png')
    out_img.show()        
        

    
choices_1 = ['Обрезка', 'Цветовой фильтр', 'Изменение размеров', 'Фильтры', 'Метка', 'Конвертация в PNG', 'Закрыть']
choices_0 = ['Открыть картинку', 'Закрыть']
choices_2 = ['SMOOTH', 'SHARPEN', 'EMBOSS', 'DETAIL']
choices_3 = ['Черно-белый фильтр', 'Негатив']

win_0 = buttonbox('Вы открыли графический редактор', choices = choices_0)
if win_0 == choices_0[1]:
    sys.exit()
elif win_0 == choices_0[0]:
    filepath = fileopenbox('Откройте картинку')
    win_1 = buttonbox('Выберите:', choices = choices_1)
    if  win_1 == choices_1[0]:    #  Обрезка
        msg = ''
        title = ''
        fieldNames = ['x1', 'y1', 'x2', 'y2']
        fieldValues = []
        fieldValues = multenterbox(msg, title, fieldNames)
        crop(filepath, int(fieldValues[0]), int(fieldValues[1]), int(fieldValues[2]), int(fieldValues[3]))
    
    elif win_1 == choices_1[1]:    #  Цветовой фильтр
        win_2 = buttonbox('Выберите фильтер:', choices = choices_2)
        filter(filepath, win_2)
        
    elif win_1 == choices_1[2]:    #  Изменения размеров
        msg = ''
        title = ''
        fieldNames = ['w', 'h']
        fieldValues = []
        fieldValues = multenterbox(msg, title, fieldNames)
        resize(filepath, int(fieldValues[0]), int(fieldValues[1]))
        
    elif win_1 == choices_1[3]:    #  Фильтры
        win_3 = buttonbox('Выберите:', choices = choices_3)
        color_filter(filepath, win_3)
        
    elif win_1 == choices_1[4]:    #  Метка
        size_mark = enterbox('Введите размер метки')
        mark(filepath, int(size_mark))
        
    elif win_1 == choices_1[5]:    #  конвертация в PNG
        conversion(filepath)
        
    elif win_1 == choices_1[6]:    #  Закрыть
        sys.exit()

