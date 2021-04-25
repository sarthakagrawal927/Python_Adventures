import sqlite3


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS BOOK (id INTEGER PRIMARY KEY, title text,author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("insert into book values (NULL, ? , ?, ?, ?)",
                         (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("select * from book")
        return self.cur.fetchall()
        self.conn.commit()

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("select * from book where title=? or author=? or year= ? or isbn= ?",
                         (title, author, year, isbn))
        return self.cur.fetchall()
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("delete from book where id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("update book set title=?, author=?, year=?,isbn=? where id=?",
                         (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# insert("helo", "helo", "helo", "helo")
# print(view())
# print(search(author="helo"))
