import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1234", port="5432")
cur = conn.cursor()


def get_all_data():
    cur.execute("SELECT * FROM snakegame ORDER BY user_score DESC")
    rows = cur.fetchall()
    for row in rows:
        print(f"Username = {row[0]} Score = {row[1]} Level = {row[2]}")

get_all_data()