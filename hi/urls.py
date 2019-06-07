from django.urls import path
from . import views

urlpatterns = [

    path('<int:blog_id>/', views.detail, name="detail"),
    path('send/', views.send, name="send"),
    path('create/', views.create, name="create"),
    ]