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
		related_name="invatations_received",
		on_delete=models.CASCADE
	)
	message = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True)
