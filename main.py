from functions import *


def main():
    print('''Welcome to Groccery Shopping Center''')

    while True:
        choice = get_user_choice()

        if choice == 1:
            display_available_products()
        elif choice == 2:
            add_to_cart()
        elif choice == 3:
            exit_program()


if __name__ == "__main__":
    main()
