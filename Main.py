# Attendance Tracking System (OOP version)
# Domain: Education
# Stage 3: class method, static methods, tuple summary and an interactive menu


class Student:
    """Blueprint for one student's attendance information."""

    total_students = 0  # class attribute: shared by ALL Student objects

    def __init__(self, student_id, name, classes_attended):
        # Attributes: the data every Student object stores
        self.student_id = student_id
        self.name = name
        self.classes_attended = classes_attended
        Student.total_students += 1  # every new student increases the count

    # ---------- Instance methods (use self: work on ONE student) ----------
    def calculate_percentage(self, total_classes):
        """Return this student's attendance percentage."""
        return (self.classes_attended / total_classes) * 100

    def check_eligibility(self, total_classes):
        """A student needs 75% or more to be eligible."""
        if self.calculate_percentage(total_classes) >= 75:
            return "Eligible"
        return "Not Eligible"

    def get_summary(self, total_classes):
        """Return the percentage and status together as a TUPLE."""
        percentage = self.calculate_percentage(total_classes)
        status = self.check_eligibility(total_classes)
        return (percentage, status)

    def display_info(self, total_classes):
        """Print this student's attendance record."""
        percentage, status = self.get_summary(total_classes)  # unpack the tuple
        print("\n---------- Attendance Record ----------")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Classes Attended: {self.classes_attended}")
        print(f"Percentage: {percentage:.1f}%")
        print(f"Status: {status}")

    # ---------- Class method (uses cls: works with the CLASS) ----------
    @classmethod
    def get_total_students(cls):
        """Return how many Student objects have been created."""
        return cls.total_students

    # ---------- Static methods (no self or cls: simple checks) ----------
    @staticmethod
    def is_valid_name(name):
        """A valid name is not empty and contains letters (and spaces) only."""
        return name != "" and name.replace(" ", "").isalpha()

    @staticmethod
    def is_valid_attendance(attended, total_classes):
        """Attendance must be between 0 and the total number of classes."""
        return 0 <= attended <= total_classes


class AttendanceRegister:
    """Holds many Student objects for one course."""

    def __init__(self, course_name, total_classes):
        self.course_name = course_name
        self.total_classes = total_classes
        self.students = []  # list that stores Student objects

    def add_student(self, student):
        """Add a Student object to the list."""
        self.students.append(student)
        print(f"{student.name} added successfully.")

    def display_students(self):
        """Loop through the list and display every student's record."""
        print(f"\n********** {self.course_name} Attendance Register **********")
        print(f"Total classes held: {self.total_classes}")

        if len(self.students) == 0:
            print("No student records found.")
        else:
            for student in self.students:
                student.display_info(self.total_classes)


# ---------- Helper functions for user input ----------
def read_whole_number(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Only numbers are allowed. Please try again.")


def read_total_classes():
    """Ask for the total number of classes (must be greater than 0)."""
    while True:
        total = read_whole_number("Enter total number of classes: ")
        if total > 0:
            return total
        print("Total classes must be greater than 0.")


def create_student_from_input(register):
    """Ask the user for details, build a Student object and add it."""
    name = input("Enter student name: ").strip()
    if not Student.is_valid_name(name):
        print("Name cannot be empty and must contain letters only.")
        return

    attended = read_whole_number("Enter number of classes attended: ")
    if not Student.is_valid_attendance(attended, register.total_classes):
        print(f"Classes attended must be between 0 and {register.total_classes}.")
        return

    # IDs are generated automatically (ST001, ST002...) so no personal ID is needed
    student_id = f"ST{Student.get_total_students() + 1:03d}"
    student = Student(student_id, name, attended)
    register.add_student(student)


def show_menu():
    print("\n1. Add a student")
    print("2. Display all students")
    print("3. Show total number of students")
    print("4. Exit")


def main():
    print("========== Attendance Tracking System ==========")
    total_classes = read_total_classes()
    register = AttendanceRegister("Programming 1", total_classes)

    running = True
    while running:
        show_menu()
        choice = input("Select option: ").strip()

        if choice == "1":
            create_student_from_input(register)
        elif choice == "2":
            register.display_students()
        elif choice == "3":
            print(f"Total students recorded: {Student.get_total_students()}")
        elif choice == "4":
            print("Attendance record ended. Goodbye!")
            running = False
        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")


# Runs the program only when this file is run directly
if __name__ == "__main__":
    main()