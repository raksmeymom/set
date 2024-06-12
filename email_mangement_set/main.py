from utility.util import *
import os

def main():
    while (True):
        display_menu()
        option = int(input("Enter option: "))
        os.system("cls")
        if option ==1:
            display_all_email()
        elif option == 2:
            add_new_email_subcriber()
        elif option == 3:
            remove_email_subcriber()
        elif option == 4:
            send_email_to_all_subcriber()
        elif option == 0:
            print("Enter exit...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
   main()


