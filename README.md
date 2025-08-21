# 📞 Contact Book — A Smart CLI Contact Manager

A powerful, user-friendly, and persistent contact book built with Python. Designed with **OOP principles**, **partial editing**, and **robust data persistence** — perfect for managing your contacts from the terminal.

----------------------------------------------------------------------------

## 🚀 Features

✨ **Add Contacts** – Store name, family, and phone  
🔍 **Smart Search** – Find by name, family, or number (case-insensitive & partial match)  
✏️ **Partial Edit** – Change only what you need (e.g., just the phone number)  
🗑️ **Remove Contacts** – Clean up your list  
💾 **Auto-Save & Load** – Data persists between sessions using JSON  
🌍 **Unicode Support** – Works perfectly with Persian, Arabic, and special characters  
🧯 **Error Resilient** – Handles invalid inputs and corrupted files  
⌨️ **Graceful Exit** – Press `Ctrl+C` anytime — your data is saved safely  
🧩 **OOP Design** – Clean separation of `Contact` and `ContactBook` classes

---

## 🖥️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/hasan1369sh/Python-Contact-Book.git

2. Go to the project:
    cd Python-Contact-Book

3. Run it:
    python contact_book.py

"💡 No dependencies. Just pure Python 🐍 "

🎮 Demo: Partial Editing (Game Changer!)
Imagine you only want to update a phone number — no need to retype everything:

Current info: Hasan Sherafat - 09900000000
Leave blank to keep current value.

New first name (current: Hasan): 
New last name (current: Sherafat): 
New phone (current: 09900000000): 09999999999

✅ Contact updated: Hasan Sherafat - 09999999999

"🔥 You only changed the phone — the rest stayed intact. "

🛠️ Data Structure
Each contact is stored in contacts.json as:

    {
        "name": "Hasan",
        "family": "Sherafat",
        "phone": "09999999999"
    }

All data is saved with ensure_ascii=False — full Unicode support guaranteed.

🚧 Future Roadmap
    Add email, address, and birthday fields
    Sort contacts by name
    Export to CSV or vCard

👤 Author
👤 Hasan Sherafat
📧 hasan.sherafat.69@gmail.com
🔗[ GitHub Profile](https://github.com/hasan1369sh/)