from rest_framework import serializers
from .models import City, Hotel, Room, Comment

class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class HotelListSerializer(serializers.ModelSerializer):
    get_avg_rate = serializers.ReadOnlyField()

    class Meta:
        model = Hotel
        fields = ["id", "name", "star", "get_avg_rate"]


class RoomSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ["hotel"]
    
    def get_total_price(self, obj):
        night = self.context["night"]
        return obj.price * night
    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["hotel"]


class HotelDetailSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField(read_only=True)
    room = RoomSerializer(many=True)
    comments = CommentSerializer(many=True)
    
    class Meta:
            model = Hotel
            fields = "__all__"


class HotelFilterSerializer(serializers.Serializer):
     start_date = serializers.DateField(required=True)
     end_date = serializers.DateField(required=True)
     capacity = serializers.IntegerField(required=True)