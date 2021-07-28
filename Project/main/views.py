from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def list(request):
	object=Product.objects.all()
	context={'object':object}
	return render(request,'list.html',context)

@login_required(login_url='login')
def detail(request,id):
	object=get_object_or_404(Product,pk=id)
	context={'object':object}
	return render(request,'detail.html',context)

def register(request):
	form=CreateUserForm()

	if request.method == 'POST':
	  form=CreateUserForm(request.POST)
	  if form.is_valid():
		  form.save()
		  return redirect('login')
	context={'form':form}
	return render(request,'register.html',context)

def login(request):
	if request.user.is_authenticated:
		return redirect('list')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				auth_login(request,user)
				return redirect('list')
	context={}
	return render(request,'login.html',context)
def logoutUser(request):
	logout(request)
	return redirect('login')