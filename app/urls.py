from django.urls import path
from .views import ModelListView


urlpatterns = [
    path('',ModelListView.as_view())
]