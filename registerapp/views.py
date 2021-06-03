from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from registerapp.models import Article

from .forms import CreateUserForm

# login required views (for big project need middlware using)
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def homePage(request):
	posts = Article.objects.all()
	return render(request, 'registerapp/home2.html', {'posts':posts})

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('homePage')
	else:
		form = CreateUserForm()
		if request.method == "POST":
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')

		context = {'form':form}
		return render(request, 'registerapp/home2.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('homePage')
	else:
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('homePage')
			else:
				messages.info(request, 'username or password is incorrect')

		context = {}
		return render(request, 'registerapp/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')


def home(request):
    posts = Article.objects.all()
    return render(request, 'registerapp/home2.html',{'posts':posts})