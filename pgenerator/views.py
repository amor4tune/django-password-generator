from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'pgenerator/home.html')

def about(request):
    return render(request, 'pgenerator/about.html')

def contacts(request):
    return render(request, 'pgenerator/contacts.html')

def password(request):

    characters= list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('~`!@#$%^&*()_-+="/?.>,<'))

    if request.GET.get('numbers'):
        characters.extend(list('0987654321'))

    lenght = int(request.GET.get('lenght', 12))

    thepassword= ''

    for x in range (lenght):
        thepassword += random.choice(characters)
    return render(request, 'pgenerator/password.html', {'password': thepassword})
