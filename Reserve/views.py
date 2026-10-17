from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReservationSerializer
from .models import Reservation, ReservtionPassenger
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Residence.models import Room
from django.shortcuts import get_object_or_404

class Reserve(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():
            result = Reservation.objects.filter(
                room=serializer.validated_data["room"],
                start_date__lt=serializer.validated_data["end_date"],
                end_date__gt=serializer.validated_data["start_date"]
            )

            if result.exists():
                return Response(
                    {"message":"این اتاق در این تاریخ رزرو شده"},
                    status=status.HTTP_400_BAD_REQUEST    
                )
            elif serializer.validated_data["guest_number"] > serializer.validated_data["room"].capacity:
                return Response(
                    {"message":"تعداد مسافران بیشتر از حد مجاز اتاق است"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                serializer.validated_data["user"] = request.user
                passengers = serializer.validated_data.pop('passengers')
                reserved = Reservation.objects.create(**serializer.validated_data)
                for passenger in passengers:
                    ReservtionPassenger.objects.create(reservation=reserved, **passenger)
                return Response(request.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)