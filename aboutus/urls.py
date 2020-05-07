from django.urls import re_path, include, path
from . import views

app_name = 'aboutus'

urlpatterns = [

    path('', views.aboutus, name='aboutus'),
]