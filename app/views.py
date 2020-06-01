from django.shortcuts import render, Http404, HttpResponseRedirect, reverse
from .models import *
from .forms import OrderForm
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'app/index.html')


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
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.saller = str(saller)
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
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.saller = str(saller)
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

