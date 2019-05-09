from django.db import models
from django.contrib.auth.models import User


class Invitation(models.Model):
	from_user = models.ForeignKey(
		User,
		related_name="invitations_sent",
		on_delete=models.CASCADE
	)
	to_user = models.ForeignKey(
		User,
		related_name="invitations_received",
		on_delete=models.CASCADE,
		verbose_name="User to invite",
		help_text="Please select a user you want to play a game with"
	)
	message = models.CharField(
		max_length=200,
		blank=True,
		verbose_name="Optional message",
		help_text="Friendly message"
	)
	timestamp = models.DateTimeField(auto_now_add=True)
