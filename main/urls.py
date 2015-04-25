from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
			#Home page
			url(r'^$',views.IndexView.as_view(),name='index'),
			#About
			url(r'^about$',views.AboutView.as_view(),name='about'),
			#Tools Used
			url(r'^tools$',views.ToolsView.as_view(),name='tools'),
			#Algorithm
			url(r'^algo$',views.AlgoView.as_view(),name='algo'),
			)
