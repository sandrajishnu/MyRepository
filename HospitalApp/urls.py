from django.urls import path
from HospitalApp import views

urlpatterns =[
    path('index/',views.index,name="index"),
    path('hospitalpage/',views.hospitalpage,name="hospitalpage"),
    path('savehospital/',views.savehospital,name="savehospital"),
    path('displayhospital/',views.displayhospital,name="displayhospital"),
    path('edithospital/<int:dataid>',views.edithospital,name="edithospital"),
    path('updatehospital/<int:dataid>',views.updatehospital,name="updatehospital"),
    path('deletehospital/<int:dataid>',views.deletehospital,name="deletehospital"),


    path('doctorspage/',views.doctorspage,name="doctorspage"),
    path('savedoctors/',views.savedoctors,name="savedoctors"),
    path('displaydoctors/',views.displaydoctors,name="displaydoctors"),
    path('editdoctors/<int:dataid>', views.editdoctors, name="editdoctors"),
    path('updatedoctors/<int:dataid>', views.updatedoctors, name="updatedoctors"),
    path('deletedoctors/<int:dataid>', views.deletedoctors, name="deletedoctors"),

    path('adminloginpage/', views.adminloginpage, name="adminloginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),

]