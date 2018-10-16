from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView



# Create your views here.
#def MyHomePage(request):
	#return HttpResponse("Hello World")
class HomePageView(TemplateView):  #TempLateView is default 
		template_name= 'home.html'