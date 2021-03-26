from django.urls import include, path

from .views_account import Login, Register

#accont related urls
urlpatterns=[
    path('register',Register.as_view(),name='register'),
    path('login',Login.as_view(),name='login'),
    #path('/forget',views_account.password,name='forget')
]

