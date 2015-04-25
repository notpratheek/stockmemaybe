from django.shortcuts import render_to_response,render,get_object_or_404
import re
import urllib.request
from django.views.generic import View,ListView
from django.utils import timezone
from django.core import serializers
from ugc.models import Messages
from datetime import datetime, timedelta

#Class for the home page
class IndexView(ListView):
	template_name = 'main/index.html'
	Messages.objects.filter(created_at__lte = timezone.now() - timedelta(days=3)).delete()
	#returns queryable data subset, if any
	def get_queryset(self):
		return
class AboutView(ListView):
	template_name = 'main/about.html'
	#returns queryable data subset, if any
	def get_queryset(self):
		return

class ToolsView(ListView):
	template_name = 'main/tools.html'
	#returns queryable data subset, if any
	def get_queryset(self):
		return

class AlgoView(ListView):
	template_name = 'main/algo.html'
	#returns queryable data subset, if any
	def get_queryset(self):
		return
