from django.urls import path, include
from .views import register, specialists, news, gallery

urlpatterns = [
    path('register/', register, name='register'),
    path('specialists/', specialists, name='specialists'),
    path('news/', news, name='news'),
    path('gallery/', gallery, name='gallery'),
    path('', include('django.contrib.auth.urls')),
]
