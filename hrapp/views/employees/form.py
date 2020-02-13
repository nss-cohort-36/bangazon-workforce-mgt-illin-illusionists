import sqlite3
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from hrapp.models import Employee

def employee_form(request):
    if request.method == 'GET':
        

        template = 'employees/form.html'
        context = {}

    return render(request, template, context)
