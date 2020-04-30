from django.shortcuts import render, redirect
from .models import Massage
from .forms import MassageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.
def MainPage(request):
    Massages = Massage.objects.filter(header__contains='title')
    return render(request,'MainPage.html',{'Massages': Massages})



def NewMassage(request):
     if request.method == "POST":
         form = MassageForm(request.POST)
         if form.is_valid():
             Massage = form.save(commit=False)
             Massage.author = request.user
              
             Massage.save()
             return redirect('Massage_detail', pk=Massage.pk)
     else:
        form = MassageForm()
     return render(request, 'NewMassage.html', {'form': form})        



 
def Registration(request):
    if request.method == 'POST':
        Massages = Massage.objects.filter(header__contains='title')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
    else:
        form = UserCreationForm()
    return render(request, 'Login.html', {'form': form})              