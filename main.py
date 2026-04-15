from email_sender import send_with_retry
from contact_loader import load_csv
from template_manager import load_templates, apply_template
from history_manager import save_history, view_history
from utils import normalize_email

def main():
    print("===== BULK EMAIL SENDER =====")

    sender = input("Enter your email: ")
    password = input("Enter app password: ")

    contacts = []
    templates = load_templates("data/templates.json")

    while True:
        print("\n1. Load Contacts")
        print("2. Send Emails")
        print("3. View History")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            contacts = load_csv("data/contacts.csv")
            print(f"{len(contacts)} contacts loaded.")

        elif choice == "2":
            if not contacts:
                print("Load contacts first!")
                continue

            print("Available templates:", list(templates.keys()))
            template_name = input("Choose template: ")

            template = templates.get(template_name)
            if not template:
                print("Invalid template!")
                continue

            subject = input("Enter subject: ")

            for contact in contacts:
                email = normalize_email(contact['email'])
                body = apply_template(template, contact)

                success, msg = send_with_retry(sender, password, email, subject, body)

                print(f"{email}: {msg}")
                save_history(email, subject, "Sent" if success else "Failed")

        elif choice == "3":
            view_history()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()