import pytest
from pytest_learning.source import (
    TooManyStudents,
    Classroom,
    Teacher,
    Student,
)  # Replace with the actual module name


# Fixtures
@pytest.fixture
def teacher_snape():
    return Teacher("Severus Snape")


@pytest.fixture
def harry_potter_students():
    return [
        Student(name) for name in ["Harry Potter", "Hermione Granger", "Ron Weasley"]
    ]


@pytest.fixture
def potions_class(teacher_snape, harry_potter_students):
    return Classroom(
        teacher=teacher_snape, students=harry_potter_students, course_title="Potions"
    )


# Test Classroom initialization
def test_classroom_initialization(potions_class, teacher_snape, harry_potter_students):
    assert potions_class.teacher == teacher_snape
    assert potions_class.students == harry_potter_students
    assert potions_class.course_title == "Potions"


# Test adding students
def test_add_student_success(potions_class):
    new_student = Student("Draco Malfoy")
    potions_class.add_student(new_student)
    assert new_student in potions_class.students


def test_add_student_too_many(potions_class):
    # Add students to exceed the limit
    for i in range(7):
        potions_class.add_student(Student(f"Student {i}"))
    with pytest.raises(TooManyStudents):
        potions_class.add_student(Student("Neville Longbottom"))


# Test removing students
@pytest.mark.parametrize(
    "student_name", ["Harry Potter", "Hermione Granger", "Ron Weasley"]
)
def test_remove_student_success(potions_class, student_name):
    removed_student = potions_class.remove_student(student_name)
    assert removed_student.name == student_name
    assert all(student.name != student_name for student in potions_class.students)


def test_remove_student_not_found(potions_class):
    removed_student = potions_class.remove_student("Luna Lovegood")
    assert removed_student is None


# Test changing the teacher
def test_change_teacher(potions_class):
    new_teacher = Teacher("Albus Dumbledore")
    potions_class.change_teacher(new_teacher)
    assert potions_class.teacher == new_teacher
