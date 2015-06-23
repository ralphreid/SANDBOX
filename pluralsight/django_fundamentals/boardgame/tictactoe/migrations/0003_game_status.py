# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0002_remove_game_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('F', 'First Player Wins'), ('S', 'Second Player Wins'), ('D', 'Draw')], default='A', max_length=1),
        ),
    ]
