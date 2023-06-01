from django.shortcuts import render,redirect
from HospitalApp.models import HospitalDB,DoctorsDB
from WebApp.models import AppointmentDB,LogindataDB
from django.contrib import messages


# Create your views here.
def displayhome(req):
    data = HospitalDB.objects.all()
    return render(req,"Home.html",{'data':data})
def hospitalspage(req,catg,dataid):
    data = DoctorsDB.objects.get(id=dataid)
    doct = DoctorsDB.objects.filter(Hospital_Name=catg)
    return render(req,"Hospitals.html",{'doct':doct,'data':data})
def aboutpage(req):
    return render(req,"About.html")
def contactpage(req):
    return render(req,"Contact.html")

def appointmentpage(req):
    return render(req,"Appointment.html")

def doctorinfopage(req,dataid):
    data = DoctorsDB.objects.get(id=dataid)
    return render(req,"Doctor_Info.html",{'data':data})

def appointmentsave(req):
    messages.success(req, "Done")
    return redirect(displayhome)

def userloginpage(req):
    return render(req,"Userlogin.html")

def savelogin(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        pw = request.POST.get('password')
        obj = LogindataDB(Name=na, Email=em, Password=pw)
        obj.save()
        return redirect(userloginpage)
def userlogin(request):
    if request.method=="POST":
        email_r=request.POST.get('email')
        password_r=request.POST.get('password')
        if LogindataDB.objects.filter(Email=email_r, Password=password_r):
            request.session['emaill'] = email_r
            request.session['passwordl'] = password_r
            return redirect(displayhome)
        else:
            return redirect(userloginpage)
    return redirect(userloginpage)