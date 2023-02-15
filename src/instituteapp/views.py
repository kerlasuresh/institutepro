from django.shortcuts import render
from .models import ServicesData
from .models import FeedbackData
from .models import ContactData
import datetime
date1=datetime.datetime.now()

def homePage(request):
    return render(request,'homePage.html')

def contactPage(request):
    if request.method=='GET':
        return render(request,'contactPage.html')

    else:
        ContactData(
        F_Name=request.POST.get('fname'),
        L_Name=request.POST.get('lname'),
        Email=request.POST.get('email'),
        Mobile=request.POST.get('mobile'),
        Location=request.POST.get('loc')
        ).save()
        return render(request,'contactPage.html')

def servicesPage(request):
    course=ServicesData.objects.all()
    return render(request,'servicesPage.html',{'course':course})

def feedbackPage(request):
    if request.method=='GET':
        feedbacks=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedbackPage.html',{'feedbacks':feedbacks})

    else:
        FeedbackData(
        Name=request.POST.get('name'),
        Rating=request.POST.get('rating'),
        Date=date1,
        Feedback=request.POST.get('feedback')
        ).save()
        feedbacks=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedbackPage.html',{'feedbacks':feedbacks})

def galleryPage(request):
    return render(request,'galleryPage.html')
