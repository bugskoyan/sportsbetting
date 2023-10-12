# Generated by Django 4.2.2 on 2023-10-12 12:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название компании')),
                ('contact_info', models.CharField(max_length=255, verbose_name='контактная информация')),
            ],
            options={
                'verbose_name': 'букмекер',
                'verbose_name_plural': 'букмекеры',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название события')),
                ('datetime', models.DateTimeField(verbose_name='дата и время начало события')),
                ('sports_choice', models.CharField(choices=[('FT', 'Футбол'), ('BT', 'Баскетбол'), ('TN', 'Теннис')], max_length=100, verbose_name='вид спорта')),
                ('status', models.CharField(choices=[('active', 'Активное'), ('completed', 'Завершенное'), ('upcoming', 'Предстоящее')], max_length=20, verbose_name='статус')),
            ],
            options={
                'verbose_name': 'событие',
                'verbose_name_plural': 'события',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Odds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_type', models.CharField(max_length=50, verbose_name='вид ставки')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='значение коэффициента')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bets.event', verbose_name='событие')),
            ],
            options={
                'verbose_name': 'событие',
                'verbose_name_plural': 'события',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='BetHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_datetime', models.DateTimeField(verbose_name='дата и время сделанной ставки')),
                ('status', models.CharField(choices=[('won', 'Выигрыш'), ('lost', 'Проигрыш'), ('pending', 'Ожидание')], max_length=20, verbose_name='статус ставки')),
                ('winnings_or_loss', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='выигрыш или проигрыш по ставке')),
                ('bet_details', models.TextField(verbose_name='подробности о ставке')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'история ставки',
                'verbose_name_plural': 'история ставок',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_form', models.CharField(choices=[('W', 'Победа'), ('L', 'Проигрыш'), ('D', 'Ничья')], max_length=100, verbose_name='вид ставки')),
                ('bet_sum', models.DecimalField(decimal_places=3, max_digits=1000, validators=[django.core.validators.MinValueValidator(0, message='бомж')], verbose_name='сумма ставки')),
                ('bet_cf', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='коэффициент ставки')),
                ('bet_event', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='bets.event', verbose_name='событие, на которое сделана ставка')),
                ('user', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь, сделавший ставку')),
            ],
            options={
                'verbose_name': 'ставка',
                'verbose_name_plural': 'ставки',
                'ordering': ('id',),
            },
        ),
    ]