from django.urls import path
from . import views


urlpatterns = [

    path('kk/', views.portfolio, name="portfolio"),
    
]