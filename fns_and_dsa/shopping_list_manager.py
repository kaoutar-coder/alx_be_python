shopping_list = ['apple', 'oil', 'graps','suger']

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def main():
    shopping_list = ['apple', 'oil', 'graps','suger']

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            shopping_list.append(input("enter the item name to add:  "))
        elif choice == '2':
             shopping_list.remove(input("enter the item name to remove:  "))
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
