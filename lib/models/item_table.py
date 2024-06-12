from .connect import conn, cursor
 
class items_table:
    
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
    def create_table(cls):
        sql ="""
            CREATE TABLE items(
               id INTEGER PRIMARY KEY,
               buyer_id INT,
               item TEXT,
               stock TEXT,
               seller_id INT 
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


