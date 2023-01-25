from django.urls import path
from .views import home, listDados



urlpatterns = [
    #path('', home, name="home"),
    path('<str:url_parameter>', listDados, name="list"),
    #path('<str:pk>/', views.DadosList.as_view(), name='list'),

]