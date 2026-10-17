from rest_framework import serializers
from .models import User, Passenger

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "confirm_password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError('passwords must match!')
        return attrs
    
    def create(self, validated_data):
        del validated_data["confirm_password"]
        return User.objects.create_user(**validated_data)

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "national_code", "password", "email"]


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        exclude = ["creator"]