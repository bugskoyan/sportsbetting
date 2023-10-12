import django_filters
from bets.models import Event

class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Event
        fields = [
            'name',
            'datetime',
            'sports_choice'
        ]