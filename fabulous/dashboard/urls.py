from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index1', views.index1, name='index1'),

    path('fan11', views.fan11, name='fan11'),
path('garage1', views.garage1, name='garage1'),
path('camera1', views.camera1, name='camera1'),
path('music1', views.music1, name='music1'),
    path('light', views.light, name='light'),
    path('light1', views.light1, name='light1'),
    path('light2', views.light2, name='light2'),
    path('light3', views.light3, name='light3'),
    path('light4', views.light4, name='light4'),
    path('light5', views.light5, name='light5'),
    path('light6', views.light6, name='light6'),
    path('light7', views.light7, name='light7'),
path('fan', views.fan, name='fan'),
path('fan1', views.fan1, name='fan1'),
path('fan2', views.fan2, name='fan2'),
path('fan3', views.fan3, name='fan3'),
path('fan4', views.fan4, name='fan4'),
path('fan5', views.fan5, name='fan5'),
path('fan6', views.fan6, name='fan6'),
path('fan7', views.fan7, name='fan7'),
path('garage', views.garage, name='garage'),
path('camera', views.camera, name='camera'),
path('music', views.music, name='music'),
    path(r'^view$', views.view_detail, name='view_detail'),

]