import csv
import psycopg2

# Установка соединения с базой данных PostgreSQL
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1234", port="5432")
cur = conn.cursor()

# Создание таблицы phonebook
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone VARCHAR(50)
    )
""")
conn.commit()

# Функция для вставки данных в таблицу
def insert_data(first_name, last_name, phone):
    cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()

# Загрузка данных из CSV файла
def upload_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            first_name, last_name, phone = row
            insert_data(first_name, last_name, phone)

# Функция для ввода данных с консоли
def enter_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    insert_data(first_name, last_name, phone)

# Функция для обновления данных в таблице
def update_data(id, first_name=None, phone=None):
    if first_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE id = %s", (first_name, id))
    if phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (phone, id))
    conn.commit()

# Функция для запроса данных из таблицы
def query_data(filter=None):
    if filter:
        cur.execute("SELECT * FROM phonebook WHERE {}".format(filter))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Функция для удаления данных из таблицы
def delete_data(name=None, phone=None):
    if name:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    if phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()

# Вызываем функцию для загрузки данных из CSV файла
upload_csv(r'/Users/sovetkhandaniyar/Desktop/PP2/lab10/phonebook/numbers.csv')

# Запрашиваем данные у пользователя
enter_data()

# Пример обновления данных (меняем имя)
update_data(1, first_name="DANIYAR")

# Пример запроса данных с фильтром
query_data("first_name = 'DANIYAR'")

# Пример удаления данных (по имени)
delete_data(name="DANIYAR")
# Закрываем соединение с базой данных
cur.close()
conn.close()