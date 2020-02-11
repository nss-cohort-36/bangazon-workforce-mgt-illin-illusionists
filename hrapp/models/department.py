from django.db import models

class Department(models.Model):
    """
    description: This class creates a department and its properties
    author: Melody
    properties:
      dept_name: name of department
      budget: department budget
    """

    dept_name = models.CharField(max_length= 25)
    budget = models.IntegerField()