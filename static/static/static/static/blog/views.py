from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def blog(request):
    return render(request, 'blog/blog.html')

def blog1(request):
    return render(request, 'blog/blog1.html')

def blog2(request):
    return render(request, 'blog/blog2.html')

def blog3(request):
    return render(request, 'blog/blog3.html')

def blog4(request):
    return render(request, 'blog/blog4.html')

def blog5(request):
    return render(request, 'blog/blog5.html')

def blog6(request):
    return render(request, 'blog/blog6.html')
