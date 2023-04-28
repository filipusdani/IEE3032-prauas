from django.urls import path

from . import views

urlpatterns = [
    path('webview/', views.home, name='base-home'),
    path('api/sensor/', views.api, name='api')
]

