# Generated by Django 4.2.2 on 2023-10-12 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='odds',
            options={'ordering': ('id',), 'verbose_name': 'коэффициент', 'verbose_name_plural': 'коэффициенты'},
        ),
    ]