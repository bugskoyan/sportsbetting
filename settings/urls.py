
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.bets.views import EventViewSet, BetViewSet, BetHistoryViewSet, BookmakerViewSet, OddsViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'bets', BetViewSet)
router.register(r'bet_history', BetHistoryViewSet)
router.register(r'bookmakers', BookmakerViewSet)
router.register(r'odds', OddsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls), name='bets'),
]
