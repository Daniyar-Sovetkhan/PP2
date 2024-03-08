#1
import os

def list_directories_files(path):
    print("Директории:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    print("\nФайлы:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)
    print("\nВсе директории и файлы:")
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            print(os.path.join(root, dir_name))
        for file_name in files:
            print(os.path.join(root, file_name))

# Пример использования
path = "/путь/к/директории"
list_directories_files(path)

#2
import os

def check_path_access(path):
    print(f"Путь: {path}")
    print(f"Существует: {os.path.exists(path)}")
    print(f"Читаемый: {os.access(path, os.R_OK)}")
    print(f"Записываемый: {os.access(path, os.W_OK)}")
    print(f"Исполняемый: {os.access(path, os.X_OK)}")

# Пример использования
path = "/путь/к/вашему/файлу_или_директории"
check_path_access(path)

#3
import os

def path_info(path):
    if os.path.exists(path):
        print(f"Путь '{path}' существует.")
        print(f"Директория: {os.path.dirname(path)}")
        print(f"Имя файла: {os.path.basename(path)}")
    else:
        print(f"Путь '{path}' не существует.")

# Пример использования
path = "/путь/к/вашему/файлу_или_директории"
path_info(path)

#4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

# Пример использования
file_path = "/путь/к/вашему/файлу.txt"
print(f"Количество строк: {count_lines(file_path)}")

#5
def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

# Пример использования
file_path = "/путь/к/вашему/файлу.txt"
data = ['элемент1', 'элемент2', 'элемент3']
write_list_to_file(file_path, data)

#6
import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_name = letter + '.txt'
        with open(file_name, 'w') as file:
            pass  # создает пустой файл

# Пример использования
generate_text_files()

#7
def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        with open(destination_path, 'w') as destination_file:
            for line in source_file:
                destination_file.write(line)

# Пример использования
source_path = "/путь/к/исходному/файлу.txt"
destination_path = "/путь/к/целевому/файлу.txt"
copy_file(source_path, destination_path)

#8
import os

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Файл '{file_path}' успешно удален.")
    else:
        print(f"Файл '{file_path}' не существует.")

# Пример использования
file_path = "/путь/к/вашему/файлу.txt"
delete_file(file_path)
