import sqlite3

def create_table():
    conn = sqlite3.connect("shop.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items(name TEXT, price REAL, in_stock INTEGER)''')
    conn.commit()
    conn.close()

def add_item(name, price, in_stock):
    conn = sqlite3.connect("shop.db")
    c = conn.cursor()
    c.execute("INSERT INTO items (name, price, in_stock) VALUES (?, ?, ?)", (name, price, in_stock))
    conn.commit()
    conn.close()

def get_all_items():
    conn = sqlite3.connect("shop.db")
    c = conn.cursor()
    c.execute("SELECT * FROM items")
    items = c.fetchall()
    conn.close()
    return items

def main():
    create_table()

    choice = 0
    while choice != 5:  
        print("***CHOOSE YOUR BEST FIT.***")
        print("(1) Add an item.")
        print("(2) Check if item is in stock.")
        print("(3) Adjust price")
        print("(4) List all the items.")
        print("(5) Quit.")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("Adding an item")
            name = input("Enter the item name: ")
            price = float(input("Enter the price: "))
            in_stock = input("Is it in stock (True/False): ").capitalize() == "True"
            add_item(name, price, in_stock)

        elif choice == 2:
            print("Checking if the item exists.")
            name = input("Enter item to search: ")
            items = get_all_items()
            found = False
            for item in items:
                if name == item[0]:
                    print("Item found!")
                    found = True
                    break
            if not found:
                print("Item not found.")

        elif choice == 3:
            print("Changing the current price.")
            name = input("Enter the item name: ")
            new_price = float(input("Enter the new price: "))
            conn = sqlite3.connect("shop.db")
            c = conn.cursor()
            c.execute("UPDATE items SET price=? WHERE name=?", (new_price, name))
            conn.commit()
            conn.close()
            print("Price updated.")

        elif choice == 4:
            print("Showing all items")
            items = get_all_items()
            for item in items:
                print(item)

        elif choice == 5:
            print("Quitting program.")

        else:
            print("***Invalid choice.***")

if __name__ == "__main__":
    main()