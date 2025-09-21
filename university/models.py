from django.db import models

class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, related_name='courses')

    def __str__(self):
        return self.title

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True, help_text="სტუდენტის უნიკალური ნომერი")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    enrolled_courses = models.ManyToManyField(Course, blank=True, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"