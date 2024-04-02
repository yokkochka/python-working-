
file_path = "file2.txt"
try:
    file = open(file_path, "w")  
    file.write("Hello world!")

    print("Данные успешно записаны в файл.")
    file.close() 

except IOError:
    print("Ошибка ввода-вывода при записи в файл.")
