from django.urls import path
from .import views

urlpatterns = [  
    path('',views.forum),
    path('newdis/',views.newdis),
    path('addnew/',views.addnew),
    path('addnewc/<str:prod>/',views.addnewc),
    path('<str:prod>/',views.disc),
    path('<str:prod>/addcomment/',views.cmnt),
]