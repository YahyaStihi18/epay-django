from django.urls import path,reverse
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('services/',views.services, name='services'),
    path('contact/',views.contact, name='contact'),
    path('services/credit/',views.credit, name='credit'),
    path('services/games/', views.games, name='games'),
    path('services/checkout/service/<int:service_id>/', views.checkout, name='checkout'),

    path('saller/',views.saller,name="saller"),
    path('saller/service/add/', views.service_create, name='add'),
    path('saller/service/<int:pk>/edit/',views.service_update,name='edit'),
    path('saller/service/<int:pk>/delete/',views.delete_service,name='delete_service'),


    path('profile/', views.profile,name='profile'),
    path('profile/delete/<int:order_pk>/', views.delete, name='delete'),
    path('register/', views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='app/login.html'),name='login' ),
    path('logout/',auth_views.LogoutView.as_view(template_name='app/logout.html'),name='logout' ),

]

