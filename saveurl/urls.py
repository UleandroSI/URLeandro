from django.urls import path
from .views import home, list_dados



urlpatterns = [
    #path('', home, name="home"),
    path('<str:url_parameter>', list_dados, name="list"),
    #path('<str:pk>/', views.DadosList.as_view(), name='list'),

]