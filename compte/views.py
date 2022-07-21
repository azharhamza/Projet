
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .form import UserCreationForm
from django.contrib import messages
# Create your views here.

def inscriptionpage(request):
    form = UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account Create successfully')
            return redirect('acces')
    context={'form':form}
    return render(request,'compte/inscription.html',context)

def accespage(request):
    context={}
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None :
            login(request,user)
            return redirect('Data')
        else:
            messages.info(request,"there is an error in the name or in the password")
    return render(request,'compte/acces.html',context)

def logoutUser(request):
    logout(request)
    return redirect('acces')