from django.shortcuts import render,redirect
from .models import Catagory,Product
from django.contrib import messages
from shop.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,'index.html', {"products": products})
def register(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Success")
            return redirect('login')
    return render(request,'register.html',{'form':form})
def login_page(request):

  if request.user.is_authenticated:
      return redirect('/')
  else:
    if request.method == 'POST':
            name=request.POST.get('username')
            password = request.POST.get('password')
            user=authenticate(request,username=name,password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid User Name or Password")
                return redirect("/login")

    return render(request,'login.html')
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect('/')


def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,'collections.html',{'catagory':catagory})
def collectionsview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,'collectionsview.html',{'products':products,"name":name})
    else:
        messages.warning(request,"No Such Category Found")
        return redirect('collections')
def product_details(request,cname,pname):
    if(Catagory.objects.filter(status=0,name=cname)):
        if (Product.objects.filter(status=0, name=pname)):
            products=Product.objects.filter(status=0, name=pname).first()
            return render(request,"product_details.html",{"products":products})
        else:
            messages.error(request, "No Products Found")
            return redirect('collections')

    else:
        messages.error(request, "No Such Catagory Found")
        return redirect('collections')