from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
	frist_player = models.ForeignKey(User, on_delete=models.CASCADE,
			related_name="games_first_player"
			)
	second_player = models.ForeignKey(User, on_delete=models.CASCADE,
			related_name="games_second_player"
			)
	start_time = models.DateTimeField(auto_now_add=True)
	last_active = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=1, default='F')


class Move(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()
	comment = models.CharField(max_length=200, blank=True)
	by_first_player = models.BooleanField()
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
