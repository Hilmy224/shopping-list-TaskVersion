from django.forms import ModelForm
from main.models import Item
from django import forms   
from django.contrib.auth.models import User   

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name","species", "amount","causeOfDeath","spiritStatus","description"]

    # Something like required to finish all before submitting
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)