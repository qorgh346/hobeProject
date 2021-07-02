"""firstHobeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))ls
"""
from django.contrib import admin
from django.urls import path
from firstHobeApp import views as first_views 
from wordcountapp import views as wc_views


urlpatterns = [
    path('admin/', admin.site.urls),                                            
    path('',first_views.welcome,name="welcome" ),
    path('hello/',first_views.hello,name="hello"),
    path('wc/',wc_views.StartWord_Count,name="wc"),
    path('wc/result',wc_views.word_count,name="result"),
    
]
