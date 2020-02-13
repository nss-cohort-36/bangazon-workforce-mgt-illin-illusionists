import sqlite3
from django.shortcuts import render
from ..connection import Connection

def training_program_form(request):
    if request == 'GET':
        template = 'trainingprograms/trainingprograms_form.html'
        context: {}

    return render(request, template, context)
