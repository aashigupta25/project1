from django.shortcuts import render, HttpResponse
from datetime import datetime
from polls.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):

    context ={
        "variable1":"this is sent",
        "variable2":"Lovely"
    }

    messages.success(request, "This is a text Message")
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")

def About(request):
    return render(request, 'About.html')
    # return HttpResponse("This is Aboutpage")

def Service(request):
    return render(request, 'Service.html')
    # return HttpResponse("This is Servicepage")

def Contact(request):
    
    if request.method =="POST":
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Address = request.POST.get('Address')
        Contact = Contact(Firstname = Firstname, Lastname = Lastname, Email = Email, Password = Password, Address = Address, date = datetime.today())
        Contact.save()

        messages.success(request, 'Your message has been sent!')

    return render(request, 'Contact.html')


    # return HttpResponse("This is Contactpage")

def Blog(request):
    return render(request, 'Blog.html')

    # return HttpResponse("This is Blogpage")

  
