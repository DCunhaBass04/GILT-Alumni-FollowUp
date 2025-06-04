from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('mudar_data', views.posts_changetime, name="escolher_data")
]
