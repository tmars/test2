from django.urls import path
from .import views

app_name = 'appgames'

urlpatterns = [
    path('list/', views.list_games, name="list_games")
]
