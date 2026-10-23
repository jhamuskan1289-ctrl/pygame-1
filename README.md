# pygame-1

# To-Do List App 📝

A beginner-friendly command-line To-Do List application built using Python. This project helps users manage their daily tasks and practice fundamental Python programming concepts.

## Features

- **Add Tasks:** Add new tasks to your to-do list.
- **View Tasks:** Display all tasks with their completion status.
- **Mark Tasks as Done:** Mark a task as completed.
- **Delete Tasks:** Remove tasks from the list.
- **Input Validation:** Handle invalid numeric inputs using exception handling.

## Technologies Used

- Python 3
- Built-in Python data structures and functions

## Concepts Practiced

- Lists and dictionaries
- Functions
- `if/else` conditional statements
- `for` loops and `enumerate()`
- User input with `input()`
- List methods such as `append()` and `pop()`
- Exception handling using `try/except`
- F-strings and conditional expressions

## How to Run

1. Install Python 3 if it is not already installed.
2. Clone this repository or download the project files.
3. Open a terminal in the project directory.
4. Run the Python file:

   ```bash
   python todo.py
   ```

   Replace `todo.py` with your actual Python filename if it is different.

## How It Works

Tasks are stored in a Python list. Each task is represented by a dictionary containing its name and completion status.

Example:

```python
{"task": "Study Python", "done": False}
```

The application uses functions to perform different task-management operations.

## Future Improvements

- Add an interactive menu loop.
- Allow users to repeatedly perform operations until they choose Exit.
- Save tasks to a file so they persist after the program closes.
- Add task editing functionality.
- Improve input validation and user experience.

## Learning Project

This project was created as part of my journey to improve my Python programming skills through hands-on practice.
