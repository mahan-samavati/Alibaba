from  django_filters.rest_framework import FilterSet, filters
from .models import Hotel
from django_filters import RangeFilter

class HotelFilter(FilterSet):

    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains"
    )

    city = filters.CharFilter(
        field_name="city__name",
        lookup_expr="exact",
        required=True
    )

    capacity = filters.NumberFilter(
        field_name="room__capacity",
        lookup_expr="gte",
        required=True,
        distinct=True
    )

    star = filters.NumberFilter(
        field_name="star",
        lookup_expr="exact"
    )

    type = filters.CharFilter(
        field_name="type",
        lookup_expr="exact"
    )

    price = RangeFilter(field_name="room__price")

    
    class Meta:
        model = Hotel
        fields = []

