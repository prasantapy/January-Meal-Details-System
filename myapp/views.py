from django.shortcuts import render
from myapp.models import Customer
from django.http import HttpResponse

def home(request):
    return render(request,'Home.html')
def create_data(request):
    if request.method == 'POST':
        customers = Customer.objects.create(
        name = request.POST.get('name'),
        advance = request.POST.get('advance'),
        location = request.POST.get('location'),
        date = request.POST.get('date'),
        lunch = request.POST.get('lunch'),
        dinner = request.POST.get('dinner'),
        extra_meals = request.POST.get('extra_meals'),
        )
        return render(request,'home.html')
    return render (request,'create.html')


def show_data(request):
    User = Customer.objects.all()

    return render(request,'show.html',{'Users':User})

def Update_data(request,id):
    Customers = Customer.objects.get(id=id)
    if request.method =='POST':
            Customers.name = request.POST.get('name')
            Customers.advance = request.POST.get('advance')
            Customers.location = request.POST.get('location')
            Customers.date = request.POST.get('date')
            Customers.lunch = request.POST.get('lunch')
            Customers.dinner = request.POST.get('dinner')
            Customers.extra_meals = request.POST.get('extra_meals')
            Customers.save()
            return HttpResponse('Updated !!!! ')
    return render(request,'update.html',{'Users':Customers})

def Delete_data(request,id):
    Customer.objects.filter(id=id).delete()
    return HttpResponse("Data Have Deleted !")



