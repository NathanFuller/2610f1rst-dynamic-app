#This is the urls.py for the 'f1rst' app. Do not confuse it with the one in dynamic_django, which is the project one.
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^diff$', views.diff, name='different'),
]
