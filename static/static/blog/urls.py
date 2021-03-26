from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog),
    path('Explore-SS/', views.blog1),
    path('Ecommerce/', views.blog2),
    path('Seller-Learning/', views.blog3),
    path('Seller/', views.blog4),
    path('Learning/', views.blog5),
    path('Learning1/', views.blog6),
]
