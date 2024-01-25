from django.urls import path
from .views import FormClass, ListClass

app_name = 'formapp'
urlpatterns = [
    path('form/', FormClass.as_view(), name='form'),
    path('list/', ListClass.as_view(), name='list'),
]