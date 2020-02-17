from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mesa/', views.mesas, name='mesas'),
    path('mesa/<int:mesa_id>/', views.mesa, name='mesa'),

]