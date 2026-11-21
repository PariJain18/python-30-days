from habit import Habit
from storage import load_habits, save_habits


def main():
    habits = load_habits()

    while True:
        print("\n===== HABIT TRACKER =====")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Mark Completed")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter habit name: ")
            habit = Habit(name)
            habits.append({
                "name": habit.name,
                "completed": habit.completed
            })
            save_habits(habits)
            print("Habit added successfully!")

        elif choice == "2":
            if not habits:
                print("No habits found.")
            else:
                for i, habit in enumerate(habits, start=1):
                    status = "Completed" if habit["completed"] else "Pending"
                    print(f"{i}. {habit['name']} - {status}")

        elif choice == "3":
            if not habits:
                print("No habits found.")
            else:
                for i, habit in enumerate(habits, start=1):
                    print(f"{i}. {habit['name']}")

                try:
                    number = int(input("Enter habit number: "))
                    if 1 <= number <= len(habits):
                        habits[number - 1]["completed"] = True
                        save_habits(habits)
                        print("Habit marked as completed!")
                    else:
                        print("Invalid habit number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Thank you for using Habit Tracker!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()