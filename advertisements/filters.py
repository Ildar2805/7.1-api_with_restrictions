from django_filters import rest_framework as filters, DateTimeFromToRangeFilter, NumberFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateTimeFromToRangeFilter()
    creator = NumberFilter()


    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
