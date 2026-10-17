from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('register/', views.UserRigester.as_view()),
    path('update/<int:pk>/', views.UserUpdate.as_view()),
    path('reservation-history/', views.ResevationHistory.as_view()),
]

router = routers.SimpleRouter()
router.register('passengers', views.PassengerViewSet, basename='passengers')
urlpatterns += router.urls