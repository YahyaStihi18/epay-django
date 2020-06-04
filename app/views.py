from django.shortcuts import render, Http404, HttpResponseRedirect, reverse,redirect
from .models import *
from .forms import OrderForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFrom
from django.contrib.auth.models import User



# Create your views here.


def index(request):
    return render(request, 'app/index.html')

def details(request):
    return render(request, 'app/details.html')


def services(request):
    return render(request, 'app/services.html')

def contact(request):
    return render(request, 'app/contact.html')


def credit(request):
    services = ServiceCredit.objects.all()
    context = {'services': services}
    return render(request, 'app/credit.html', context)


def checkoutCredit(request, service_id):
    service = ServiceCredit.objects.get(pk=service_id)
    saller = service.distributor
    product = service.name
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.user = request.user
                instance.save()
            else:
                pass
            instance.saller = str(saller)
            instance.save()
            instance.product = str(product)
            instance.save()
            newamount = service.available-float(form.data['amount'])
            service.available = newamount
            service.save()
            form.save()
            messages.success(
                request, 'your order has been submitted successfully it will be processed in : 30 Min, you can contact the distributor at any time you want, Thank you.')

            return HttpResponseRedirect(reverse('checkoutcredit', args=(service_id,)))

    service = ServiceCredit.objects.get(pk=service_id)
    form = OrderForm()
    return render(request, 'app/checkout.html', {'service': service, 'form': form})


def games(request):
    services = ServiceGame.objects.all()
    context = {'services': services}
    return render(request, 'app/games.html', context)


def checkoutGames(request, service_id):
    service = ServiceGame.objects.get(pk=service_id)
    saller = service.distributor
    product = service.name
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.user = request.user
                instance.save()
            else:
                pass
            instance.saller = str(saller)
            instance.save()
            instance.product = str(product)
            instance.save()
            newamount = service.available-float(form.data['amount'])
            service.available = newamount
            service.save()
            form.save()
            messages.success(
                request, 'your order has been submitted successfully it will be processed in : 30 Min, you can contact the distributor at any time you want, Thank you.')

            return HttpResponseRedirect(reverse('checkoutgames', args=(service_id,)))

    service = ServiceGame.objects.get(pk=service_id)
    form = OrderForm()
    return render(request, 'app/checkout.html', {'service': service, 'form': form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"new user '{username}' created seccefully")
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'app/register.html', {'form':form})

@login_required
def profile(request):
    return render(request,'app/profile.html')