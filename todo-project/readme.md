# CLI To-Do List (Python)

A bite‑size command‑line app that lets you manage tasks with four simple commands.

---

## Core Requirements

| Command                       | What it must do                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------- |
| `python todo.py add "task"`   | Append a new task (initially **not** complete).                                     |
| `python todo.py list`         | Print all tasks, numbered, showing a checkbox: ☐ = incomplete, ✓ = done.            |
| `python todo.py done <num>`   | Mark the task with that number as complete.                                         |
| `python todo.py delete <num>` | Remove the task with that number from the list.                                     |

**Persistence:**  
*Tasks must still be there after you quit and rerun the program.*  
Store them in a small JSON file called `tasks.json` in the same folder.

**Help message:**  
If the user types an unknown command or no command, print a short usage guide.

---

## Stretch Goals (optional)

* Coloured output (e.g., green ✓, red ✗).  
* Due dates & automatic sorting.  
* Unit tests with `pytest`.

---

## Getting Started

1. **Clone or download** this repo.  
2. Ensure you have **Python 3.10+** installed.  
3. Run any command, for example:  
   ```bash
   python todo.py add "Write README"
