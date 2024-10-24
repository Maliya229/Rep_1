from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def AddExpense(self,description,amount):
        date = datetime.now()
        expense = {"description":description, "date":date ,"amount":amount}
        self.expenses.append(expense)
        print(f"{expense} has been added")
    
    def UpdateExpense(self,index,description=None ,amount=None):
        if 0 <= index < len(self.expenses):
            if description:
                self.expenses[index]["description"] = description
            if amount:
                self.expenses[index]["amount"] = amount
            print(f"{self.expenses[index]} has been updated ")
        else:
            print("Invalid input. Could not update")

    def DeleteExpense(self,index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            deleted = self.expenses[index]
            print(f"{deleted} has been deleted")
        else:
            print("Invalid index")

    def ViewExpenses(self):
        print(f"{self.expenses}")

    def Summary(self):
        if not self.expenses:
            print("No expenses")
        else:
            total = 0
            for i in self.expenses:
                total += i["amount"]
            print(f"{total} is the total expense")

    def month_summary(self, month):
        current_year = datetime.now().year
        monthly_expenses = [
            exp for exp in self.expenses if exp["date"].year == current_year and exp["date"].month == month
        ]
        if not monthly_expenses:
            print(f"No monthly expenses for month {month}")
        else:
            total = sum(exp["amount"] for exp in monthly_expenses)
            print(f"Total monthly expenses for the month {month} is ${total}")
            for index, expense in enumerate(monthly_expenses,start = 1):
                date_str = expense["date"].strftime("%Y-%m-%d")
                print(f"{index}.{expense['description']} - ${expense['amount']} - {date_str}")



def main():
    tracker = ExpenseTracker()
    while True:
        print("\nMenu")
        print("1.Add expense")
        print("2.Update expense")
        print("3.Delete expense")
        print("4.View all expenses")
        print("5.View summary of all expenses")
        print("6.View summary of expenses for a certain month")
        print("7.Exit")

        choice = int(input("Enter the number of your choice:"))

        if choice == 1:
            description = input("Enter description of expense: ")
            amount = float(input("Enter amount: "))
            tracker.AddExpense(description,amount)
            
        elif choice == 2:
            index = int(input("Enter the index of the choice you need to update: "))
            description = input("Enter the new description: ")
            amount = float(input("Enter the new amount: "))
            tracker.UpdateExpense(index,description,amount)

        elif choice == 3:
            index = int(input("Enter the index of the choice you need to delete: "))
            tracker.DeleteExpense(index)
        
        elif choice == 4:
            tracker.ViewExpenses()

        elif choice == 5:
            tracker.Summary()
        
        elif choice == 6:
            month = int(input("Enter the number of the month(1-12): "))
            tracker.month_summary(month)
        
        elif choice == 7:
            print("Exiting program")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

