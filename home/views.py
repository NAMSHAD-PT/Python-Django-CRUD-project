from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages

# Create your views here.
def index(request):
    data = Student.objects.all()
    context = {'datas':data}
    return render(request,'index.html',context)

def insertData(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

        query = Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Inserted Succesfully")
        print(name,email,age,gender)

        return redirect("/")

        


    return render(request,'index.html')

def updateData(request,id):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit= Student.objects.get(id=id)
        edit.name=name
        edit.email= email
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.warning(request,"Data Updated Succesfully")
        return redirect("/")
        



    d = Student.objects.get(id=id)
    context = {'d':d}
    return render(request,'update.html',context)

def deleteData(request,id):
    data = Student.objects.get(id=id)
    data.delete()
    messages.error(request,"Data Deleted Succesfully")

    return redirect("/")
    # context = {'datas':data}
    # return render(request,'index.html',context)