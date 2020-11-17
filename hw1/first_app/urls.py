from django.urls import path, include
from .views import home, introduction, dt, solution
# from .views import 

urlpatterns = [
    path('', home, name='home'),
    path('intro/', introduction, name='introduction'),
    path('time/', dt, name='dt'),
    path('dict/', solution, name='solution'),


]