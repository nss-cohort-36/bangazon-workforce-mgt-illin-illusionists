import sqlite3
from django.shortcuts import reverse, redirect, render
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from hrapp.models import Computer

def computer_form(request):
