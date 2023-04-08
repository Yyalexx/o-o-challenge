from django_filters import FilterSet


from .models import EstateObject

class ObjectFilter(FilterSet):
    class Meta:
        model = EstateObject
        # fields = '__all__'
        exclude = ['media_files']
