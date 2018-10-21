from django.urls import path  #This file is written in pages folder

from .views import MyProfileView
from .views import MyTimelineView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
     path('',MyProfileView.as_view(),name='profile'),
     path('timeline/',MyTimelineView.as_view(),name='timeline'),
     #path('test_project/static',MyTimelineView.as_view(),name='image')
        #name is optional

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)