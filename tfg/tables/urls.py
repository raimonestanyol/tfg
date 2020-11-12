from django.urls import path
from django.contrib import admin

from .views import RegistryListView

urlpatterns = [
    path('', RegistryListView.as_view(), name='registry_list'),
]