from rest_framework import serializers
from django.contrib.auth.models import User

from bets.models import Event, Bet, BetHistory, Bookmaker, Odds


class EventSerializer(serializers.ModelSerializer):
    


    class Meta:
        model = Event
        fields = '__all__'


class BetSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Bet
        fields = '__all__'


class BetHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BetHistory
        fields = '__all__'


class BookmakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmaker
        fields = '__all__'


class OddsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odds
        fields = '__all__'