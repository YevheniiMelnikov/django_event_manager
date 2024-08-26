import django_filters

from .models import Event


class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Event
        fields = ["title", "date", "location", "organizer"]
