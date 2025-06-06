shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")

for _ in range(5):
    display_menu()

    try:
        menu = int(input("Choose a menu option (1-4): "))
    except ValueError:
        print("Please enter a number between 1 and 4.")
        continue

    if menu == 1:
        new_item = input("Enter the item to add: ")
        shopping_list.append(new_item)

    elif menu == 2:
        old_item = input("What's the item name? ")
        if old_item in shopping_list:
            shopping_list.remove(old_item)
        else:
            print("Item not on the list.")

    elif menu == 3:
        if shopping_list:
            print("Shopping list:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("Shopping list is empty.")

    elif menu == 4:
        print("Exiting...")
        break

    else:
        print("Not a valid menu option. Choose between 1 - 4.")

