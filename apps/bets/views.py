from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from django_filters.rest_framework import DjangoFilterBackend

from bets.models import Event, Bet, BetHistory, Bookmaker, Odds
from bets.serializers import EventSerializer, BetSerializer, BetHistorySerializer, BookmakerSerializer, OddsSerializer
from bets.filter import EventFilter


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = EventFilter
    ordering_fields = ['name', 'sports_choice']  
    ordering = ['name', 'sports_choice']

    def get_queryset(self):
        
        queryset = super().get_queryset()

        # ordering_param = self.request.query_params.get('ordering', None)

        # if ordering_param:
        #     if ordering_param in ['price', '-price']:
        #         queryset = queryset.order_by(ordering_param)

        return queryset

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: EventSerializer = EventSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self, 
        request: Request, 
        pk: int = None
    ) -> Response:
        try:
            game = self.queryset.get(pk=pk)
        except Event.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = EventSerializer(instance=game)
        return Response(data=serializer.data)


class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: BetSerializer = BetSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self, 
        request: Request, 
        pk: int = None
    ) -> Response:
        try:
            game = self.queryset.get(pk=pk)
        except Bet.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = BetSerializer(instance=game)
        return Response(data=serializer.data)



class BetHistoryViewSet(viewsets.ModelViewSet):
    queryset = BetHistory.objects.all()
    serializer_class = BetHistorySerializer

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: BetHistorySerializer = BetHistorySerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self, 
        request: Request, 
        pk: int = None
    ) -> Response:
        try:
            game = self.queryset.get(pk=pk)
        except BetHistory.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = BetHistorySerializer(instance=game)
        return Response(data=serializer.data)


class BookmakerViewSet(viewsets.ModelViewSet):
    queryset = Bookmaker.objects.all()
    serializer_class = BookmakerSerializer


    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: BookmakerSerializer = BookmakerSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self, 
        request: Request, 
        pk: int = None
    ) -> Response:
        try:
            game = self.queryset.get(pk=pk)
        except Bookmaker.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = BookmakerSerializer(instance=game)
        return Response(data=serializer.data)


class OddsViewSet(viewsets.ModelViewSet):
    queryset = Odds.objects.all()
    serializer_class = OddsSerializer


    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: OddsSerializer = OddsSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self, 
        request: Request, 
        pk: int = None
    ) -> Response:
        try:
            game = self.queryset.get(pk=pk)
        except Odds.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = OddsSerializer(instance=game)
        return Response(data=serializer.data)

