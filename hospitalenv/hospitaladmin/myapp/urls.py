from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),


    # ...........Create........

    path('Doctorreg',views.DoctorRegistration,name='Doctorreg'),
    path('Patientreg',views.PatientRegistration,name='Patientreg'),
    path('appointment',views.appointment1,name='appointment'),
    path('docreg',views.docreg,name='docreg'),
    path('deptreg',views.departmentFn,name='deptreg'),

    # .........Read........

    path('usermod',views.usermodule,name='usermod'),
    path('contact',views.contact,name='contact'),
    path('doctormodule',views.Doctormodule,name='doctormodule'),
    path('signup',views.Signup,name='signup'),
    path('viewdoctors',views.viewdoctors,name='viewdoctors'),
    path('department',views.show_dept,name='department'),
    path('viewappointment/<str:did>',views.viewappointments,name='viewappointment'),

    # ..........update.........

    path('editpatient/<pk>',views.edit_patient,name='editpatient'),


    # ...........delete.........



    # ...........logout.........
    path('logout',views.logout,name="logout"),
]
