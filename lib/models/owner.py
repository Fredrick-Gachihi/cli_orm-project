from .connect import conn, cursor  

class Owner:
    def __init__(self, id, first_name, last_name, email, phone, username, location):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.username = username
        self.location = location  

    def __repr__(self):
        return f"<Current owner {self.id} {self.first_name} {self.last_name} {self.email} {self.phone} {self.username} {self.location}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE owner(
               id INTEGER PRIMARY KEY,
               first_name TEXT,
               last_name TEXT,
               email TEXT,
               phone INTEGER,
               username TEXT,
               location TEXT
            )
        """  
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS owner;
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            INSERT INTO owner(
                first_name, last_name, email, phone, username, location
            ) VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
            self.username,
            self.location,
        ))
        conn.commit()
        self.id = cursor.lastrowid

    def update(self):
        sql = """
            UPDATE owner
            SET first_name=?, last_name=?, email=?, phone=?, username=?, location=?
            WHERE id=?
        """
        cursor.execute(sql, (
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
            self.username,
            self.location,
            self.id,
        ))
        conn.commit()