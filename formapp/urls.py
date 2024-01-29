from django.urls import path
from .views import FormClass, ListClass, deletePost

app_name = 'formapp'
urlpatterns = [
    path('', FormClass.as_view(), name='form'),
    path('list/', ListClass.as_view(), name='list'),
    path('<str:pk>/delete/', deletePost, name='deletePost'),
]