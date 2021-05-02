from django.http.response import HttpResponse
from django.shortcuts import render, redirect  
from .forms import laptopForm  
from .models import Laptop  

def new(request):  
    if request.method == "POST":  
        form = laptopForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = laptopForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    laptop = Laptop.objects.all()  
    return render(request,"show.html",{'Laptops':laptop})  
def edit(request, id):  
    laptop = Laptop.objects.get(id=id)  
    return render(request,'edit.html', {'Laptops':laptop})  
def update(request, id):
    laptop = Laptop.objects.get(id=id)
    form = laptopForm(instance = laptop) 
    print("laptop") 
    if request.method=='POST': 
        form = laptopForm(request.POST, request.FILES, instance = laptop)  
        if form.is_valid():  
            print('Here form')  
            form.save()  
            return redirect("/show")  
        else:
            return HttpResponse(form.errors)
    return render(request, 'edit.html', {'form': form, 'id':laptop.id}) 
def destroy(request, id):  
    laptop = Laptop.objects.get(id=id)  
    laptop.delete()  
    return redirect("/show")  