import psycopg2


def create_session(func):
    def wrapper(**kwargs):
        conn = psycopg2.connect()
        cour = conn.cursor()
        return func(**kwargs, cour=cour, conn=conn)
    return wrapper



@create_session
def create_table(cour=None, conn=None):
    cour.execute("""
        CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY key,
            name VARCHAR(24)
        ); 
    """)
    conn.commit()

create_table()
