import sqlite3
from django.shortcuts import redirect, render, reverse
from hrapp.models import TrainingProgram
from hrapp.models import Employee
from ..connection import Connection

# SQL Helper Function that parses each row/ tuple from the SQL query results
# Within each row, set these properties for Training Program instance and Employee instance from models 
# Creating an empty list to store many to one items joined from other database table it was flat in database and now we are building useable, nested data
#  Returned as tuples to plug into get_training_program function

def create_employee_training(cursor, row):
    _row = sqlite3.Row(cursor, row)

    tp = TrainingProgram()
    tp.id = _row["id"]
    tp.title = _row["title"]
    tp.start_date = _row["start_date"]
    tp.end_date = _row["end_date"]
    tp.capacity = _row["capacity"]

    tp.employees = []

    employee = Employee()
    if _row["employee_first_name"] is not None:
        employee.first_name = _row["employee_first_name"] 
        employee.last_name = _row["employee_last_name"] 
    
    return (tp, employee,)

# SQL Query 

def get_training_program(program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee_training
        db_cursor = conn.cursor()

        db_cursor.execute( """
        SELECT
            tp.id,
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
            # training program's `id` value, add the key and set the value
            # to the current program
            if tp.id not in tp_groups:
                tp_groups[tp.id] = tp
                if employee.first_name:
                    tp_groups[tp.id].employees.append(employee)

            # If the key does exist, just append the current
            # employee to the list of employees for the current training program
            else:
                if employee.first_name:
                    tp_groups[tp.id].employees.append(employee)
        return tp_groups

def training_details(request, program_id):
    if request.method == 'GET':
        program = get_training_program(program_id)
        template = 'trainingprograms/detail.html'
        context = {
            'program': program[program_id], 
            'employees': program[program_id].employees,
            'has_employees': len(program[program_id].employees) > 0
        }

    return render(request, template, context)