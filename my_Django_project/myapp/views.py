from django.shortcuts import render,get_object_or_404, redirect
from myapp.models import *
from myapp.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
# Create your views here.

def photos(request):
	return render(request,'photos.html')

def home(request):
	query = student.objects.all()
	context_dict = {
	'student': query
	}
	return render(request,'index.html',context_dict)

def showdetails(request,id):
	obj = student.objects.get(id=id)
	context ={
	'detail': obj
	}
	return render(request,'detail.html', context)

def about(request):
	return render(request,'about.html')


@csrf_exempt
def ShowStudentForm(request):
	if request.method == 'POST':
		form = StudentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/')
	else:
		form=StudentForm()
		context_dict ={
		'form': form
		}

	return render(request, 'contact.html',context_dict)



@csrf_exempt
def user_login(request):
	if request.method == 'POST':
		form = userlogin(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					return HttpResponse('User is not active')
			else:
				return HttpResponse('User is none ')
	else:
		form = userlogin()
		context = {
		'form':form
		}
	return render(request, 'login.html', context)



def user_logout(request):
	logout(request)
	return redirect('/')


def profile(request):
	return render(request, 'profile.html')




		