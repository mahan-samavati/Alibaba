from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.CityList.as_view(), name="cities"),
    path('hotels/', views.HotelList.as_view(), name="hotels"),
    path('hotels/<int:pk>/', views.HotelDetail.as_view(), name="hotel_detail"),
]