import django_filters
from .models import Room

class RoomFilter(django_filters.FilterSet):
    room_name = django_filters.CharFilter(lookup_expr='qs')

    class Meta:
        model = Room
        fields = ['room_name']



