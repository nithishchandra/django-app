from django.db import models

# Create your models here.

class StudentInfo(models.Model):

    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_address = models.CharField(max_length=250)

    class Meta:
        db_table = 'student_info'