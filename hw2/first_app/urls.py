from django.urls import path, include
from .views import home, json_reader, dict_, check

urlpatterns = [
    path('', home, name='home'),
    path('items/', json_reader, name='json_reader'),
    path('dict/', dict_, name='dict_'),
    path('checking', check, name='check')
]
