# Attendance Tracking System (OOP)

A console-based Python program that records student class attendance and shows whether each student is eligible to sit the exam. Built with Object-Oriented Programming for **PROG211: Object-Oriented Programming 1** (Individual Assignment: *Real-World Solutions under DPG Standards*), Limkokwing University of Creative Technology, Sierra Leone.

**Author:** Desmond Hinga Kutubu-Koroma
**Domain:** Education

## Problem being addressed

Lecturers need a simple, clear way to record how many classes each student attended and to see quickly who meets the attendance requirement. This program records attendance, calculates each student's percentage, and reports a status of **Eligible** (75% or more) or **Not Eligible**.

## Main features

- Set the total number of classes held for the course
- Add students with the number of classes they attended
- Automatic attendance percentage and eligibility status
- Display every stored record
- Show the total number of students recorded
- Input checking with clear error messages

## Classes and their responsibilities

| Class | Responsibility |
|---|---|
| `Student` | Represents one student. Stores the ID, name and classes attended, and can calculate and display that student's attendance. |
| `AttendanceRegister` | Represents one course register. Stores many `Student` objects in a list and can add and display them. |

The two classes work together: the register stores the students and asks each `Student` object to display itself.

## Data structure used

A **list** (`self.students` inside `AttendanceRegister`) stores multiple `Student` objects. `add_student()` appends a new object to the list, and `display_students()` loops through it to show every record.

## Methods implemented

**Instance methods** (use `self`, work on one student):
- `calculate_percentage(total_classes)`: returns the attendance percentage
- `check_eligibility(total_classes)`: returns "Eligible" or "Not Eligible"
- `display_info(total_classes)`: prints the student's record

**Class method** (uses `cls`, works with the class):
- `get_total_students()` (decorated with `@classmethod`): returns how many `Student` objects have been created, using the shared class attribute `total_students`

**Static methods** (need neither `self` nor `cls`):
- `is_valid_name(name)`: checks that a name is not empty and contains letters only
- `is_valid_attendance(attended, total_classes)`: checks that attendance is between 0 and the total number of classes

**Register methods:** `add_student()` and `display_students()`

## Digital Public Goods (DPG) compliance

1. **Open-source:** The full source code is published in this GitHub repository under the MIT License (see `LICENSE`), so anyone can read, use and adapt it.
2. **Inclusive and accessible design:** The program uses a simple numbered menu, plain-language prompts, and clear error messages. Invalid input (letters instead of numbers, an empty name, attendance out of range, a wrong menu choice) is explained and the program keeps running instead of crashing.
3. **Privacy-respecting:** Only a first/last name and a class count are collected. No sensitive personal data is stored. Student IDs (ST001, ST002, ...) are generated automatically by the program, so no real ID numbers are needed. Sample data in this README is fictional.
4. **Modular and reusable:** Each class and function has one clear job (`Student`, `AttendanceRegister`, and separate helper functions for input). The menu starts only when the file is run directly (`if __name__ == "__main__":`), so the classes can be imported and reused in other programs.

## How to run

1. Install Python 3.
2. Download or clone this repository.
3. In a terminal, go to the project folder and run:

```
python main.py
```

(On some systems use `python3 main.py` or `py main.py`.)

## Example input and output

Values after a prompt (for example `20`) are what the user types.

```
========== Attendance Tracking System ==========
Enter total number of classes: 20

1. Add a student
2. Display all students
3. Show total number of students
4. Exit
Select option: 1
Enter student name: Aminata Kamara
Enter number of classes attended: 18
Aminata Kamara added successfully.

1. Add a student
2. Display all students
3. Show total number of students
4. Exit
Select option: 1
Enter student name: Mohamed Sesay
Enter number of classes attended: 12
Mohamed Sesay added successfully.

1. Add a student
2. Display all students
3. Show total number of students
4. Exit
Select option: 2

********** Programming 1 Attendance Register **********
Total classes held: 20

---------- Attendance Record ----------
ID: ST001
Name: Aminata Kamara
Classes Attended: 18
Percentage: 90.0%
Status: Eligible

---------- Attendance Record ----------
ID: ST002
Name: Mohamed Sesay
Classes Attended: 12
Percentage: 60.0%
Status: Not Eligible

1. Add a student
2. Display all students
3. Show total number of students
4. Exit
Select option: 3
Total students recorded: 2

1. Add a student
2. Display all students
3. Show total number of students
4. Exit
Select option: 4
Attendance record ended. Goodbye!
```

### Example of error handling

```
Enter student name: Mohamed 5esay
Name cannot be empty and must contain letters only.

Enter number of classes attended: abc
Only numbers are allowed. Please try again.
Enter number of classes attended: 25
Classes attended must be between 0 and 20.

Select option: 7
Invalid option. Please choose 1, 2, 3 or 4.
```

## License

Released under the MIT License. See the `LICENSE` file.
