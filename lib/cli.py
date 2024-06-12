def main():
    # print(f"Hello wordld!")
    items = []

choice = 0

while choice != 4:
    print("***OWNER***")
    print("(1) Add an item.")
    print("(2) Check if item is in stock.")
    print("(3) Adjust price")
    print("(4) List all the items.")
    # print("(5) Quit.")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Adiing a item")
        added1 = input("The item : ") 
        added2 = input("The price : ") 
        added3 = input("If is on stock == true ") 
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
        print ("Change the current price.")
        added4 = input("The item: ") 
        added5 = input("set new price: ") 
        items.append([added4 , added5])
        
    elif choice == 4:
        print("Show all items")
        for i in range(len(items)):
            print(items[i])


    else:
        print("Invalid choice.Quiting programe")

        if __name__ == "__main__":
            main()
