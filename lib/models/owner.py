from .connect import conn, cursor

class owner:
    def __init__(self, id, first_name, last_name, email, phone, username, location):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.username = username
        self.locaion = location

    
    def __repr__(self):
        return f"<item {self.buyer_id} {self.item} {self.price} {self.stock} {self.seller_id}>" 

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE owner(
               id INTEGER PRIMARY key,
               first_name TEXT,
               last_name TEXT,
               email TEXT,
               phone INTEGER,
               username TEXT,
               location TEXT
            )
        """    
    @classmethod
    def drop_table(cls):
        sql = """"
            DROP TABLE IF EXISTS items;
        """

        cursor.execute(sql)
        conn.commit()  

    def save(self):
        sql = """"
            INSERT INTO items(
                item, price, stock
            )VALUES (?, ?, ?)
        """ 

        cursor.execute(
            sql,
            (
                self.item,
                self.price,
                self.stock,
            ),
        ) 
        conn.commit()
        self.id = cursor.lastrowid