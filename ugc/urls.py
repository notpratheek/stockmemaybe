from django.conf.urls import patterns, url

from ugc import views

urlpatterns = patterns('',
			
			url(r'^$', views.UGCView.as_view(), name = 'ugc')
)
