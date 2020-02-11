## Steps to get your project started:

* Clone down your team's repo and `cd` into it

* Create your OSX virtual environment in Terminal:

  * `python -m venv workforceenv`
  * `source ./workforceenv/bin/activate`

* Or create your Windows virtual environment in Command Line:

  * `python -m venv workforceenv`
  * `cd workforceenv`
  * `cd Scripts`
  * `activate.bat`
  * `cd ..`
  * `cd ..`

* Install the app's dependencies:

  * `pip install -r requirements.txt`

* Build your database from the existing models:

  * `python manage.py makemigrations hrapp`
  * `python manage.py migrate`

* Create a superuser for your local version of the app:

  * `python manage.py createsuperuser`

* Populate your database with initial data from fixtures files: (_NOTE: every time you run this it will remove existing data and repopulate the tables_)

  * `python manage.py loaddata computers`
  * `python manage.py loaddata users`

* Fire up your dev server and get to work!

  * `python manage.py runserver`


## Official Bangazon LLC ERD

Our team of database developers and administrators developed this ERD for you to reference when creating your models.

https://dbdiagram.io/d/5bad7831a3794b0014b3ccc7

Not that the column names do not conform to the Python community standards (PEP) for naming conventions. Make sure your models use snake case.