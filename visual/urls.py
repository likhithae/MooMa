from django.urls import path
from . import views

app_name = 'visual'

urlpatterns = [
    path('',views.visual,name='visual'),
    path('quantity/',views.quantity,name='quantity'),
    path('quality/',views.quality,name='quality'),
    path('cowhealth/',views.cowhealth,name='cowhealth'),
    path('profile/',views.profile,name='profile'),
]