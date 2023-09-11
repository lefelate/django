from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('resume', views.resume, name='resume'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('services', views.services, name='services'),
    path('addBlog', views.addBlog, name='addBlog'),
    path('blog', views.blog, name='blog'),
]
