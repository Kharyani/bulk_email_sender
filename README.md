# bulk_email_sender
📌 Project Overview
This is a Python-based CLI application that automates sending bulk emails using SMTP. It allows users to load contacts from a CSV file, use reusable email templates, personalize messages, and track email history.
The project simulates real-world email marketing and notification systems.

🎯 Features


📬 Send bulk emails using SMTP (Gmail)


👥 Load contacts from CSV file


✉️ Use predefined email templates


🧑‍💼 Personalize emails using placeholders:


{name}


{company}




📁 Email history tracking (success/failure logs)


🔁 Retry mechanism for failed emails


🧩 Modular Python code structure


🖥 CLI-based menu system



🗂 Project Structure
bulk_email_sender/│├── main.py├── email_sender.py├── contact_loader.py├── template_manager.py├── history_manager.py├── utils.py│├── data/│   ├── contacts.csv│   ├── templates.json│   ├── history.json

📂 Data Files
📄 contacts.csv
Stores recipient information:
name,email,companyAli,ali@gmail.com,HK AcademySara,sara@gmail.com,TechSoftJohn,john@gmail.com,ABC Ltd

📄 templates.json
Email message templates:
{  "welcome": "Hello {name},\nWelcome to {company}. We are glad to have you!",  "offer": "Hi {name},\nSpecial offer just for you at {company}!"}

📄 history.json
Stores email sending logs:
[]

⚙️ Requirements


Python 3.x


Internet connection


Gmail account with App Password (for SMTP)



🔐 Gmail SMTP Setup
To send emails using Gmail:


Enable 2-Step Verification


Generate App Password


Use:


SMTP Server: smtp.gmail.com


Port: 587




Use App Password instead of normal password



🚀 How to Run
Run the project using:
python main.py

🧭 Menu Options


Load Contacts


Send Emails


View History


Exit



📧 Example Output
ali@gmail.com: Sentsara@gmail.com: Sentjohn@gmail.com: Sent

⚠️ Error Handling


Invalid email format handling


SMTP authentication errors


Retry mechanism for failed emails


File loading error handling



💡 Future Improvements


🖥 GUI version using Tkinter


📎 File attachments support


✨ HTML email templates


⏰ Email scheduling system


📊 Dashboard for analytics



👨‍💻 Author
Student Project – Python Automation System
Developed for learning real-world email automation concepts.

📌 License
This project is for educational purposes only.



Just tell me 👍
