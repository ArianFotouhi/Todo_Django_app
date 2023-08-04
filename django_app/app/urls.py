from django.urls import path
from app import views

urlpatterns =[
    path('', views.todos, name='todos'),
    path('<int:pk>', views.todo, name='todo'),
]