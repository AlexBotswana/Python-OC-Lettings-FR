# urls pour les profiles

from django.urls import path
from . import views
from . import errors

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]

# Assign custom error handlers
handler404 = errors.handler404
handler500 = errors.handler500
