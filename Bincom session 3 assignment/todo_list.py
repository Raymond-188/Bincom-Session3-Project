import psycopg2
from config import config

# Function to create a connection to the database


def create_connection():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return connection

# Function to add a task to the database


def add_task(task):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todo_list (description, completed) VALUES (%s, %s)",
                   (task, False))
    connection.commit()
    cursor.close()
    connection.close()

# Function to retrieve all tasks from the database


def show_tasks():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, description, completed FROM todo_list")
    todo_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return todo_list

# Function to mark a task as done in the database


def mark_task_as_done(task_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE todo_list SET completed = TRUE WHERE id = %s", (task_id,))
    connection.commit()
    cursor.close()
    connection.close()

# Function to delete a task from the database


def delete_task(task_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todo_list WHERE id = %s", (task_id,))
    connection.commit()
    cursor.close()
    connection.close()


def main():
    while True:
        print("\n____ ☑ Simple Todo App _____")
        print("Select only Task Id (1 , 2 0r 3)to perform your task! ")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
            print("Task added!")

        elif choice == '2':
            todo_list = show_tasks()
            print("\nTasks:")
            for task in todo_list:
                status = "Done" if task[2] else "Not Done"
                print(f"{task[0]}. {task[1]} - {status}")

        elif choice == '3':
            task_id = int(input("Enter the task number to mark as done: "))
            mark_task_as_done(task_id)
            print("Task marked as done!")

        elif choice == '4':
            task_id = int(input("Enter the task number to delete: "))
            delete_task(task_id)
            print("Task deleted!")

        elif choice == '5':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
