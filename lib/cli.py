def main():
    items = []

    choice = 0
    while choice != 5:  
        print("***OWNER***")
        print("(1) Add an item.")
        print("(2) Check if item is in stock.")
        print("(3) Adjust price")
        print("(4) List all the items.")
        print("(5) Quit.")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("Adding an item")
            added1 = input("Enter the item name: ") 
            added2 = input("Enter the price: ") 
            added3 = input("Is it in stock (True/False): ") 
            items.append([added1, added2, added3])

        elif choice == 2:
            print("Checking if the item exists.")
            keyword = input("Enter item to search: ")
            found = False
            for item in items:
                if keyword == item[0]:
                    print("Item found!")
                    found = True
                    break
            if not found:
                print("Item not found.")

        elif choice == 3:
            print("Changing the current price.")
            keyword = input("Enter the item name: ") 
            keyword = input("Enter the new price: ") 
            for item in items:
                if keyword == item[0]:
                    item[1] = keyword
                    print("Price updated.")
                    break
            else:
                print("Item not found.")

        elif choice == 4:
            print("Showing all items")
            for item in items:
                print(item)

        elif choice == 5:
            print("Quitting program.")

        else:
            print("***Invalid choice.***")

if __name__ == "__main__":
    main()