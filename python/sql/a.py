import sqlite3

db = sqlite3.connect("test.db", isolation_level=None)


# 命令を実行
db.execute("""
    CREATE TABLE Fruit (
        id INTEGER,
        name VARCHAR(20),
        price INTEGER
    );
""")


# 命令を実行
db.execute("""
    INSERT INTO Fruit VALUES (
        1,
        'banana',
        138
    )
""")


# レコードの表示
for row in db.execute("SELECT * FROM Fruit"):
    print(row)

db.close()
