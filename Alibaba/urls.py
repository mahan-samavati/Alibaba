from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include("UserProfile.urls")),
    path('', include("Residence.urls")),
    path('reservation/', include("Reserve.urls")),
    path('token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]
