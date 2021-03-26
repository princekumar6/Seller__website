from django.urls import path
from .import views

urlpatterns = [  
    path('admin/',views.admin),
    path('verify/',views.verify),
    path('sendemail/',views.emailsend),
    path('viewdetail/',views.sellerid),
]