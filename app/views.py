from django.shortcuts import render, Http404, HttpResponseRedirect, reverse,redirect,get_object_or_404
from .models import *
from .forms import OrderForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFrom
from django.contrib.auth.models import User
from django.db.models import F
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView,CreateView




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
    currency = service.currency
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.user = request.user
                instance.save()
            else:
                pass
            instance.currency = str(currency)
            instance.save()
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
    currency = service.currency
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.user = request.user
                instance.save()
            else:
                pass
            instance.currency = str(currency)
            instance.save()
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
    orders = Order.objects.filter(user=request.user).order_by('-date')
    return render(request,'app/profile.html',{'orders':orders})

def delete(request, order_pk):
    user = request.user  # you get the loged user
    order = Order.objects.get(pk=order_pk)  # you get the order through the pk
    if order.user == user:  # you check if the user is the owner of the order
        order.visible_for_buyer = False  # set the attr to false
        order.save()  # save that specific object
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # you redirect to the page you came (you can change this for whatever you want)
    else:
        raise PermissionDenied()  # in case someone that is not the user tries to execute that view through the url you make, it will raise an error.

@login_required
def saller(request):
    user = request.user
    if user.is_staff :
        distributor = Distributor.objects.get(user=user)
        orders = Order.objects.filter(saller=user).order_by('date')
        services_games = ServiceGame.objects.filter(distributor=distributor)
        services_credit = ServiceCredit.objects.filter(distributor=distributor)
        context = {'distributor':distributor,
                'services_games':services_games,
                'services_credit':services_credit,
                'orders':orders,
               }
        return render(request,'app/saller.html',context)
    else:
        raise PermissionDenied()

class ServiceCreateView(CreateView):
    model = Order
    fields = ['name','price','currency','available']





