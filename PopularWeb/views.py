from django.shortcuts import render,redirect
from PopularOpticsApp.models import catdb,prodb,staffdb,contactdb,estimatedb
from PopularWeb.models import Customerdetails,cartdb
# Create your views here.
def indexpg(request):
    data = catdb.objects.all()
    return render(request,"index1.html",{"data":data})

def contactpg(request):
    data = catdb.objects.all()
    return render(request,"contact.html",{'data':data})

def aboutpg(request):
    data = catdb.objects.all()
    return render(request,"about.html",{'data':data})

def staffpg(request):
    data = staffdb.objects.all()
    da = catdb.objects.all()
    return render(request,"staff.html",{'data':data,'da':da})

def productpg(request):
    data=prodb.objects.all()
    return render(request,"products.html",{"dat":data})
def displaycategory(request,ItemCatg):
    print("---------ItemCatg---------",ItemCatg)
    catg = ItemCatg.upper()
    products = prodb.objects.filter(category=ItemCatg)
    context = {
        'products':products,
        'catg':catg
    }
    return render(request,"display category.html",context)

def prodetail(request,dataid):
    data = prodb.objects.get(id=dataid)
    return render(request,"productdetail.html",{"dat":data})

def login(request):
    data = catdb.objects.all()
    return render(request,"login_register.html",{'da':data})

def loginsave(request):
    if request.method=="POST":
        u = request.POST.get('username')
        e = request.POST.get('email')
        p = request.POST.get('password')
        c = request.POST.get('confirmpassword')
        if p == c:
            obj = Customerdetails(username=u,email=e,password=p,confirmpassword=c)
            obj.save()
            return redirect(login)
        else:
            return render(request,'login_register.html',{'msg':"Sorry......password not matched "})

def customerlogin(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if Customerdetails.objects.filter(username = username_r,password=password_r).exists():

            request.session['username'] = username_r
            request.session['password'] = password_r


            return redirect(indexpg)
        else:
            return render(request,'login_register.html',{'msg1':"Sorry......password not matched "})


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(indexpg)

def contactsave(request):
    if request.method=="POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        s = request.POST.get('sub')
        m = request.POST.get('msg')
        obj = contactdb(name=n,email=e,subject=s,message=m)
        obj.save()
        return redirect(contactpg)

def cart(request):
    da = catdb.objects.all()
    data = cartdb.objects.all()
    return render(request,"cart.html",{'da':da,'data':data})

def cartsave(request):
    if request.method=="POST":
        i = request.FILES['img']
        n = request.POST.get('productname')
        f = request.POST.get('frame')
        q = request.POST.get('quantity')
        t = request.POST.get('totalprice')
        obj = cartdb(image=i, productname=n, frame=f,quantity=q,total=t)
        obj.save()
        return redirect(cart)

def estimate(request):
    if request.method == "POST":
        c = request.POST.get('country')
        s = request.POST.get('state')
        z = request.POST.get('zip')
        obj = estimatedb(country=c , state=s, zip=z)
        obj.save()
        return redirect(cart)
