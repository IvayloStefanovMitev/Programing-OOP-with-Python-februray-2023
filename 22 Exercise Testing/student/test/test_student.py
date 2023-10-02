from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Guy1")
        self.student_with_course = Student("Guy2", {"some course": ["some note"]})

    def test_initialisation(self):
        self.assertEqual("Guy1", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"some course": ["some note"]}, self.student_with_course.courses)

    def test_enroll_with_already_added_course_and_notes_update(self):
       result = self.student_with_course.enroll("some course", ["new note"])
       self.assertEqual("new note", self.student_with_course.courses["some course"][1])
       self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_add_course_with_notes_with_empty_str(self):
        result = self.student.enroll("new course", ["new note"])
        self.assertEqual("new note", self.student.courses["new course"][0])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_course_with_notes_with_y(self):
        result = self.student.enroll("new course", ["new note"], "Y")
        self.assertEqual("new note", self.student.courses["new course"][0])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_course_with_notes(self):
        result = self.student.enroll("new course", ["new note"], "N")
        self.assertEqual(0, len(self.student.courses["new course"]))
        self.assertEqual("Course has been added.", result)

    def test_add_notes_for_existing_course(self):
        result = self.student_with_course.add_notes("some course", "new note")
        self.assertEqual("new note", self.student_with_course.courses["some course"][-1])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("some course", "some note")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_for_existing_course(self):
        result = self.student_with_course.leave_course("some course")
        self.assertEqual({}, self.student_with_course.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_for_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_course.leave_course("new course")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()