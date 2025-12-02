📚 Library Management System

A Python-based Library Management System built using Tkinter for GUI and MySQL for database storage.
This application allows users to manage library members, book records, issue/return details, and more.

🚀 Features
✅ Member Management

Add and store member details

Fields: Member Type, Enrollment No., Name, Address, Mobile No., etc.

✅ Book Management

Select a book from a predefined list

Auto-fill book details such as:

Book ID

Book Title

Author Name

Borrow Date

Due Date

Days on Book

Fine & Final Price

✅ Book Issue System

Auto-calculates due date (15 days from issue)

Automatic fine & pricing values

✅ GUI Functions

Clean Tkinter-Based UI

Form Entries & Labels

Book List with Scrollbar

Auto-fill on book selection

Text box section for book details

✅ Database Connectivity

Uses MySQL / PyMySQL to store:

Member data

Book data

Issue records

🖥️ Tech Stack
Component	Technology
GUI	Tkinter
Backend	Python
Database	MySQL
Libraries	tkinter, tkinter.ttk, mysql.connector, pymysql, datetime
📂 Project Structure
LibraryManagement/
│
├── main.py          # Main Tkinter application file
├── README.md        # Project documentation
└── requirements.txt # Required Python modules

🔧 Installation & Setup
1️⃣ Clone This Repository
git clone https://github.com/YourUsername/LibraryManagementSystem.git

2️⃣ Install Dependencies
pip install pymysql mysql-connector-python

3️⃣ Create MySQL Database
CREATE DATABASE library;
USE library;

4️⃣ Run the Application
python main.py

📸 Screenshots

(Add your app screenshots here)

📝 How Book Selection Works

When you click any book in the list (e.g., Python, DBMS, HTML),
it automatically fills the fields:

✔ Book ID
✔ Title
✔ Author
✔ Borrow Date & Due Date
✔ Fine, Price

All done via the selectbook() function.

✨ Future Enhancements

Search bar for books

Login authentication

Export data to Excel

Dark mode support

Fully dynamic book list stored in MySQL

🤝 Contributing

Contributions are welcome. Feel free to fork the repo and submit a pull request.

📞 Contact

Developer: Ayush
For project help or modifications, feel free to message.
