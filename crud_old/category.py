from .engine import create_session


class CRUDCategory:

    @staticmethod
    @create_session
    def add(name: str, cour=None, conn=None) -> None:
        cour.execute("""
            INSERT INTO categories(name)
            VALUES(?);
        """, (name,))
        #conn.commit()

    @staticmethod
    @create_session
    def get(category_id: int, cour=None, conn=None) -> tuple:
        cour.execute("""
                    SELECT * FROM categories
                    WHERE id =?;
                    
        """, (category_id,))
        return cour.fetchone()


# CRUDCategory.add(name="Полки")
#print(CRUDCategory.get(category_id=2))

'''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        email TEXT UNIQUE
    );
CREATE TABLE IF NOT EXISTS passports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passport_number TEXT UNIQUE NOT NULL,
        passport_expire_date TEXT NOT NULL,
        user_id INTEGER UNIQUE NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );


'''
