from django.db import models

# Create your models here.
# model is just a python class
# model represents a table in the db
# attrs are the field on the table
# job posting table
#  with a title, description, company, salary

class JobPosting(models.Model):
    # id - starts at 1 and autoincrements
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()

# makemigrations
# -> creates instructions telling django how the db have changed
# migrate
# -> applies the above changes
