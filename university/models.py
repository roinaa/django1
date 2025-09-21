# university/models.py

from django.db import models

# რადგან კურსს სჭირდება ლექტორი, ლექტორის მოდელი პირველი შევქმნათ
class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# კურსის მოდელი, რომელსაც აქვს "ბევრი ერთთან" კავშირი ლექტორთან
class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, related_name='courses')
    # on_delete=models.SET_NULL ნიშნავს, რომ ლექტორის წაშლის შემთხვევაში,
    # ამ ლექტორის კურსებში lecturer ველი გახდება ცარიელი (NULL) და კურსი არ წაიშლება.

    def __str__(self):
        return self.title

# სტუდენტის მოდელი, რომელსაც აქვს "ბევრი ბევრთან" კავშირი კურსებთან
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True, help_text="სტუდენტის უნიკალური ნომერი")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    enrolled_courses = models.ManyToManyField(Course, blank=True, related_name='students')
    # ManyToManyField ავტომატურად შექმნის მესამე ცხრილს ამ ორი მოდელის დასაკავშირებლად.

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"