from django.shortcuts import render


# Home Page
def home(request):
    return render(request, "home.html")


# About Me Page
def about(request):
    return render(request, "about.html")


# Skills Page
def skills(request):
    return render(request, "skills.html")


# Projects Page
def projects(request):
    return render(request, "projects.html")


# Education Page
def education(request):
    return render(request, "education.html")


# Contact Page
def contact(request):
    return render(request, "contact.html")




# Create your views here.
