from django.urls import path

from . import views

urlpatterns = [
    path('custom', views.page, name='page'),
    path('index', views.index, name='index'),
]
