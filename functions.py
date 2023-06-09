from database import product_data
temp_data = product_data.copy()
def get_user_choice():
    print('''
    1: To check available products
    2: To purchase items
    3: exit
    ''')
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid choice")
        choice=None
    return choice

def display_available_products():
    for item, description in product_data.items():
        print(f"{item:20}: {description[0]:20} : {description[1]:20}  : {description[2]:<20}  :  {description[3]}")

def add_to_cart():
    cart = []

    while True:
        option = get_cart_option()

        if option == 1:
            add_item_to_cart(cart)
        elif option == 2:
            remove_item_from_cart(cart)
        elif option == 3:
            print_cart(cart)
        elif option == 4:
            calculate_and_print_bill(cart)
            break
        elif option == 5:
            break

def get_cart_option():
    print('''
    1: To add items
    2: To remove items
    3: To check your cart
    4: To billing
    5: To exit
    ''')
    try:
        option = int(input("Enter your option: "))
    except:
        print("Invalid Choice")
        option=None
    return option

def add_item_to_cart(cart):
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))

    if name in temp_data:
        available_quantity = temp_data[name][3]
        if quantity <= available_quantity:
            cart.append({name: quantity})
            temp_data[name][3] -= quantity  # Update the temporary quantity
            print("Item added to cart")
        else:
            print("Item quantity unavailable")
    else:
        print("Item not found")

def remove_item_from_cart(cart):
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity to remove: "))

    for item in cart:
        if name in item and quantity == item[name]:
            cart.remove(item)
            temp_data[name][3] += quantity  # Update the temporary quantity
            print("Item removed from cart")
            break
        elif name in item and quantity < item[name]:
            item[name] -= quantity
            temp_data[name][3] += quantity  # Update the temporary quantity
            print("Item quantity reduced in cart")
            break
        elif name in item and quantity > item[name]:
            print("Operation is not possible")
            break
    else:
        print("Item not found in cart")

def print_cart(cart):
    print("Items in cart:")
    print(cart)

def calculate_and_print_bill(cart):
    bill = 0

    for items in cart:
        for product in items:
            bill += product_data[product][2] * items[product]


    print(f"Total Bill: {bill}")
    print(".......Thanks for visiting.....")
    product_data.clear()
    product_data.update(temp_data)
def exit_program():
    print("Exiting the program...")
    # Revert the temporary changes made to the quantity in the database

    exit()
