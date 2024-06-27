import django_filters
from .models import Room

class RoomFilter(django_filters.FilterSet):
    room_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Room
        fields = ['room_name']


