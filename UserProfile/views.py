from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer,UserUpdateSerializer,PassengerSerializer
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from .models import User, Passenger
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from Reserve.serializers import ReservationSerializer


class UserRigester(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdate(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsOwner,]


class PassengerViewSet(viewsets.ModelViewSet):
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return self.request.user.passengers.all()

    def create(self, request, *args, **kwargs):
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["creator"] = request.user
            Passenger.objects.create(**serializer.validated_data)
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResevationHistory(ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return self.request.user.reservation_user.all()



# {
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc5MjI5OTQ2NiwiaWF0IjoxNzkyMjEzMDY2LCJqdGkiOiIwMzlkN2RlMmQ0NGY0OTdhOWE2ZTZjYzIxZDY2M2M3OSIsInVzZXJfaWQiOiIxNiJ9._nsEa5HCxiE4waVGPENiW7673Bs4oaXEi2LFuiWlzAY",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkyMjk5NDY2LCJpYXQiOjE3OTIyMTMwNjYsImp0aSI6ImRhMGU2ZDY1MzhhMDQ1Mjc4YzA4ZDU2YTQ1ZWE2YmNiIiwidXNlcl9pZCI6IjE2In0.goEWZVlt-8gUUVIUAU_JJFkJmGhJdUpbpeeDj95z1Lo"
# }