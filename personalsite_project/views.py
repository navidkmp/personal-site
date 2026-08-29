from django.shortcuts import render
from contactus_app.models import Footer, Message


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        family = request.POST.get("family")
        message = request.POST.get("message")
        Message.objects.create(name=name, email=email, phone=phone, family=family, message=message)




    footer = Footer.objects.all().last()
    return render(request, 'ind.html', context={'footer': footer})



