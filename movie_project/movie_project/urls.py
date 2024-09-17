from django.contrib import admin
from django.urls import path
from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_movie, name='add_movie'),
    path('', views.movie_list, name='movie_list'),
]
