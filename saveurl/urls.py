from django.urls import path
from .views import home

app_name = 'saveurl'

urlpatterns = [
    path('', home, name="home"),
    path('list/<str:pk>/', views.DadosList.as_view(), name='list'),

]