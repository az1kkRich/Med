from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('galery/', galery, name='galery'),
    path('timatables/', timatables, name='timatables'),
    path('departaments/', departaments, name='departaments'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('make/', make, name='make'),
    path('new/<int:pk>/', member_detail.as_view(), name='member_detail'),
    path('page/<int:pk>/', page_detail.as_view(), name='page_detail'),
]