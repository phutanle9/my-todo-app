import os

# Define the file path
filepath = 'todos.txt'


def get_todos():
    # Check if the file exists, if not create it
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file_local:
            file_local.write("")  # Create an empty file initially

    # Read todos from the file
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()

    # Clean up newlines in each todo item
    return [todo.strip() for todo in todos]


def write_todos(todos):
    # Write todos to the file
    with open(filepath, 'w') as file_local:
        for todo in todos:
            file_local.write(todo + "\n")
