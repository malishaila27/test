from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class MyProfileView(TemplateView):
	template_name='profile.html'

class MyTimelineView(TemplateView):
	template_name='timeline.html'