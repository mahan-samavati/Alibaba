from rest_framework import generics
from .models import City, Hotel, Room
from .serializers import CityListSerializer, HotelListSerializer, HotelDetailSerializer, HotelFilterSerializer
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HotelFilter
from rest_framework.exceptions import ValidationError
from django.db.models import Prefetch


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer
    permission_classes = [AllowAny,]

class HotelList(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter

    def get_queryset(self):
        query_set = super().get_queryset()

        params = HotelFilterSerializer(data=self.request.query_params)
        if not params.is_valid():
            raise ValidationError("تاریخ ورود و خروج و تعداد نفرات را وارد کنید")

        start_date = params.validated_data["start_date"]
        end_date = params.validated_data["end_date"]

        no_reserve_room = Room.objects.exclude(
            reservation__start_date__lt=end_date,
            reservation__end_date__gt=start_date
        )

        query_set = query_set.filter(
            room__in=no_reserve_room
        ).distinct()

        return query_set


class HotelDetail(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer
    permission_classes = [AllowAny,]

    def get_queryset(self):
        query_set = super().get_queryset()
    
        params = HotelFilterSerializer(data=self.request.query_params)
        if not params.is_valid():
            raise ValidationError("تاریخ ورود و خروج و تعداد نفرات را وارد کنید")
        
        start_date = params.validated_data["start_date"]
        end_date = params.validated_data["end_date"]
        capacity = params.validated_data["capacity"]

        no_reserve_room = Room.objects.exclude(
            reservation__start_date__lt=end_date,
            reservation__end_date__gt=start_date,
        ).filter(
            capacity__gte=capacity
        )

        return query_set.prefetch_related(
            Prefetch("room", queryset=no_reserve_room)
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()

        params = HotelFilterSerializer(data=self.request.query_params)
        if not params.is_valid():
            raise ValidationError("تاریخ ورود و خروج را وارد کنید")
                
        start_date = params.validated_data["start_date"]
        end_date = params.validated_data["end_date"]
        
        night = (end_date - start_date).days
        context['night'] = night
        return context