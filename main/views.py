from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from main.forms import ProductForm
from main.models import Item

# Create your views here.
def show_main(request):
    items = Item.objects.all()
    tempItemCount=0
    for ii in items:
        tempItemCount+=ii.amount
    
    context = {
        'name': 'Muhammad Hilmy Abdul Aziz',
        'class': 'PBP D',
        'products': items,
        'itemCount':tempItemCount,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

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

