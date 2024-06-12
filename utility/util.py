from data import email_list
from table import print_table_body, print_table_header

def display_menu() -> None:
    print("======| Email Managemenet System |=========")
    print("1. Display all email")
    print("2. Add new email subcriber")
    print("3. Remove email subcriber") 
    print("4. Send email to all subscriber")
    print("0. Exit")
    print("================================")

def display_all_email() -> None:
    print("======| All Email  Subcriber |=========")
    print_table_header()
    for email, username in email_list:
        print_table_body(email, username)
    print("================================")
    
def add_new_email_subcriber() -> None:
    print("======| All Email  Subcriber |=========")
    email_input = input("Enter Email:")
    username_input = input("Enter username:")
    for email, username in email_list:
        if email_input == email:
            print("Enter realdy exit!")
            return
    email_list.add((email_input, username_input))
    print("Enter added successflly!")
 


def remove_email_subcriber() -> None:
    print("======| Remove Email Subcriber |=======")
    email_input = input("Enter Email:")
   
    for email, username in email_list:
        if email_input == email:
            email_list.remove((email,username))
            print("Email removed successfully")
            return
        print("Email not found")

def send_email_to_all_subcriber() -> None:
    print("======| Send Email Subcriber |=======")
    subject = input("Enter email subject: ")
    content = input("Enter email content: ")
    domain_email = "openvai-support@openvai.com"
    for email, _ in email_list:
        send_email(domain_email, email, subject, content)


def send_email(from_email, to_email, subject, content) -> None:
    print("------------------------------------------")
    print("From:", from_email)
    print("To:", to_email)
    print("Subject:", subject)
    print("------------------------------------------")
    print(content)

send_email_to_all_subcriber()




   
    
