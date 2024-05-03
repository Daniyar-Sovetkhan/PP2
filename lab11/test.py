
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
        next(reader)  # Пропускаем заголовок
        for row in reader:
            first_name, last_name, phone = row
            insert_data(first_name, last_name, phone)

# Функция для ввода данных с консоли
def enter_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    insert_data(first_name, last_name, phone)

# Процедура для вставки нового пользователя по имени и телефону, обновляя телефон, если пользователь уже существует
def insert_or_update_user(name, phone):
    cur.execute("SELECT id FROM phonebook WHERE first_name = %s", (name,))
    existing_user = cur.fetchone()
    if existing_user:
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (phone, existing_user[0]))
        print("User's phone updated successfully.")
    else:
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
        print("New user inserted successfully.")
    conn.commit()

# Процедура для вставки нескольких новых пользователей из списка имени и телефона
def insert_many_users(users):
    invalid_data = []
    for user in users:
        name, phone = user
        if len(phone) != 10 or not phone.isdigit():
            invalid_data.append((name, phone))
        else:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    if invalid_data:
        print("The following data is incorrect and was not inserted:")
        for data in invalid_data:
            print(data)

# Функция для запроса данных из таблицы с пагинацией (по лимиту и смещению)
def query_data_with_pagination(limit, offset):
    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Процедура для удаления данных из таблицы по имени пользователя или номеру телефона
def delete_data_by_name_or_phone(name=None, phone=None):
    if name:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    if phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()

# Вызываем функцию для загрузки данных из CSV файла
upload_csv('/Users/sovetkhandaniyar/Desktop/PP2/lab11/numbers.csv')

# Запрашиваем данные у пользователя
enter_data()

# Пример вызова процедуры для вставки нового пользователя или обновления существующего
insert_or_update_user("John", "1234567890")

# Пример вызова процедуры для вставки нескольких новых пользователей
insert_many_users([("Alice", "2345678901"), ("Bob", "3456789012"), ("Charlie", "4567890123")])

# Пример вызова функции для запроса данных с пагинацией
query_data_with_pagination(5, 0)

# Пример вызова процедуры для удаления данных по имени пользователя
delete_data_by_name_or_phone(name="John")

# Закрытие соединения с базой данных
cur.close()
conn.close()