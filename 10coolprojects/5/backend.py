import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS BOOK (id INTEGER PRIMARY KEY, title text,author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("insert into book values (NULL, ? , ?, ?, ?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from book")
    return cur.fetchall()
    conn.commit()
    conn.close()


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from book where title=? or author=? or year= ? or isbn= ?",
                (title, author, year, isbn))
    return cur.fetchall()
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from book where id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("update book set title=?, author=?, year=?,isbn=? where id=?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()
# insert("helo", "helo", "helo", "helo")
# print(view())
# print(search(author="helo"))
