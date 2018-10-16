from django.urls import path  #This file is written in pages folder

from .views import HomePageView

urlpatterns=[
     path('',HomePageView.as_view(),name='home')   #name is optional

]