import sqlite3
from django.shortcuts import render
from hrapp.models import TrainingProgram
from ..connection import Connection

def training_program_form(request):
    if request.method == 'GET':
        template = 'trainingprograms/trainingprograms_form.html'
        context= {}

    return render(request, template, context)
