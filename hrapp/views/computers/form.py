import sqlite3
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from hrapp.models import Computer

def computer_form(request):
    if request.method == 'GET':
        

        template = 'computers/form.html'
        context = {}

    return render(request, template, context)
