from django.urls import path
from . import views

urlpatterns = [
    path('', home),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<id>/', views.detail, name='detail')
]
