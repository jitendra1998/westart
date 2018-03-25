from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import UserDetails, Sessionpart, Menudetails, Orderdetails
from django.http import HttpResponse
from .models import StartUps
# Create your views here.
def index(request):
	return render(request, 'dashboard/landingpage.html')


def signup(request):
	already_login = list(Sessionpart.objects.all())
	if already_login:
		return render(request, 'dashboard/dashboard.html')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password1']
		password1 = request.POST['password2']
		email = request.POST['email']
		listkey = list(request.POST.keys())
		if "custom" in listkey:
			type = 1
		else:
			type = 0
		# type = request.POST['custom']
		# sell = request.POST['selsl']
		# if request.POST.field_exists('sell'):
		# 	type = 0
		# elif request.POST.field_exists('custom'):
		# 	type = 1
		if UserDetails.objects.filter(username=username).exists():
			error = "User Already Exists"
			return render(request,'dashboard/signup.html' ,{'error':error})
		if password != password1:
			error = "*Passwords Not Match!"
			return render(request,'dashboard/signup.html' ,{'error':error})


		profile = UserDetails(username=username,password=password,email=email,type=type)
		profile.save()
		sv = Sessionpart(username=username)
		sv.save()
		return redirect('userorder12')

	return render(request, 'dashboard/signup.html')

def dashboard(request):
	return render(request, 'dashboard/dashboard.html')

def logout(request):
	already_login = list(Sessionpart.objects.all())
	if not already_login:
		return redirect('login')
	else:
		Sessionpart.objects.all().delete()
		return redirect('login')

def login(request):
	already_login = list(Sessionpart.objects.all())
	if already_login != []:
		return redirect('userorder12')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		if not UserDetails.objects.filter(username=username).exists():
			error = "Invalid User"
			return render(request,'dashboard/login.html' ,{'error':error})
		user = UserDetails.objects.get(username=username)
		if password != user.password:
			error = "Invalid Password"
			return render(request,'dashboard/login.html' ,{'error':error})
		else:
			sv = Sessionpart(username=username)
			sv.save()
			# return render(request, 'dashboard/dashboard.html')
			return redirect('userorder12')
	return render(request, 'dashboard/login.html')


def createstartup(request):
	if request.method == 'POST':
		startname = request.POST['startname']
		startdescription = request.POST['startdescription']
		user_name = Sessionpart.objects.all()[0]
		username = UserDetails.objects.get(username=user_name)
		print(username)
		startup = StartUps(start_up_name=startname,start_up_description=startdescription,start_up_username=username)
		startup.save()
	return render(request, 'dashboard/createstartup.html')

def userorder12(request):
	userid = Sessionpart.objects.all()[0]
	print(userid)
	Order_details = Orderdetails.objects.filter(user_name=userid)
	return render(request, 'dashboard/userorder.html', {'order_details':Order_details})

def userorder(request):
	if request.method == 'GET':
		start_up = request.GET['item']
		order_item=Menudetails.objects.get(Menu_start_up_item=start_up)
		start_up_item_price = order_item.Menu_start_up_item_price
		start_up_name = order_item.Menu_start_up_name
		Start = StartUps.objects.get(start_up_name=start_up_name)
		user_name = Sessionpart.objects.all()[0]
		# user_name = Start.start_up_username
		menu = Orderdetails(user_name=user_name,order_start_up_name=start_up_name, order_item = order_item, order_price=start_up_item_price)
		menu.save()
	# userorder12(request
	return redirect('userorder12')

def viewallstart(request):
	start_up = StartUps.objects.all()
	return render(request, 'dashboard/viewallstart.html' , {'startups_list':start_up})

def showmenu(request):
	# if request.method == 'POST':
	# 	btn = request.POST.get('submit');
	# 	order_item=Menudetails.objects.filter(Menu_start_up_item=btn)
	# 	print (btn)
	# 	start_up_item_price = Menudetails.objects.filter(Menu_start_up_item=order_item).Menu_start_up_item_price
	#
	# 	start_up_name = Menudetails.objects.filter(Menu_start_up_item=order_item).Menu_start_up_name
	# 	user_name = StartUps.objects.filter(start_up_name=start_up_name).user_name
	# 	menu = Orderdetails(user_name=user_name,order_start_up_name=start_up_name, order_item = order_item, order_start_up_item_price=start_up_item_price)
	# 	menu.save()
	start_up = request.GET['start_up']
	# print(start_up)
	# start = StartUps.objects.get(start_up_name=start_up)
	obj = Menudetails.objects.filter(Menu_start_up_name=start_up)
	return render(request, 'dashboard/showmenu.html' , {'Menudetails':obj})

def userprofile(request):
	return render(request, 'dashboard/userprofile.html')

def StartUpListView(request):
	start_up = StartUps.objects.all()
	return render(request, 'dashboard/startups.html' , {'startups_list':start_up})

# class viewallstart(ListView):
# 	queryset= StartUps.objects.all()
# 	template_name = 'dashboard/viewallstart.html'
#
# class showmenu(ListView):
# 	start_up = request.GET['start_name']
# 	queryset= StartUps.objects.all()
# 	template_name = 'dashboard/showmenu.html'
#
# class StartUpListView(ListView):
#     queryset= StartUps.objects.all()
#     template_name = 'dashboard/startups.html'
