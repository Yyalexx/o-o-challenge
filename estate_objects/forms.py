from django.forms import ModelForm, IntegerField, NumberInput, DateTimeField, DateInput


from .models import EstateObject, Solution


class AddObjectForm(ModelForm):
    area = IntegerField(
        label='Площадь',
        widget=NumberInput(attrs={"class":"myfield"})
        )
    class Meta:
        model = EstateObject
        exclude = ['media_files']
        # fields = '__all__'


class SolutionForm(ModelForm):
    complete_before = DateTimeField(label='Срок исполнения', widget=DateInput(attrs={'type': 'date'}))
    discussion_date = DateTimeField(label='Дата проведения заседания', widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Solution
        exclude = ['obj_id']
        fields = '__all__'
