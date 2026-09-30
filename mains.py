from database import conn, cursor
expenses = []

while True:
    print("\n ====== HOSTEL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date: ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description,
        }
        expenses.append(expense)
        cursor.execute(
            "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
            (date, category, amount, description)
        )
        conn.commit()
        print("Expense added successfully!")
        

    elif choice == "2":
        print("\n==== YOUR EXPENSES ====")
        cursor.execute("SELECT * FROM expenses")
        records = cursor.fetchall()
        if len(records) == 0:
            print("No expenses added yet.")
        else:
            for record in records :
                print("ID:", record[0])
                print("Date:", record[1])
                print("Category:", record[2])
                print("Amount:", record[3])
                print("Description:", record[4])
                print("-----------------------")

    elif choice == "3":
        cursor.execute("SELECT  SUM(amount) FROM expenses")
        result = cursor.fetchone()
        total = result[0]     
        if total is None:
            total = 0
        print("Total Expense:", total)

    elif choice == "4":
        cursor.execute("SELECT * FROM expenses")
        records = cursor.fetchall()
        if len(records) == 0:
            print("No expenses to update.")
        else:
            for record in records:
                print("ID:", record[0], "Date:", record[1], "Category:", record[2], "Amount:", record[3], "Description:", record[4])
            number = int(input("Enter expense ID to update: "))
            cursor.execute("SELECT * FROM expenses WHERE id = ?", (number,))
            record = cursor.fetchone()
            if record:
                new_date = input("Enter new date: ")
                new_category = input("Enter new category: ")
                new_amount = float(input("Enter new amount: "))
                new_description = input("Enter new description: ")
                cursor.execute(
                    "UPDATE expenses SET date = ?, category = ?, amount = ?, description = ? WHERE id = ?",
                    (new_date, new_category, new_amount, new_description, number)
                )
                conn.commit()
                print("Expense updated successfully!")
            else:
                print("Invalid expense ID.")

    elif choice == "5":
        cursor.execute("SELECT * FROM expenses")
        records = cursor.fetchall()
        if len(records) == 0:
            print("No expenses to delete.")
        else:
            for record in records:
                print("ID:", record[0], "Date:", record[1], "Category:", record[2], "Amount:", record[3], "Description:", record[4])
            number = int(input("Enter expense ID to delete: "))
            cursor.execute("SELECT * FROM expenses WHERE id = ?", (number,))
            record = cursor.fetchone()
            if record:
                cursor.execute("DELETE FROM expenses WHERE id = ?", (number,))
                conn.commit()
                print("Expense deleted successfully!")
            else:
                print("Invalid expense ID.")

    elif choice == "6":
        print("Exiting Hostel Expense Tracker...")
        break

    else:
        print("Invalid choice. Please try again.")
        