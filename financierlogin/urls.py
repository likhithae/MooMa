from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


app_name = 'financierlogin'

urlpatterns = [
    path('',views.userlogin,name='userlogin'),
    path('logout/',views.userlogout,name='userlogout'),
    #path('',auth_views.login,{'template_name': 'farmerlogin/login.html'},name='login'),
    path('signup/', views.signup, name='signup'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('ajax/load_districts/', views.load_districts, name='load_districts'),
    path('ajax/load_cities/', views.load_cities, name='load_cities'),
    path('ajax/load_banks/', views.load_banks, name='load_banks'),
    path('ajax/load_branches/', views.load_branches, name='load_branches'),
    path('ajax/load_ifscs/', views.load_ifscs, name='load_ifscs'),
]