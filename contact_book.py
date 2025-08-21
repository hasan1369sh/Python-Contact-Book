import json
import os


class Contact:
    """نماینده یک مخاطب با ویژگی‌های نام، نام خانوادگی و شماره تلفن"""

    def __init__(self, name, family, phone):
        self.name = name
        self.family = family
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.family} - {self.phone}"

    def __repr__(self):
        return f"Contact(name='{self.name}', family='{self.family}', phone='{self.phone}')"

    def to_dict(self):
        """تبدیل شیء به دیکشنری برای ذخیره در JSON"""
        return {
            "name": self.name,
            "family": self.family,
            "phone": self.phone
        }

    @staticmethod
    def from_dict(data):
        """تبدیل دیکشنری به شیء Contact"""
        return Contact(data["name"], data["family"], data["phone"])


class ContactBook:
    """مدیریت لیست مخاطبین: افزودن، حذف، ویرایش، جستجو و ذخیره"""

    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load()

    def add_contact(self, contact):
        """افزودن یک مخاطب جدید به لیست و ذخیره در فایل"""
        self.contacts.append(contact)
        self.save()
        print(f"✅ Contact '{contact}' added successfully.")

    def remove_contact(self, index):
        """حذف مخاطب بر اساس ایندکس"""
        if 0 <= index < len(self.contacts):
            removed = self.contacts.pop(index)
            self.save()
            print(f"✅ Contact '{removed}' has been removed.")
            return True
        else:
            print("❌ Invalid contact number.")
            return False

    def edit_contact(self, index, new_data):
        """
        ویرایش جزئی یک مخاطب
        new_data: دیکشنری شامل فیلدهایی که می‌خوای عوض کنی، مثلاً {'phone': '0912...'}
        """
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            
            # فقط فیلدهای پر شده رو آپدیت می‌کنیم
            if 'name' in new_data and new_data['name'].strip():
                contact.name = new_data['name'].strip()
            if 'family' in new_data and new_data['family'].strip():
                contact.family = new_data['family'].strip()
            if 'phone' in new_data and new_data['phone'].strip():
                contact.phone = new_data['phone'].strip()

            self.save()
            print(f"✅ Contact updated: {contact}")
            return True
        else:
            print("❌ Invalid contact number.")
            return False

    def search(self, query):
        """
        جستجوی پیشرفته: بررسی بخشی از نام، نام خانوادگی یا شماره تلفن
        بدون توجه به بزرگی/کوچکی حروف
        """
        query = query.lower().strip()
        if not query:
            return []
        results = []
        for contact in self.contacts:
            if (query in contact.name.lower() or
                query in contact.family.lower() or
                query in contact.phone):
                results.append(contact)
        return results

    def display_all(self):
        """نمایش تمام مخاطبین با شماره. اگر لیست خالی باشد، پیام مناسب نمایش داده می‌شود."""
        if not self.contacts:
            print("\n📭 No contacts available.")
            return False
        print("\n📋 Contact List:")
        print("-" * 60)
        for i, contact in enumerate(self.contacts, 1):
            print(f"  {i}. {contact}")
        print("-" * 60)
        return True

    def save(self):
        """ذخیره لیست مخاطبین در فایل JSON با کدگذاری صحیح فارسی"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump([c.to_dict() for c in self.contacts], file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"❌ Error saving file: {e}")

    def load(self):
        """بارگذاری مخاطبین از فایل JSON در صورت وجود فایل"""
        if not os.path.exists(self.filename):
            self.contacts = []
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.contacts = [Contact.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            print("⚠️  Data file is corrupted or unreadable. Starting with an empty list.")
            self.contacts = []


def get_valid_index(book, prompt="Enter contact number: "):
    """
    دریافت یک ایندکس معتبر از کاربر
    اگر لیست خالی باشد یا ایندکس نامعتبر باشد، None برمی‌گردونه
    """
    if not book.display_all():
        return None
    try:
        idx = int(input(f"\n{prompt}")) - 1
        if 0 <= idx < len(book.contacts):
            return idx
        else:
            print("❌ Invalid contact number.")
            return None
    except ValueError:
        print("❌ Please enter a valid number.")
        return None


def show_menu():
    """نمایش منوی اصلی به کاربر"""
    print("\n" + "★" * 50)
    print("               Contact Book")
    print("★" * 50)
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Edit contact")
    print("4. Search contacts (by name, family or phone)")
    print("5. Remove contact")
    print("6. Exit")


def get_choice():
    """دریافت و اعتبارسنجی ورودی کاربر برای انتخاب منو"""
    try:
        return int(input("\n🔢 Enter your choice (1-6): "))
    except ValueError:
        return -1


def main():
    book = ContactBook()

    try:
        while True:
            show_menu()
            choice = get_choice()

            if choice == 1:
                book.display_all()

            elif choice == 2:
                print("\n➕ Adding New Contact:")
                name = input("First name: ").strip()
                family = input("Last name: ").strip()
                phone = input("Phone number: ").strip()

                if not name or not family or not phone:
                    print("❌ All fields are required!")
                    continue

                contact = Contact(name, family, phone)
                book.add_contact(contact)

            elif choice == 3:
                idx = get_valid_index(book, "Enter contact number to edit: ")
                if idx is not None:
                    current = book.contacts[idx]
                    print(f"\nCurrent info: {current}")
                    print("Leave blank to keep current value.")

                    new_name = input(f"New first name (current: {current.name}): ").strip()
                    new_family = input(f"New last name (current: {current.family}): ").strip()
                    new_phone = input(f"New phone (current: {current.phone}): ").strip()

                    # فقط فیلدهایی که تغییر کردن رو ارسال می‌کنیم
                    updates = {}
                    if new_name:
                        updates['name'] = new_name
                    if new_family:
                        updates['family'] = new_family
                    if new_phone:
                        updates['phone'] = new_phone

                    if updates:
                        book.edit_contact(idx, updates)
                    else:
                        print("🔸 No changes made.")

            elif choice == 4:
                query = input("\n🔍 Search query (part of name, family or phone): ").strip()
                if not query:
                    print("❌ Please enter a search term.")
                    continue

                results = book.search(query)
                if results:
                    print(f"\n🎯 Found {len(results)} result(s):")
                    for i, c in enumerate(results, 1):
                        print(f"  {i}. {c}")
                else:
                    print("❌ No contacts found.")

            elif choice == 5:
                idx = get_valid_index(book, "Enter contact number to remove: ")
                if idx is not None:
                    book.remove_contact(idx)

            elif choice == 6:
                print("👋 Goodbye! Your data has been saved.")
                break

            else:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")

    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user (Ctrl+C).")
        print("💾 Saving your contacts before exit...")
        book.save()
        print("✅ Your data has been saved safely.")
        print("👋 Goodbye!")


if __name__ == "__main__":
    main()