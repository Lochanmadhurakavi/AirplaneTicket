from django.shortcuts import redirect, render
from .models import Passenger
from .forms import ModelPassenger

# Create your views here.

def homepage(request):
    data = Passenger.objects.all()
    context = {'datas':data}
    return render(request, 'passengers/homepage.html', context)

def createPassenger(request):
    form = ModelPassenger()
    if request.method == 'POST':
        form = ModelPassenger(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form }
    return render(request, 'passengers/create.html', context)

def viewPassenger(request, pk):
    data = Passenger.objects.get(id=pk)
    context = {'datas':data}
    return render(request, 'passengers/viewPassenger.html', context)

def updatePassenger(request, pk):
    data = Passenger.objects.get(id=pk)
    form = ModelPassenger(instance=data)
    if request.method == 'POST':
        form = ModelPassenger(request.POST, instance=data, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'passengers/updatePassenger.html', context)

def deletePasseger(request, pk):
    data = Passenger.objects.get(id=pk)
    data.delete()
    return redirect('/')
