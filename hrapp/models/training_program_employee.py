from django.db import models

class TrainingProgramEmployee(models.Model):
    """
    Creates the join table for the many to many relationship between training program and employee
    Author: Melody
    methods: none
    """

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    training_program = models.ForeignKey("TrainingProgram", on_delete=models.CASCADE)
