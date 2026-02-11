from django.urls import path
from . import views

urlpatterns = [
    # path('', views.mainPage),  
    path('', views.mainPage, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('places/', views.places_list, name='mainPage'),
]