from django.urls import path  #This file is written in pages folder

from .views import HomePageView
from .views import AboutPageView

urlpatterns=[
     path('',HomePageView.as_view(),name='home'),
     path('about/',AboutPageView.as_view(),name='about')   #name is optional

]