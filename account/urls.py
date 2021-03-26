from django.contrib.auth.decorators import login_required
from django.urls import include, path

from .views import Profile
from .views_account import Forget, Login, Logout, Register
from .views_address import AddressDetail
from .views_bank import BankDetail
from .views_company import CompanyDetail
from .views_entity import EntityDetail
from .views_representative import RepresentativeDetail

#accont related urls
urlpatterns=[
    path('',login_required(Profile),name='profile'),
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('forget/',Forget.as_view(),name='forget'),

# company related work here
    path('representativedetail/',login_required(RepresentativeDetail.as_view()),name='representativedetail'),
    path('companydetail/',login_required(CompanyDetail.as_view()),name='companydetail'),
    path('entitydetail/',login_required(EntityDetail.as_view()),name='entitydetail'),
    path('bankdetail/',login_required(BankDetail.as_view()),name='bankdetail'),
    path('addressdetail/',login_required(AddressDetail.as_view()),name='addressdetail')
]
