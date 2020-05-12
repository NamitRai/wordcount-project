
from django.urls import path
from wordcount import views
urlpatterns = [
    path('', views.home),
    path('countword/', views.count, name="countword"),
    path('countchar/', views.countchar, name="countchar"),
    path('countfreq/', views.countfreq, name="countfreq"),
    path('about/', views.about, name="about"),
]
