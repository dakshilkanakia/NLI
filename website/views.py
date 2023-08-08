from telnetlib import AUTHENTICATION
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import AddRecordForm
from .models import Record
from django.db.models import Q 


# Create your views here.

def home(request):

    records = Record.objects.all()

    # chek to see if user if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request,"Invalid credentials")
            return redirect('home')  
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')
    
def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request,"You are not logged in Kindly Login")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        confirm_delete = Record.objects.get(id=pk)
        return render(request, 'confirm_delete.html', {'confirm_delete': confirm_delete})
    else:
        messages.success(request,"You are not logged in Kindly Login")
        return redirect('home')

def confirm_delete(request,pk):
    if request.user.is_authenticated:
        delete_it2 = Record.objects.get(id=pk)
        delete_it2.delete()
        messages.success(request,"Record Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request,"You are not logged in Kindly Login")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record =    form.save()
                messages.success(request,"Record added successfully")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request,"You must be logged in")
        return redirect('home') 
        
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request,"You are not logged in Kindly Login")
        return redirect('home')
    