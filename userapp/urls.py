from django.urls import path, include
from . import views

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('', views.start_page, name='start_page'),
    path('register/', views.register, name='register'),

]
