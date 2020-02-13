from django.urls import path
from django.conf.urls import include
# from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('departments/', department_list, name='department_list'), # TODO: update the context param and name value
    path('computers/', computer_list, name='computer_list'),
    path('trainingprograms/', training_program_list, name='training_list'),
    path('computers/<int:computer_id>', computer_details, name="computer")

]
