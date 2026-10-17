from django.db import models
from django.db.models import Avg
from .hoteltype import HOTEL_TYPE

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="city")
    name = models.CharField(max_length=50)
    star = models.PositiveSmallIntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    facilities = models.TextField(blank=True)
    type = models.CharField(max_length=30, choices=HOTEL_TYPE)

    @property
    def get_avg_rate(self):
       return self.comments.aggregate(rate=Avg("rate"))
    

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='room')
    price = models.PositiveBigIntegerField()
    capacity = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50)


class Comment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comments')
    rate = models.PositiveSmallIntegerField()
    body = models.TextField()