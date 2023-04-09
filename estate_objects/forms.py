from django.forms import ModelForm, IntegerField, NumberInput


from .models import EstateObject


class AddObjectForm(ModelForm):
    area = IntegerField(
        label='Площадь',
        widget=NumberInput(attrs={"class":"myfield"})
        )
    class Meta:
        model = EstateObject
        exclude = ['media_files']
        # fields = '__all__'
