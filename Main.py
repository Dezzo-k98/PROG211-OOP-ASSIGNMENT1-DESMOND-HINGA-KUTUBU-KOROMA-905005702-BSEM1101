# Attendance Tracking System (OOP version)
# Domain: Education
# Stage 2: AttendanceRegister class stores Student objects in a list

TOTAL_CLASSES = 20  # total number of classes held (temporary fixed value for now)


class Student:
    """Blueprint for one student's attendance information."""

    def __init__(self, student_id, name, classes_attended):
        # Attributes: the data every Student object stores
        self.student_id = student_id
        self.name = name
        self.classes_attended = classes_attended

    def calculate_percentage(self, total_classes):
        """Instance method: works with THIS student's data (uses self)."""
        return (self.classes_attended / total_classes) * 100

    def check_eligibility(self, total_classes):
        """Instance method: a student needs 75% or more to be eligible."""
        if self.calculate_percentage(total_classes) >= 75:
            return "Eligible"
        return "Not Eligible"

    def display_info(self, total_classes):
        """Instance method: prints this student's attendance record."""
        print("\n---------- Attendance Record ----------")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Classes Attended: {self.classes_attended}")
        print(f"Percentage: {self.calculate_percentage(total_classes):.1f}%")
        print(f"Status: {self.check_eligibility(total_classes)}")


class AttendanceRegister:
    """Holds many Student objects for one course, like the lecturer's Hospital class."""

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


# Creating objects from the Student class (fictional sample data)
student1 = Student("ST001", "Aminata Kamara", 18)
student2 = Student("ST002", "Mohamed Sesay", 12)
student3 = Student("ST003", "Fatmata Bangura", 15)

# Creating a register object (it will store the Student objects)
register = AttendanceRegister("Programming 1", TOTAL_CLASSES)

# Objects interacting: the register stores and displays the students
register.add_student(student1)
register.add_student(student2)
register.add_student(student3)

register.display_students()