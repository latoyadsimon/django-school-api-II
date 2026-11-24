from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False)
    student_email = models.EmailField(null = False, blank = False, unique=True)
    personal_email = models.EmailField(null = False, blank = False, unique=True)
    locker_number = models.IntegerField(default=110, null = False, blank = False, unique=True)
    locker_combination = models.CharField(default="12-12-12", max_length=255, null = False, blank = False )
    good_student = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    
    def locker_reassignment(self, int):
        self.locker_number = int
        
        
    def student_status(self, good):
        self.good_student = good