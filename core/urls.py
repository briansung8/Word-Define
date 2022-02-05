from django.urls import path

from . import views

urlpatterns = [
    path('', views.dictionary1, name='dictionary1'),
]
