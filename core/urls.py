from django.urls import path

from . import views

urlpatterns = [
    path('dictionary1/', views.dictionary1, name='dictionary1'),
]
