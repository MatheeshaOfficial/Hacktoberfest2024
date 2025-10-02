
import json
import os

FILE = "tasks.json"

if os.path.exists(FILE):
    with open(FILE, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        with open(FILE, "w") as f:
            json.dump(tasks, f)
        print("✅ Task added")
    elif choice == "2":
        print("📋 Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    else:
        break
