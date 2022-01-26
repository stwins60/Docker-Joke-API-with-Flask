import sqlite3 as sql



joke_db = sql.connect('joke.db', check_same_thread=False)
cursor = joke_db.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS jokes(
        id INTEGER PRIMARY KEY,
        type TEXT,
        setup TEXT,
        punchline TEXT
    )""")

    print('Table created')

def add_joke(id, type, setup, punchline):
    cursor.execute("""INSERT or REPLACE INTO jokes(id, type, setup, punchline)
        VALUES(?, ?, ?, ?)""", (id, type, setup, punchline))
    joke_db.commit()
    # print('Joke added')

def get_all_jokes():
    cursor.execute("""SELECT * FROM jokes""")
    jokes = cursor.fetchall()
    columns = cursor.description
    # print(columns)

    data = []
    for joke in jokes:
        data.append({
            'id': joke[0],
            'type': joke[1],
            'setup': joke[2],
            'punchline': joke[3]
        })
    return data

def get_random_joke():
    cursor.execute("""SELECT * FROM jokes ORDER BY RANDOM() LIMIT 1""")
    joke = cursor.fetchone()
    data = []
    data.append({
        'id': joke[0],
        'type': joke[1],
        'setup': joke[2],
        'punchline': joke[3]
    })
    return data
def delete_joke(id):
    cursor.execute("""DELETE FROM jokes WHERE id = ?""", (id,))
    joke_db.commit()
    print('Joke deleted')