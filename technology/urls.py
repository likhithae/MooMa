from django.urls import re_path, include, path
from . import views

app_name = 'technology'

urlpatterns = [

    path('', views.technology, name='technology'),
]