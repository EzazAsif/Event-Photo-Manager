from django.urls import path
from . import views

urlpatterns = [
    path('', views.myEvents, name='myEvents'),
    path('myEvents', views.myEvents, name='events'),
    path('myPhotos', views.myPhotos, name='myPhotos'),
    path('addEvents', views.addEvents, name='addEvents'),
    path('addPhotos/<str:eventID>', views.addPhotos, name='addPhotos'),
    path('myEvents/<str:eventID>', views.eventPage, name='eventPage'),
    path('myEvents/<str:eventID>', views.eventPage, name='eventPage'),
    path('publishEvent/<str:eventID>', views.publishEvent, name='publishEvent'),
    path('checkEventStatus/<str:eventID>', views.checkEventStatus, name='checkEventStatus'),
]
