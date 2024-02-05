from db.database import Database


SQL = "select * from production.brands"
conn = Database.connect()
cursor = conn.cursor()
cursor.execute(SQL)

print(cursor.fetchall())

cursor.close()
