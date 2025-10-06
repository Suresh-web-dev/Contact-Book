from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from .models import contact

# Create your views here.

def index(request):
    contact_list = contact.objects.all()
    obj = {"contact_list" : contact_list}
    return render(request, "index.html",obj)

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username,email=email,password=password)
        login(request,user)
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect(index)

        else:
            messages.error(request,"Username or password was incorrect....")
            return redirect(index)
    return render(request, "index.html")
    

def logout_view(request):
    logout(request)
    return redirect(login_view)


def add_contact(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        name = request.POST.get("name").upper()
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        address = request.POST.get("address")

        contact.objects.create(user = request.user, image = image, name = name, phone_number = phone_number, email = email, address = address)
        return redirect(index)
    return render(request,"Add_contact.html")


def view_profile(request,id):
    contacts = contact.objects.get(id=id)
    obj = {"contact" : contacts}
    return render(request,"view_profile.html",obj)


def delete_contact(request,id):
    del_contact = contact.objects.get(id=id)
    del_contact.delete()
    return redirect(index)



def edit_contact(request, id):
    contacts = get_object_or_404(contact, id=id)

    if request.method == "POST":
        new_image = request.FILES.get("new_image")
        new_name = request.POST.get("new_name").upper()
        new_phone_number = request.POST.get("new_phone_number")
        new_email = request.POST.get("new_email")
        new_address = request.POST.get("new_address")

        if new_image:
            contacts.image = new_image
        contacts.name = new_name
        contacts.phone_number = new_phone_number
        contacts.email = new_email
        contacts.address = new_address

        contacts.save()

        return redirect(view_profile, id=contacts.id)

    context = {"contact": contacts}
    return render(request, "view_profile.html", context)



def search(request):
    if request.method == "POST":
        name = request.POST.get("name").upper()

        if contact.objects.filter(name=name).exists():
            contacts = contact.objects.filter(name=name)
            obj = {"contacts": contacts}

        else:
            obj = {"error": "Contact not found...😔"}

        return render(request, "index.html", obj)
