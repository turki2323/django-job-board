from django.db import models



JOB_TYPE = (
( 'Full Time', 'Full Time'), 
( 'Part Time', 'Part Time'), 


)

# Create your models here.
class Job (models.Model):
    title = models.CharField (max_length=100)

   # location
Job_type = models.CharField(max_length=15 , choices = JOB_TYPE)





