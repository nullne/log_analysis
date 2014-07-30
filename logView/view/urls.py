from django.conf.urls import patterns, url
from view import views

urlpatterns = patterns('',
        url(r'^svg/$', views.showSVG, name='show'),
        url(r'^upload$', views.upload, name='upload'),
        )
