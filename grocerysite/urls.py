"""
URL configuration for grocerysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from myapp import views
from myapp.views import Detail, TeamMembersView

app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    path('about/<int:yr>/<int:mth>/', views.about, name='about'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    # path('detail/<int:type_no>/', views.detail, name='detail'),        #for FBV
    path('<int:type_no>/',Detail.as_view(),name='detail'),       #for CBV
    path('team/',TeamMembersView.as_view(),name='team'),                #LAB 6 PART 2
]