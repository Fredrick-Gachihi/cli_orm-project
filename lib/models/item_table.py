from .connect import conn, cursor
 
class ItemTable:
    
    def __init__(self, id, buyer_id, item, price, stock, seller_id):
        self.id = id
        self.buyer_id = buyer_id
        self.item = item
        self.price = price
        self.stock = stock
        self.seller_id = seller_id
    
    def __repr__(self):
        return f"<item {self.buyer_id} {self.item} {self.price} {self.stock} {self.seller_id}>"
    
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS items;"
        cursor.execute(sql)
        conn.commit

    @classmethod
    def create_table(cls):
        sql ="""
            CREATE TABLE IF NOT EXISTS items(
               name TEXT,
               price REAL,
               in_stock INTEGER 
            )
        """
        cursor.execute(sql)
        conn.commit()
        
    @classmethod
    def update(self):
        sql = """"
            CREATE TABLE buyers(
                id INTEGER PRIMARY KEY,
                email TEXT,
                phone INTEGER,
                location TEXT
            )
        """


