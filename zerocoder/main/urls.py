from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new, name='page2'),
    path('feeding/', views.feeding, name='page3'),
    path('play/', views.play, name='page4'),
]
