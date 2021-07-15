import mimetypes

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Registeration, UserProfile
from .models import Patient
from .models import Doctor
from .models import Messages
from .models import Documents
from .models import Document
from datetime import datetime
from django.forms import Form
from healthsystem import settings
from wsgiref.util import FileWrapper


# Create your views here.
def submitmessage(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        text = request.POST['text']
        s = Messages(name=name, email=email, subject=subject, text=text)
        s.save()
        return render(request, 'homepage.html')


def download(request, filename):
    print('hello')
    file_path = settings.MEDIA_ROOT + filename
    fname = filename.split('/')[-1]
    f1 = open(file_path, 'r')
    mime_type = mimetypes.guess_type(file_path)
    response = HttpResponse(f1, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % fname
    return response


def home(request):
    return render(request, 'homepage.html')


def logout(request):
    try:
        del request.session['email']
    except:
        return render(request, 'homepage.html')
    return render(request, 'homepage.html')


def uploaddocument(request):
    doc = {'userdata': Doctor.objects.all()}
    return render(request, 'document_upload.html', doc)


def upload(request):
    if request.method == "POST":
        form = Form(request.POST)
        file = request.FILES['filename']
        # file = request.POST['filename']
        receiver = request.POST['doctors']
        sender = request.session['email']
        transaction = datetime.now()
        # if form.is_valid():
        #    file = form.cleaned_data['filename']
        # print(receiver, sender, transaction)
        t = Documents(sender=sender, receiver=receiver, transactiontime=transaction, file=file)
        t.save()
        messages.error(request,'Document sent Successfully!!')
        return render(request, 'document_upload.html')


def ulogin(request):
    return render(request, 'user_login.html')


def editdocprofile(request):
    email = request.session['email']
    userdata = {'userdata': Doctor.objects.filter(email=email)}
    return render(request, 'editDoctorProfile.html', userdata)


def edituserprofile(request):
    email = request.session['email']
    userdata = {'userdata': Patient.objects.filter(email=email)}
    return render(request, 'editUserProfile.html', userdata)


def docupdate(request):
    if request.method == "POST":
        name = request.POST['name']
        age = int(request.POST['age'])
        email = request.POST['email']
        phone = request.POST['phone']
        lisence = request.POST['lisence']
        Doctor.objects.filter(email=email).update(name=name, age=age, phno=phone, lisence=lisence, email=email)
        userdata = {'userdata': Doctor.objects.filter(email=email)}
        return render(request, 'doc_profile.html', userdata)


def userupdate(request):
    if request.method == "POST":
        name = request.POST['name']
        age = int(request.POST['age'])
        email = request.POST['email']
        phone = request.POST['phone']
        adhar = request.POST['adhar']
        Patient.objects.filter(email=email).update(name=name, age=age, phno=phone, adhar=adhar, email=email)
        userdata = {'userdata': Patient.objects.filter(email=email)}
        return render(request, 'user_profile.html', userdata)


def uregister(request):
    return render(request, 'user_register.html')


def dregister(request):
    return render(request, 'doc_register.html')


def dlogin(request):
    return render(request, 'doc_login.html')


def register(request):  # need to create the function
    if request.method == "POST":
        name = request.POST['name']
        passwor = request.POST['password']
        email = request.POST['email']
        s = Registeration(name=name, password=passwor, email=email)
        s.save()
        return HttpResponse("done")


def viewdata(request):
    vd = {'mydataa': Registeration.objects.all()}
    return render(request, 'view.html', vd)


def delete(request, email):
    d = Registeration.objects.get(pk=email)
    d.delete()
    return redirect("/viewdata")


def update(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        passwor = request.POST['password']
        s = Registeration.objects.filter(email=email).update(name=name, password=passwor)
        return HttpResponse("Yes")


def supdate(request, email):
    ab = {'mydata': Registeration.objects.filter(pk=email)}
    return render(request, 'update.html', ab)


def userReg(request):
    if request.method == "POST":
        name = request.POST['name']
        age = int(request.POST['age'])
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        adhar = request.POST['adhar']
        password = request.POST['password']
        if Patient.objects.filter(email=email).exists():
            messages.error(request,'Already existing user Email is used!!')
            return render(request, 'user_register.html')
        if Patient.objects.filter(adhar=adhar).exists():
            messages.error(request,'Already existing user Adhar is used!!')
            return render(request, 'user_register.html')
        if Patient.objects.filter(name=name).exists():
            messages.error(request,'Already existing user Name is used!!')
            return render(request, 'user_register.html')
        s = Patient(name=name, age=age, email=email, phno=phone, gender=gender, adhar=adhar, password=password)
        s1=UserProfile(name=name,email=email,type="patient")
        s.save()
        s1.save()
        return render(request, 'user_register.html', {'some_flag': True})


def userLog(request):
    if request.method == "POST":
        request.session['email'] = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        if Patient.objects.filter(email=request.session['email'], password=password).exists():
            userdata = {'userdata': Patient.objects.filter(email=email)}
            return render(request, 'user_profile.html', userdata)
        else:
            # return render(request, "Error.html")
            messages.error(request,'Email or Password is Incorrect!!')
            return render(request, 'user_login.html')
    else:
        return render(request, 'user_login.html')


def docReg(request):
    if request.method == "POST":
        name = request.POST['name']
        age = int(request.POST['age'])
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        lisence = request.POST.get('license', False)
        password = request.POST['password']
        # print(name,age,email,phone,gender,lisence,password)
        name="Dr "+name
        if Doctor.objects.filter(email=email).exists():
            messages.error(request,'Already existing user Email is used!!')
            return render(request, 'doc_register.html')
        if Doctor.objects.filter(lisence=lisence).exists():
            messages.error(request,'Already existing user Lisense is used!!')
            return render(request, 'doc_register.html')
        if Doctor.objects.filter(name=name).exists():
            messages.error(request,'Already existing user Name is used!!')
            return render(request, 'doc_register.html')
        s = Doctor(name=name, age=age, email=email, phno=phone, gender=gender, lisence=lisence, password=password)
        s1=UserProfile(name=name,email=email,type="doctor")
        s.save()
        s1.save()
        return render(request, 'doc_register.html', {'some_flag': True})


def dogLog(request):
    if request.method == "POST":
        request.session['email'] = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        if Doctor.objects.filter(email=request.session['email'], password=password).exists():
            userdata = {'userdata': Doctor.objects.filter(email=email)}
            return render(request, 'doc_profile.html', userdata)
        else:
            # return render(request, "Error.html")
             messages.error(request,'Email or Password is Incorrect!!')
             return render(request, 'doc_login.html')
    else:
        return render(request, 'doc_login.html')


def viewdoc(request):
    email = request.session['email']
    userdata = {'userdata': Documents.objects.filter(receiver=email)}
    return render(request, 'view_patient.html', userdata)

def userProfile(request):
    email = request.session['email']
    userdata = {'userdata': Patient.objects.filter(email=email)}
    return render(request, 'user_profile.html', userdata)

def docProfile(request):
    email = request.session['email']
    userdata = {'userdata': Doctor.objects.filter(email=email)}
    return render(request, 'doc_profile.html', userdata)