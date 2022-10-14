from django.db import models

# Create your models here.
class StudentDetails(models.Model):
	student_name=models.CharField(max_length=255)
	course=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	mob=models.BigIntegerField()
	gender=models.CharField(max_length=255)
	adress=models.CharField(max_length=255)
	
  
 