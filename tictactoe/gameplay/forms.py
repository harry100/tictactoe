from django.forms import ModelForm

from .models import Move


class MoveForm(ModelForm):
	class Meta:
		model = Move
		exclude = []
