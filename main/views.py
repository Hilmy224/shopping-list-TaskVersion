import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from main.forms import ProductForm
from main.models import Item

#Imports for registration and forms for new accounts
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  

#Imports for logins and authentichations for said accounts and also logouts
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

#Imports  for restricting access 
from django.contrib.auth.decorators import login_required

#Imports for adding the cookies
import datetime

#For implementing AJAX
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound

#Flutter Json Response
from django.http import JsonResponse

@login_required(login_url='/login')

# Create your views here.
def show_main(request):
    items = Item.objects.filter(user=request.user)
    tempItemCount=0
    for ii in items:
        tempItemCount+=ii.amount
    
    context = {
        'name': request.user.username,
        'class': 'PBP D',
        'products': items,
        'itemCount':tempItemCount,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

#Creates a registration form automatically and if submitted a new user will be made
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)


#Login function
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()),max_age=3*24*60*60) # Set the cookies max age so you can l
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

#Logout functions
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

#Modify create prodcut to save data into respective user
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        userItem = form.save(commit=False)
        userItem.user = request.user
        userItem.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)


#Create a variable to store all the data and return them in xml format(using serialiizer)
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

#Create a variable that also assigns an id for each object and return them in xml format
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#Create a variable to store all the data and return them in json format
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#Adding Amount to the Data(Does'nt really allign with my theme)
def add_amount(request,id):
    if request.method == "POST":
        tempItem=Item.objects.get(pk=id)
        tempItem.amount+=1
        tempItem.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def lessen_ammount(request,id):
    if request.method == "POST":
        tempItem=Item.objects.get(pk=id)
        if tempItem.amount>0:
            tempItem.amount-=1
            tempItem.save()
        if tempItem.amount==0:
            tempItem.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_product(request,id):
    if request.method == "POST":
        tempItem=Item.objects.get(pk=id)
        tempItem.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            species= data['species'],
            amount = int(data["amount"]),
            spiritStatus=data["spiritStatus"],
            causeOfDeath=data["causeOfDeath"],
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        species = request.POST.get("species")
        amount = request.POST.get("amount")
        spiritStatus=request.POST.get("spiritStatus")
        causeOfDeath=request.POST.get("causeOfDeath")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(user=user,name=name,species=species,amount=amount,spiritStatus=spiritStatus,causeOfDeath=causeOfDeath,description=description)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request,id):
    if request.method=='DELETE':
        Item.objects.get(pk=id).delete()
        return HttpResponse(b"DELETED",status=201)
    return HttpResponseNotFound

@csrf_exempt
def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))




