from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', include('home.urls'), name='home'),

]
