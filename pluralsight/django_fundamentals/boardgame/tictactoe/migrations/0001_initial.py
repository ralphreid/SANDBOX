# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('F', 'First Player Wins'), ('S', 'Second Player Wins'), ('D', 'Draw')], default='A', max_length=1)),
                ('first_player', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='games_first_player')),
                ('next_to_move', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='games_to_move')),
                ('second_player', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='games_second_player')),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('comment', models.CharField(max_length=300)),
                ('game', models.ForeignKey(to='tictactoe.Game')),
            ],
        ),
    ]
