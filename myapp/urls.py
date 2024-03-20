from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import Detail, TeamMembersView, SignUpView

app_name = 'myapp'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.user_login, name='login'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('<int:type_no>/',Detail.as_view(),name='detail'),       #for CBV
    path('team/',TeamMembersView.as_view(),name='team'),                #LAB 6 PART 2
    path('items/', views.items, name='items'),
    path('placeorder/',views.placeorder,name='placeorder'),
    path("itemsearch/", views.item_search,name='itemsearch'),
    path("items/<int:item_id>/", views.itemdetail, name='item_detail'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.user_login, name='login'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('myorders/', views.myorders, name='myorders'),
]