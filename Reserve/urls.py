from django.urls import path
from . import views

urlpatterns = [
    path('reserve/', views.Reserve.as_view()),
]