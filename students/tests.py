import random
from django.test import TestCase
from .models import Student


class StudentModelUnitTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            STT=random.randint(10000, 99999),
            Họ='Nguyễn',
            Tên='Đạt',
            Email='abc@gmail.com',
            Khoa='Electric Communication',
            gpa=2.5
        )

    def test_student_model(self):
        data = self.student
        self.assertIsInstance(data, Student)
