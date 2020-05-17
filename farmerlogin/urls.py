from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'farmerlogin'

urlpatterns = [
    path('',views.userlogin,name='userlogin'),
    path('logout/',views.userlogout,name='userlogout'),
    #path('',auth_views.login,{'template_name': 'farmerlogin/login.html'},name='login'),
    path('signup/', views.signup, name='signup'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]