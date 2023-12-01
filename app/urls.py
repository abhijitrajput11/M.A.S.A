from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    # path('', views.home),
    path('technology/', views.technology),
    path('APOD/', views.apod),
    path('achievements/', views.achievements),
    path('contact-us/', views.contact),
    path('about-us/', views.about),
    path('', views.loginaccount,name='login'),
    path('signup/',views.signupaccount,name='signup')

]
