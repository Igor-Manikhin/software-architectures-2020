from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from App.Facade.Facade import Facade


def index(request):
    return render(request, 'index.html')


def clientAccount(request):
    return render(request, 'clientAccountPage.html')


def managerAccount(request):
    return render(request, 'managerAccountPage.html')


def masterAccount(request):
    return render(request, 'masterAccountPage.html')


def signIn(request):
    if request.method == "POST":
        roles = ['Client', 'Manager', 'Master']
        login = request.POST.get("login")
        password = request.POST.get('password')
        client = request.POST.get('Client')
        return HttpResponse("<h2>Hello, {0}</h2>".format(login))
    else:
        return render(request, 'authPage.html')


def signUp(request):
    if request.method == "POST":
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'password']
        data = list(map(lambda x: request.POST.get(x), fields))
        Facade().registration(data, 'Client')
        return HttpResponse("<h2>Hello</h2>")
    else:
        return render(request, 'signUpPageForClients.html')


def signUpForManagers(request):
    if request.method == 'POST':
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'password']
        data = list(map(lambda x: request.POST.get(x), fields))
        Facade().registration(data, 'Manager')
        return HttpResponse("<h2>Hello</h2>")
    else:
        return render(request, 'signUpPageForManagers.html')


def signUpForMasters(request):
    if request.method == 'POST':
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'password']
        data = list(map(lambda x: request.POST.get(x), fields))
        Facade().registration(data, 'Master')
        return HttpResponse("<h2>Hello</h2>")
    else:
        return render(request, 'signUpPageForMasters.html')


def availableCars(request):
    data = {'cars': Facade().getCarsList()}
    return render(request, 'availableCarsPage.html', context=data)


def getRequestsCarRental(request):
    data = {'data': Facade().getIncomingRequests('Игорь', 'Car_Rental')}
    return render(request, 'CarRentalRequests.html', context=data)


def getRequestsCloseCarRental(request):
    data = {'data': Facade().getIncomingRequests('Игорь', 'Close_Car_Rental')}
    return render(request, 'CarRentalRequests.html', context=data)


def createContract(request):
    Facade().createContract('Игорь', 'Семён')