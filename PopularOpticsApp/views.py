from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from PopularOpticsApp.models import catdb,prodb,staffdb,contactdb
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def index(request):
    return render(request,"index.html")
def cat(request):
    return render(request,"addcategory.html")
def catsave(request):
    if request.method == "POST":
        n = request.POST.get('cname')
        d = request.POST.get('desc')
        i = request.FILES['img']
        obj=catdb(catname=n,desc=d,image=i)
        obj.save()
        return redirect(catdetails)
def catdetails(request):
    data = catdb.objects.all()
    return render(request,"categorydetails.html",{'data':data})
def catedit(request,dataid):
    data = catdb.objects.get(id=dataid)
    print(data)
    return render(request, "categoryedit.html",{'data':data})


def catupdate(request,dataid):
    if request.method == "POST":
        n = request.POST.get('cname')
        d = request.POST.get('desc')
        try:
            i = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(i.name, i)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=dataid).i
        catdb.objects.filter(id=dataid).update(catname=n, desc=d, image=file)
        return redirect(catdetails)

def catdelete(request,dataid):
    data = catdb.objects.filter(id=dataid)
    data.delete()
    return redirect(catdetails)


def addstaff(request):
    return render(request,"addstaff.html")

def staffsave(request):
    if request.method=="POST":
        n = request.POST.get('staffname')
        d = request.POST.get('desi')
        i = request.FILES['img']
        obj = staffdb(name=n,desi=d,image=i)
        obj.save()
        return redirect(staffdetails)

def staffdetails(request):
    data = staffdb.objects.all()
    return render(request,"staffdetails.html",{'data':data})


def staffedit(request,dataid):
    data = staffdb.objects.get(id=dataid)
    print(data)
    return render(request,"staffedit.html",{'data':data})


def staffupdate(request,dataid):
    if request.method=="POST":
        n = request.POST.get('staffname')
        d = request.POST.get('desi')
        try:
            i = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(i.name, i)
        except MultiValueDictKeyError:
            file = staffdb.objects.get(id=dataid).i
        staffdb.objects.filter(id=dataid).update(name=n, desi=d, image=file)
        return redirect(staffdetails)

def staffdelete(request,dataid):
    data = staffdb.objects.filter(id=dataid)
    data.delete()
    return redirect(staffdetails)


def addpro(request):
    data = catdb.objects.all()
    return render(request,"addproduct.html",{'data':data})
def prosave(request):
    if request.method == "POST":
        c = request.POST.get('cat')
        p = request.POST.get('pname')
        d = request.POST.get('desc')
        f =  request.POST.get('frame')
        s = request.POST.get('size')
        r = request.POST.get('rate')
        i = request.FILES['img']
        obj = prodb(category=c,productname=p, desc=d,frame=f,size=s,rate=r,image=i)
        obj.save()
        return redirect(prodetails)

def prodetails(request):
    data = prodb.objects.all()

    return render(request,"productdetails.html",{'data':data})
def proedit(request,dataid):
    data = prodb.objects.get(id=dataid)
    da = catdb.objects.all()
    print(data)
    return render(request,"productedit.html",{'data':data,'da':da})
def proupdate(request,dataid):
    if request.method == "POST":
        c = request.POST.get('cat')
        p = request.POST.get('pname')
        d = request.POST.get('desc')
        f = request.POST.get('frame')
        s = request.POST.get('size')
        r = request.POST.get('rate')
        try:
            i = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(i.name,i)
        except MultiValueDictKeyError:
            file = prodb.objects.get(id=dataid).i
        prodb.objects.filter(id=dataid).update(category=c,productname=p, desc=d,frame=f,size=s,rate=r,image=file)
        return redirect(prodetails)

def prodelete(request,dataid):
    data = prodb.objects.filter(id=dataid)
    data.delete()
    return redirect(prodetails)

def adminlogin(request):
    return render(request,"adminlogin.html")

def adminlog(request):
    if request.method == "POST":
        username_r = request.POST.get('user')
        password_r = request.POST.get('pass')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)

            if user is not None:
                login(request, user)
                request.session['user'] = username_r
                request.session['pass'] = password_r
                return redirect(index)

            else:
                return redirect(adminlogin)

        else:
            return redirect(adminlogin)


def contactdetails(request):
    data = contactdb.objects.all()
    return render(request,"contactinformation.html",{'data':data})
def adminlogout(request):
    del request.session['user']
    del request.session['pass']
    return redirect(adminlogin)
