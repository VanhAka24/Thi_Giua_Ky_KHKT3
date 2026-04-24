import os

def manage_todo_list():
    tasks = []
    while True:
        task = input("Nhập công việc (Enter để dừng): ").strip()
        if not task:
            break
        tasks.append(task)
        
    if tasks:
        with open("todo_list.txt", "w", encoding="utf-8") as file:
            for i, task in enumerate(tasks, start=1):
                entry = f"{i}. {task}"
                print(entry)
                file.write(entry + "\n")

if __name__ == "__main__":
    manage_todo_list()