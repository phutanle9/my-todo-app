import os

FILEPATH = "todos.txt"

# Ensure that the file exists, and if not, create it
def ensure_file_exists(filepath=FILEPATH):
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            file.write("")  # Create an empty file if it doesn't exist

# Function to read the todos from the file
def get_todos(filepath=FILEPATH):
    ensure_file_exists(filepath)  # Ensure the file exists before reading
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return [todo.strip() for todo in todos_local]  # Strip newlines from each todo

# Function to write the todos to the file
def write_todos(todos_arg, filepath=FILEPATH):
    ensure_file_exists(filepath)  # Ensure the file exists before writing
    with open(filepath, 'w') as file:
        file.writelines([todo + '\n' for todo in todos_arg])  # Add newline after each todo

# This block only runs if the script is executed directly
if __name__ == "__main__":
    print("Hello")
    todos = get_todos()
    print("Todos:", todos)
