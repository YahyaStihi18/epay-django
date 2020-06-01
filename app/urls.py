from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('details', views.details, name='details'),
    path('services/',views.services, name='services'),
    path('contact/',views.contact, name='contact'),
    path('services/credit/',views.credit, name='credit'),
    path('services/games/', views.games, name='games'),
    path('services/checkout/credit/<int:service_id>/', views.checkoutCredit, name='checkoutcredit'),
    path('services/checkout/games/<int:service_id>/', views.checkoutGames,name='checkoutgames'),
]

