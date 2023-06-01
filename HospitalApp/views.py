from django.shortcuts import render,redirect
from HospitalApp.models import HospitalDB,DoctorsDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


# Create your views here.
def index(req):
    return render(req,"Index.html")
def hospitalpage(req):
    return render(req,"Add_Hospital.html",)
def savehospital(req):
    if req.method == "POST":
        ha = req.POST.get('name')
        dis = req.POST.get('district')
        loc = req.POST.get('location')
        con = req.POST.get('contact')
        img = req.FILES['image']
        obj = HospitalDB(Hospital_Name=ha, District=dis, Location=loc, Contact_Number=con,Image=img)
        obj.save()
        return redirect(hospitalpage)
def displayhospital(req):
    data = HospitalDB.objects.all()
    return render(req,"Display_Hospital.html",{'data':data})
def edithospital(req,dataid):
    data = HospitalDB.objects.get(id=dataid)
    return render(req,"Edit_Hospital.html", {'data': data})
def updatehospital(req,dataid):
    if req.method == "POST":
        ha = req.POST.get('name')
        dis = req.POST.get('district')
        loc = req.POST.get('location')
        con = req.POST.get('contact')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = HospitalDB.objects.get(id=dataid).Image
        HospitalDB.objects.filter(id=dataid).update(Hospital_Name=ha, District=dis, Location=loc, Contact_Number=con, Image=file)
        return redirect(displayhospital)


def deletehospital(req, dataid):
    data = HospitalDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayhospital)


def doctorspage(req):
    data = HospitalDB.objects.all()
    return render(req,"Add_Doctors.html",{'data':data})
def savedoctors(req):
    if req.method == "POST":
        hn = req.POST.get('select')
        dn = req.POST.get('name')
        dep = req.POST.get('department')
        con = req.POST.get('contact')
        img = req.FILES['image']
        obj = DoctorsDB(Hospital_Name=hn, Doctor_Name=dn, Department=dep,Contact_Number=con , Image=img)
        obj.save()
        return redirect(doctorspage)

def displaydoctors(req):
    data = DoctorsDB.objects.all()
    return render(req,"Display_Doctors.html",{'data':data})
def editdoctors(req,dataid):
    data = HospitalDB.objects.all()
    doctors = DoctorsDB.objects.get(id=dataid)
    return render(req,"Edit_Doctors.html", {'data': data, 'doctors':doctors})
def updatedoctors(req,dataid):
    if req.method == "POST":
        hn = req.POST.get('select')
        dn = req.POST.get('name')
        dep = req.POST.get('department')
        con = req.POST.get('contact')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = DoctorsDB.objects.get(id=dataid).Image
        DoctorsDB.objects.filter(id=dataid).update(Hospital_Name=hn, Doctor_Name=dn, Department=dep,Contact_Number=con, Image=file)
        return redirect(displaydoctors)
def deletedoctors(req, dataid):
    data = DoctorsDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydoctors)

def adminloginpage(req):
    return render(req,"Admin_Login.html")
def adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(index)
            else:
                return redirect(adminloginpage)
        else:
            return redirect(adminloginpage)
def adminlogout(request):
        del request.session['username']
        del request.session['password']
        return redirect(adminloginpage)





