from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Muhammad Hilmy Abdul Aziz',
        'class': 'PBP D',
        'description': 'A corpse that has died shamefully in battle.His corpse is haunted with vengefull spirits seeking his demise even after death',
        'causeOfDeath':'An arrow to the knee',
        'spiritStatus': 'Tormented Spirit'
    }

    return render(request, "main.html", context)