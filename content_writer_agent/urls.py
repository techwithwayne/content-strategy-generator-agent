from django.urls import path
from . import views

urlpatterns = [
    path('generate-posts/', views.generate_posts, name='generate_posts'),
]
