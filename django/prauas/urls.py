from django.urls import path

from . import views

urlpatterns = [
    path('details/<int:pk>', views.SensorDetails.as_view()),
    path('webview/', views.webview)
]

