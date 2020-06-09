from django.shortcuts import render, Http404, HttpResponseRedirect, reverse, redirect, get_object_or_404
from .models import *
from .forms import OrderForm, ServiceForm,EmailForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterFrom
from django.contrib.auth.models import User
from django.db.models import F
from django.core.exceptions import PermissionDenied


# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def details(request):
    return render(request, 'app/details.html')


def services(request):
    return render(request, 'app/services.html')


def contact(request):
    form = EmailForm
    context = {'form':form}
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'app/contact.html',context)


def credit(request):
    services = Service.objects.filter(model='credit')
    context = {'services': services}
    return render(request, 'app/credit.html', context)


def games(request):
    services = Service.objects.filter(model='game')
    context = {'services': services}
    return render(request, 'app/games.html', context)

def other(request):
    services = Service.objects.filter(model='other')
    context = {'services': services}
    return render(request, 'app/other.html', context)


def checkout(request, service_id):
    service = Service.objects.get(pk=service_id)
    distributor = service.distributor
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
            instance.distributor = str(distributor)
            instance.save()
            instance.product = str(product)
            instance.save()
            newamount = service.available-float(form.data['amount'])
            service.available = newamount
            service.save()
            form.save()
            messages.success(
                request, 'your order has been submitted successfully it will be processed in : 30 Min, you can contact the distributor at any time you want, Thank you.')

            return HttpResponseRedirect(reverse('checkout', args=(service_id,)))

    service = Service.objects.get(pk=service_id)
    form = OrderForm()
    return render(request, 'app/checkout.html', {'service': service, 'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"new user '{username}' created seccefully")
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'app/register.html', {'form': form})


@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user).order_by('-date')
    return render(request, 'app/profile.html', {'orders': orders})


def delete(request, order_pk):
    user = request.user  # you get the loged user
    order = Order.objects.get(pk=order_pk)  # you get the order through the pk
    if order.user == user :  # you check if the user is the owner of the order
        order.visible_for_buyer = False  # set the attr to false
        order.save()  # save that specific object
        # you redirect to the page you came (you can change this for whatever you want)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        # in case someone that is not the user tries to execute that view through the url you make, it will raise an error.
        raise PermissionDenied()


@login_required
def saller(request):
    user = request.user
    if user.is_staff:
        distributor = Distributor.objects.get(user=user)
        orders = Order.objects.filter(distributor=user.username).order_by('-date')
        services = Service.objects.filter(distributor=distributor)
        context = {'distributor': distributor,
                   'services': services,
                   'orders': orders,
                   }
        return render(request, 'app/saller.html', context)
    else:
        raise PermissionDenied()


def service_create(request):
    user = request.user
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            distributor = form.cleaned_data['distributor']
            if str(distributor) != str(user.username):
                messages.warning(
                    request, "please select your own distributor accountt")
                return redirect('add')
            else:
                form.save()
                messages.success(
                    request, 'your Service has been saved')
                return HttpResponseRedirect(reverse('saller'))

    form = ServiceForm()
    return render(request, 'app/service_add.html', {'form': form})


def service_update(request, pk):
    user = request.user
    service = Service.objects.get(id=pk)
    form = ServiceForm(instance=service)
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            distributor = form.cleaned_data['distributor']
            if str(distributor) != str(user.username):
                messages.warning(
                    request, "please select your own distributor accountt")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                form.save()
                messages.success(
                    request, 'your Service has been saved')
                return HttpResponseRedirect(reverse('saller'))
    return render(request, 'app/service_add.html', {'form': form})


def delete_service(request,pk):
    user = request.user 
    service = Service.objects.get(id=pk)  
    if service.distributor.user == user: 
        service.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        raise PermissionDenied()


def view_order(request,pk):
    user = request.user
    order = Order.objects.get(id=pk)
    if order.distributor != user.username : 
        raise PermissionDenied()
    else:
        return render(request,'app/view_order.html',{'order':order})

def delete_order(request, pk):
    user = request.user  # you get the loged user
    order = Order.objects.get(id=pk)  # you get the order through the pk
    if order.distributor == user.username:  # you check if the user is the owner of the order
        order.visible_for_distributor = False   # set the attr to false
        order.save()  # save that specific object
        # you redirect to the page you came (you can change this for whatever you want)
        return HttpResponseRedirect(reverse('saller'))
    else:
        # in case someone that is not the user tries to execute that view through the url you make, it will raise an error.
        raise PermissionDenied()

def status_order(request, pk):
    user = request.user 
    order = Order.objects.get(id=pk) 
    if order.distributor == user.username: 
        order.status = 'complete'  
        order.save() 
        return HttpResponseRedirect(reverse('saller'))
    else:
        raise PermissionDenied()

