from django.forms import ModelForm
from .models import EstateObject


class AddObjectForm(ModelForm):
    class Meta:
        model = EstateObject
        exclude = ['media_files']