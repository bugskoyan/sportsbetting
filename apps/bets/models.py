from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

class Event(models.Model):

    class Sports(models.TextChoices):
        FOOTBALL = "FT", _("Футбол"),
        BASKETBALL = "BT", _("Баскетбол"),
        TENNIS = "TN", _("Теннис"),

    name: str = models.CharField(
        verbose_name='название события',
        max_length=200
    )
    datetime = models.DateTimeField(
        verbose_name='дата и время начало события'
    )
    sports_choice = models.CharField(
        verbose_name='вид спорта',
        choices=Sports.choices,
        max_length=100
    )

    status = models.CharField(
        verbose_name='статус',
        max_length=20, 
        choices=[('active', 'Активное'), ('completed', 'Завершенное'), ('upcoming', 'Предстоящее')])


    class Meta:
        ordering = ('id',)
        verbose_name = 'событие'
        verbose_name_plural = 'события'

    def __str__(self) -> str:
        return f'{self.name} | {self.sports_choice} | {self.status}'


class Bet(models.Model):
    class BetForm(models.TextChoices):
        WIN = "W", _("Победа"),
        LOSE = "L", _("Проигрыш"),
        DRAW = "D", _("Ничья")

    user = models.ForeignKey(
        verbose_name='пользователь, сделавший ставку',
        to=User,
        max_length=100,
        on_delete=models.CASCADE
    )
    bet_event = models.ForeignKey(
        verbose_name='событие, на которое сделана ставка',
        to=Event,
        max_length=100,
        on_delete=models.CASCADE
    )
    bet_form = models.CharField(
        verbose_name='вид ставки',
        choices=BetForm.choices,
        max_length=100
    )
    bet_sum : int = models.DecimalField(
        verbose_name='сумма ставки',
        validators=[
            MinValueValidator(0, message = "бомж"), 
        ],
        decimal_places=3,
        max_digits=1000
        
    )
    bet_cf = models.DecimalField(
        verbose_name='коэффициент ставки',
        max_digits=10,
        decimal_places=2
    )
    

    @property
    def bet_win(self):
        return self.bet_sum * self.bet_cf

    def __str__(self):
        return f'{self.bet_win}'
    


    class Meta:
        ordering = ('id',)
        verbose_name = 'ставка'
        verbose_name_plural = 'ставки'

    def __str__(self) -> str:
        return f'{self.user} | {self.bet_event} | {self.bet_cf}'
    


class BetHistory(models.Model):
    user = models.ForeignKey(
        verbose_name='пользователь',
        to=User, 
        on_delete=models.CASCADE)
    bet_datetime = models.DateTimeField(
        verbose_name='дата и время сделанной ставки'
    )
    status = models.CharField(
        verbose_name='статус ставки',
        max_length=20, 
        choices=[('won', 'Выигрыш'), ('lost', 'Проигрыш'), ('pending', 'Ожидание')])
    winnings_or_loss = models.DecimalField(
        verbose_name='выигрыш или проигрыш по ставке',
        max_digits=10, 
        decimal_places=2)
    bet_details = models.TextField(
        verbose_name='подробности о ставке'
    )


    class Meta:
        ordering = ('id',)
        verbose_name = 'история ставки'
        verbose_name_plural = 'история ставок'

    def __str__(self) -> str:
        return f'{self.user} | {self.status} | {self.bet_datetime}'


class Bookmaker(models.Model):
    name = models.CharField(
        verbose_name='название компании',
        max_length=100)
    contact_info = models.CharField(
        verbose_name='контактная информация',
        max_length=255)

    class Meta:
        ordering = ('id',)
        verbose_name = 'букмекер'
        verbose_name_plural = 'букмекеры'

    def __str__(self) -> str:
        return f'{self.name} | {self.contact_info}'
    
    
class Odds(models.Model):
    event = models.ForeignKey(
        verbose_name='событие',
        to=Event, 
        on_delete=models.CASCADE)
    bet_type = models.CharField(
        verbose_name='вид ставки',
        max_length=50)
    value = models.DecimalField(
        verbose_name='значение коэффициента',
        max_digits=5, 
        decimal_places=2)
    

    class Meta:
        ordering = ('id',)
        verbose_name = 'коэффициент'
        verbose_name_plural = 'коэффициенты'

    def __str__(self) -> str:
        return f'{self.event} | {self.bet_type} | {self.value}'
