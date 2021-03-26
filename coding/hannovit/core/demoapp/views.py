from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm,EditPatientForm
import json
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site

def getlist(request):
    try:
        data = Patient.objects.all()
    except Patient.DoesNotExist as e:
        print(e)
        return "Does Not Exist"
    return render(request, 'views/index.html',{"data":data})


def edit_data(request,id):
    data = Patient.objects.get(id=id)
    if request.method == 'POST':
        form = EditPatientForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/view')
        return render(request,'views/edit.html',{"data":data})
    return render(request,'views/edit.html',{"data":data})
    
   

def delete_data(request,id):
    if request.method == 'POST':
        try:
            data = Patient.objects.get(id=id)
            data.delete()
            payload = {'deleted': True}
        except Patient.DoesNotExist:
            return "Data DoesNot Exist"
    return JsonResponse(payload)

def detail_data(request,id):
        try:
            data = Patient.objects.get(id=id)
        except Patient.DoesNotExist as e:
            print(e)
            return "Value error"
        return render(request, 'views/detail.html', {'data':data})

def add_data(request):
    if request.method == 'POST':
        form = PatientForm(request.POST or None)
        if form.is_valid():
            print("valid")
            form.save()
        
            return redirect('/dashboard/view')
   
        return render(request,'views/add.html')
    return render(request,'views/add.html')
    
