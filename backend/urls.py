from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_all_coin_info, name="get_all_coin_info"),
    #path('detail/<str:pk>/', views.memberDetail, name="detail"),
    #path('create/', views.memberCreate, name="create"),
    #path('update/<str:pk>/', views.memberUpdate, name="update"),
    #path('delete/<str:pk>/', views.memberDelete, name="delete")
] 