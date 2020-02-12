from django.urls import path
from django.conf.urls import include
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('departments/', employee_list, name='employee_list'),
    path('trainingprograms/', employee_list, name='employee_list'),
    path('computers/', employee_list, name='employee_list'),
    path('computers/<int:computer_id>', computer_details, name="computer")

]
