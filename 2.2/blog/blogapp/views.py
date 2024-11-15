from datetime import date
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from .forms import *
from .models import Entry

def index(request):

    entries = Entry.objects.filter()
    return render(request, 'index.html', {'entries': entries})

def register(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            username = request.POST['login']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                user, created = User.objects.get_or_create(username=username, email=email)
            else:
                messages.warning(request, "Hasła nie są takie same!")
                return redirect('/register')
            if created:
                user.set_password(password)
                user.save()
                return redirect('/login', user)
            else:
                messages.warning(request, "Uzytkownik juz istnieje!")
    if not request.user.is_authenticated:
        form = registerForm
        return render(request, 'register.html', {'form': form})
    else:
        return redirect('login/')

def loginown(request):
    if request.method == "POST":
        form = loginownform(request.POST)
        if form.is_valid():
            username = request.POST["login"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                messages.warning(request, "Wprowadzono zle dane!")
    if request.user.is_authenticated:
        return redirect("/")
    else:
        form = loginownform
        return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/')

def createEntry(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = createEntryForm(request.POST)
            if form.is_valid():
                content = request.POST["content"]
                creatorId = request.user
                addedDate = date.today()

                newEntry = Entry.objects.create(creatorId=creatorId, content=content, addedDate=addedDate)
                newEntry.save()

                return redirect('/')
        return render(request, 'createEntry.html', {'form': createEntryForm})
    else:
        return redirect("/login")

def editEntry(request, pk):
    if request.user.is_authenticated:
        creatorId = Entry.objects.filter(id=pk).values_list('creatorId', flat=True)[0]
        if request.user.id == creatorId:
            if request.method == "POST":
                form = createEntryForm(request.POST)
                if form.is_valid():
                    content = request.POST["content"]
                    Entry.objects.filter(id=pk).update(content=content)
                    return redirect('/')
            content = Entry.objects.filter(id=pk).values_list('content', flat=True)[0]
            return render(request, 'editEntry.html', {'content': content})
        return redirect('/')
    else:
        return redirect("/login")
