from django.db import models

class TrainingProgram(models.Model):
    """
    description: This class creates a training program and its properties
    author: Melody
    properties:
      title: name of training program
      start_date: start date of training program
      end_date: end date of training program
      capacity: max number of attendees
    """

    title = models.CharField(max_length=55)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()