from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import EstateObject


# Create your views here.
class ObjectsList(ListView):
    model = EstateObject
    template_name = 'objects.html'
    context_object_name = 'objects'


class ObjectDetails(DetailView):
    model = EstateObject
    template_name = 'object.html'
    context_object_name = 'object'
