file_path = "file4.txt"

try:
    with open(file_path, "r") as file:  
        data = file.read()  
        print("Содержимое файла:")
        print(data)

except FileNotFoundError:
    print("Файл не найден.")
    
except IOError:
    print("Ошибка ввода-вывода при чтении файла.")
