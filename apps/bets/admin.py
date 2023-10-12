from django.contrib import admin

from bets.models import Event, Bet, BetHistory, Bookmaker, Odds


admin.site.register(Event)
admin.site.register(Bet)
admin.site.register(BetHistory)
admin.site.register(Bookmaker)
admin.site.register(Odds)

