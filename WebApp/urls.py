from django.urls import path
from WebApp import views

urlpatterns =[
    path('displayhome/',views.displayhome,name="displayhome"),
    path('hospitalspage/<catg>/<int:dataid>/',views.hospitalspage,name="hospitalspage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('appointmentpage/',views.appointmentpage,name="appointmentpage"),
    path('doctorinfopage/<int:dataid>/',views.doctorinfopage,name="doctorinfopage"),
    path('appointmentsave/',views.appointmentsave,name="appointmentsave"),
    path('userloginpage/',views.userloginpage,name="userloginpage"),
    path('savelogin/',views.savelogin,name="savelogin"),
    path('userlogin/',views.userlogin,name="userlogin"),

   ]
