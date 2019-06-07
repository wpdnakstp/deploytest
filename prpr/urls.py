"""prpr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import hi.views
import portfolio.views
from django.conf import settings # 이건일단 외워야되는데, 세팅에서 url설정한거 쓸거니까 
from django.conf.urls.static import static # 이것도 일단 외워

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hi.views.home, name="home"),
    path('hi/', include('hi.urls')),
    path('portfolio/', include('portfolio.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# 또는 위에거 지우고 urlpatterns += + static(settings.MEDIA_RUL, document_root=settings.MEDIA_ROOT)
