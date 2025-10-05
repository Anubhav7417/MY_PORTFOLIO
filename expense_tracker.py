import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense():
    try:
        amount = float(input("Amount: ₹"))
        category = input("Category (e.g., food, transport): ").strip()
        description = input("Description (optional): ").strip()
        date_str = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()
        if not date_str:
            date_str = datetime.now().strftime("%Y-%m-%d")
        else:
            datetime.strptime(date_str, "%Y-%m-%d")  # validate format

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date_str
        }

        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        print("✅ Expense added!\n")
    except ValueError:
        print("❌ Invalid input. Please try again.\n")

def view_expenses(show_index=True):
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.\n")
        return []
    for idx, e in enumerate(expenses, start=1):
        prefix = f"{idx}. " if show_index else ""
        print(f"{prefix}₹{e['amount']} | {e['category']} | {e['description']} | {e['date']}")
    print()
    return expenses

def view_by_category():
    category = input("Enter category to filter: ").strip()
    expenses = load_expenses()
    filtered = [e for e in expenses if e["category"].lower() == category.lower()]
    if not filtered:
        print(f"No expenses found for category '{category}'.\n")
        return
    total = sum(e["amount"] for e in filtered)
    for e in filtered:
        print(f"₹{e['amount']} | {e['description']} | {e['date']}")
    print(f"Total spent on '{category}': ₹{total:.2f}\n")

def show_report():
    expenses = load_expenses()
    if not expenses:
        print("No data to report.\n")
        return
    total = sum(e["amount"] for e in expenses)
    by_category = {}
    for e in expenses:
        cat = e["category"]
        by_category[cat] = by_category.get(cat, 0) + e["amount"]
    
    print(f"📊 Total Spent: ₹{total:.2f}")
    print("By Category:")
    for cat, amt in by_category.items():
        print(f"  {cat}: ₹{amt:.2f}")
    print()

def delete_expense():
    expenses = view_expenses()
    if not expenses:
        return
    try:
        index = int(input("Enter the number of the expense to delete: "))
        if 1 <= index <= len(expenses):
            removed = expenses.pop(index - 1)
            save_expenses(expenses)
            print(f"✅ Deleted: ₹{removed['amount']} | {removed['category']} | {removed['date']}\n")
        else:
            print("❌ Invalid number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def edit_expense():
    expenses = view_expenses()
    if not expenses:
        return
    try:
        index = int(input("Enter the number of the expense to edit: "))
        if 1 <= index <= len(expenses):
            e = expenses[index - 1]
            print("Leave a field empty to keep the current value.")
            new_amount = input(f"New amount (₹{e['amount']}): ").strip()
            new_category = input(f"New category ({e['category']}): ").strip()
            new_description = input(f"New description ({e['description']}): ").strip()
            new_date = input(f"New date ({e['date']}) [YYYY-MM-DD]: ").strip()

            if new_amount:
                try:
                    e["amount"] = float(new_amount)
                except ValueError:
                    print("❌ Invalid amount. Keeping the old value.")
            if new_category:
                e["category"] = new_category
            if new_description:
                e["description"] = new_description
            if new_date:
                try:
                    datetime.strptime(new_date, "%Y-%m-%d")
                    e["date"] = new_date
                except ValueError:
                    print("❌ Invalid date format. Keeping the old value.")

            expenses[index - 1] = e
            save_expenses(expenses)
            print("✅ Expense updated!\n")
        else:
            print("❌ Invalid number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def menu():
    while True:
        print("📒 Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Show Report")
        print("5. Delete Expense")
        print("6. Edit Expense")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            show_report()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            edit_expense()
        elif choice == '7':
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, try again.\n")

if __name__ == "__main__":
    menu()
