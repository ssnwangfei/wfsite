from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.send, name='send'),
    path('recv', views.recv, name='recv'),
    path('send_action', views.send_action, name='send_action'),
    path('recv_action', views.recv_action, name='recv_action'),
    path('delete_action', views.delete_action, name='delete_action'),
]