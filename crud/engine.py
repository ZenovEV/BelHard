import sqlite3


def create_session(func):
    def wrapper(**kwargs):
        conn = sqlite3.connect("db.db")
        cour = conn.cursor()
        return func(**kwargs, cour=cour, conn=conn)
    return wrapper
