# urls pour les letting

from django.urls import path
from . import views
from . import errors

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]

# Assign custom error handlers
handler404 = errors.handler404
handler500 = errors.handler500
