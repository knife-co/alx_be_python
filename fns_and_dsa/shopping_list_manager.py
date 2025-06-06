# Use a loop to continuously display a menu with options to the user until they choose 
# to exit. The menu should offer options to add an item, remove an item, view the list, 
# and exit.
# For adding items, prompt the user for the item name and append it to shopping_list.
# For removing items, ask the user for the item name and remove it from shopping_list. 
# If the item is not found, display a message indicating so.
# To view the list, print each item in shopping_list to the console.
# Ensure your script handles invalid menu choices gracefully.

shopping_list = []

for _ in range(5):
    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")

    menu = int(input("Choose a menu option (1-4): "))

    if menu == 1:
        new_item = input("What's the item name? ")
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

