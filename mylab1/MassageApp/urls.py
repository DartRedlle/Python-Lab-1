from django.conf.urls import url,include  
from django.contrib.auth import views as auth
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.MainPage,name='MainPage'),
    path('Massage/new/', views.NewMassage, name='NewMassage'),
    path('Massage/<int:pk>/', views.NewMassage, name='NewMassage'),
     url(r'^Registration/$', views.Registration, name='Registration'),
    
   
]
