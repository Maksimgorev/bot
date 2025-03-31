import sqlite3

# подключаемся к БД
conn = sqlite3.connect('проект\боты\пользователь.db')
# создаем курсос для БД
cur = conn.cursor()

# создание таблицы
#  IF NOT EXISTS - чтобы не было ошибки при запуске, если такая таблица существует
cur.execute('''CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    description TEXT
);''')
conn.commit()

# заполнение таблицы
# cur.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', ['гитара', 12000, 'акустическая гитара'])
# cur.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', ['барабаны', 91000, 'африканские бараны'])
# cur.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', ['флейта', 7500, 'духовой инстурумент'])
# cur.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', ['скрипка', 74500, 'струнный инструмент'])
# conn.commit() 

# получение данных из таблицы
# cur.execute('SELECT * FROM products')
# data = cur.fetchall() # записываем всё что вернулось с БД
# print(data)