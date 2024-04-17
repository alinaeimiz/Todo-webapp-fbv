from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.todo, name='todo'),
    path('active/<int:pk>',views.active, name='active')
]