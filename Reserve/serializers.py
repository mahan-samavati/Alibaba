from rest_framework import serializers
from.models import Reservation, ReservtionPassenger
from django.utils import timezone

class ReservtionPassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservtionPassenger
        exclude = ["reservation"]

class ReservationSerializer(serializers.ModelSerializer):
    passengers = ReservtionPassengerSerializer(many=True)
    get_total_price = serializers.ReadOnlyField()

    class Meta:
        model = Reservation
        exclude = ["user"]

    def validate_start_date(self, value):
        if value < timezone.localdate():
            raise serializers.ValidationError("تاریخ ورود نمیتواند قبل از امروز باشد")
        return value

    def validate(self, attrs):
        if attrs["end_date"] <= attrs["start_date"]:
            raise serializers.ValidationError(
                "تاریخ خروج نمیتواند همان روز یا قبل از ورود باشد"
            )
        if attrs["guest_number"] != len(attrs["passengers"]):
            raise serializers.ValidationError(
                "تعداد مسافران وارد شده با تعداد مسافران که تعیین کردید یکی نیست"
            )
        return attrs

