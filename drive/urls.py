"""
URL configuration for bqtbsb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'drive'

urlpatterns = [
    path('', views.my_drive, name="my_drive"),
    path('<int:id>', views.delete_file, name="delete_file"),
    path('<str:key>', views.filter_file, name="filter_file"),
    path('view_file/<int:id>', views.file_viewer, name='file_viewer'),
]
