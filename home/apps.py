from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'home'
    
    def ready(self): #method just to import the signals
    	import users.signals
