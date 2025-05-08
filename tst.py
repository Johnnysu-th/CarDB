import sqlite3

db = sqlite3.connect("car.db")
cursor = db.cursor()
sql = "Select * from car;"
cursor.execute(sql)
results = cursor.fethall()
print(results)

db.close()