from django.db import models
from django.contrib.auth.models import User  # Taking advantage of a Built-In user class


class Game(models.Model):
    # Remember all django models must inherit from the Django base model class 'models'
    first_player = models.ForeignKey(User, related_name="games_first_player")
    second_player = models.ForeignKey(User,related_name="games_second_player")
    next_to_move = models.ForeignKey(User, related_name="games_to_move")
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300)
    game = models.ForeignKey(Game)  # Added relationship of Move to Games - Many MOVES have a relationship to same Game
