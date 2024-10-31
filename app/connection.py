import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="system",
    user="postgres",
    password="2404"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM status")

status = cursor.fetchall()

print(status)

cursor.close()
connection.close()