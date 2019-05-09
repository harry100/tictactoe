from django.forms import ModelForm

from .models import Invitation


class InvitationForm(ModelForm):
	"""docstring for Invitation"""
	class Meta:
		model = Invitation
		exclude = ('from_user', 'timestamp')
