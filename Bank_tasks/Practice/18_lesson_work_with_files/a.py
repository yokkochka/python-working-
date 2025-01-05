
file_path = "file3.txt"
try:
    file = open(file_path, "a") 

    file.write("Add to the end\n")
    print("Данные успешно добавлены в файл.")
    file.close()
    
except IOError:
    print("Ошибка ввода-вывода при добавлении данных в файл.")
