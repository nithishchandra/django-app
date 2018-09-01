from django.db import models

# Create your models here.

class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField(unique=True)
    stu_address = models.CharField(max_length=250)

    def __str__(self):
        return self.stu_name

    class Meta:
        db_table = 'student'