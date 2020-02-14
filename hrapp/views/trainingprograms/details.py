import sqlite3
from django.shortcuts import redirect, render, reverse
from hrapp.models import TrainingProgram
from hrapp.models import Employee
from ..connection import Connection

def create_employee_training(cursor, row):
    _row = sqlite3.Row(cursor, row)

    tp = TrainingProgram()
    tp.title = _row["title"]
    tp.start_date = _row["start_date"]
    tp.end_date = _row["end_date"]
    tp.capacity = _row["capacity"]

    tp.employees = []

    employee = Employee()
    employee.first_name = _row["employee_first_name"] 
    employee.last_name = _row["employee_last_name"]

    
    return (tp, employee,)

def get_training_program(program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee_training
        db_cursor = conn.cursor()

        db_cursor.execute( """
        SELECT
            tp.title,
            tp.start_date,
            tp.end_date,
            tp.capacity,
            e.first_name as employee_first_name,
            e.last_name as employee_last_name
        FROM hrapp_trainingprogram tp
        LEFT JOIN hrapp_trainingprogramemployee tpe
        ON tp.id = tpe.training_program_id
        LEFT JOIN hrapp_employee e
        ON tpe.employee_id = e.id
        WHERE tp.id = ?
        """, (program_id,))

        programs = db_cursor.fetchall()

        # Start with an empty dictionary
        tp_groups = {}

        # Iterate the list of tuples
        for (tp, employee) in programs:

    # If the dictionary does have a key of the current
    # traing program's `id` value, add the key and set the value
    # to the current program
            if tp.id not in tp_groups:
                tp_groups[tp.id] = tp
                tp_groups[tp.id].employees.append(employee)

    # If the key does exist, just append the current
    # book to the list of books for the current library
            else:
                tp_groups[tp.id].employees.append(employee)
        return programs

def training_details(request, program_id):
    if request.method == 'GET':
        program = get_training_program(program_id)

        template = 'trainingprograms/detail.html'
        context = {
            'program': program
        }

    return render(request, template, context)