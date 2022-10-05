from school_schedule.student import Student

def test_new_student():
  # Arrange
  name = "Aminah"
  grade = "Freshman"
  classes = ["Chemistry", "Algebra", "Cooking", "Paint", "Poetry"]

  # Act
  aminah = Student(name, grade, classes)

  # Assert
  assert aminah.name == name
  assert aminah.grade == grade
  assert aminah.classes == classes
  assert len(aminah.classes) == 5

def test_get_num_classes():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting", "Writing"]
    ellis = Student(name, grade, classes)

    # Act
    num_classes = ellis.get_num_classes()

    # Assert
    assert num_classes == 2