from . import views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
app_name = 'app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^message/$', views.SendSmsCreateView.as_view(), name='message'),
    url(r'^statistics/$', views.statistics, name='statistics'),
]