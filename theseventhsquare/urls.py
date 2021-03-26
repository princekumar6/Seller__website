"""theseventhsquare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('account/',include('account.urls')),
    path('admin/', admin.site.urls),
    path('seller/', include('seller.urls')),
    path('', views.index),
    path('email/<str:em>/', views.emailverify),
    path('login/', views.s_login),
    path('afterlogin/', views.s_afterlogin),
    path('register/', views.s_register),
    path('verify/', views.s_afterregister.as_view()),
    path('logout/', views.s_logout),
    path('contact/', views.contact),
    path('aftercontact/', views.aftercontact),
    path('docverify/', views.docverify),
    path('afterbankverify/', views.afterbankverify),
    path('afterentityverify/', views.afterentityverify),
    path('afterrepverify/', views.afterrepverify),
    path('partner/', views.partner),
    path('afterpartner/', views.afterpartner),
    path('corporate/', views.corporate),
    path('aftercorporate/', views.aftercorporate),
    path('coming-soon/', views.coming),
    path('about/', views.about),
    path('careers/', views.careers),
    path('commercial-terms/', views.comterm),
    path('guidelines/', views.selguide),
    path('Profile/', views.dash_profile),
    path('afterdashacc/', views.dash_acc_edit),
    path('afterdashaccl/', views.dash_acc_editl),
    path('policy/', views.policy),
    path('index1/', views.index1),

    path('quick/', views.quick),

    path('marketplace/', views.marketplace),
    path('terms/', views.terms),
    path('faqs/<str:f>/', views.dash_faqs),
    path('pricecalculator/', views.pricecalculator),
    path('notify_read/', views.notify_read),
    path('newproduct/', views.dash_new),
    path('afternew/', views.after_new),
    path('mobileverify/', views.mobileverify),
    path('viewproducts/', views.dash_view),
    path('preview/<str:prod>/', views.preview),
    path('dlt_new/<str:dl>/', views.dlt_new),
    path('edit_new/<str:prod>/', views.edit_new),
    path('editproduct/<str:title>/', views.edit_view),
    # path('<str:name>/',views.prod_view),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
