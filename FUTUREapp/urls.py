from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
      
    path('', views.mainPage, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('places/', views.places_list, name='places_list'),
    path('create/', views.places_create, name='place_create'),
     path('places/update/<int:id>/', views.places_update, name='place_update'),
    path('places/delete/<int:id>/', views.places_delete, name='place_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



