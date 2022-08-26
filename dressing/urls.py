from django.urls import path
from . import views

app_name = 'dressing'

urlpatterns = [
     path('',views.party, name='party'),
     path('index',views.index, name='index'),
     path('party',views.party, name='party'),
     path('index1',views.index1, name='index1'),
     path('index2',views.index2, name='index2'),
]
