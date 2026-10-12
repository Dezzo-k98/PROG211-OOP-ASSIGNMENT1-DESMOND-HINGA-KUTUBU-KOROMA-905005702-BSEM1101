# Attendance Tracking System (OOP version)
# Domain: Education
# Stage 1: the Student class and objects created from it

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


# Creating objects from the Student class (fictional sample data)
student1 = Student("ST001", "Aminata Kamara", 18)
student2 = Student("ST002", "Mohamed Sesay", 12)
student3 = Student("ST003", "Fatmata Bangura", 15)

# Using the objects
student1.display_info(TOTAL_CLASSES)
student2.display_info(TOTAL_CLASSES)
student3.display_info(TOTAL_CLASSES)