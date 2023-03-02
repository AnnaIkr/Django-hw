from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    creator = filters.ModelMultipleChoiceFilter(to_field_name="creator_id", queryset=Advertisement.objects.all())
    status = filters.CharFilter(to_field_name="status")

    class Meta:
        model = Advertisement
