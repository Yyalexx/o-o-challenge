from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import EstateObject
from .forms import AddObjectForm


# Create your views here.
class ObjectsList(ListView):
    model = EstateObject
    template_name = 'objects.html'
    context_object_name = 'objects'


class ObjectDetails(DetailView):
    model = EstateObject
    template_name = 'object.html'
    context_object_name = 'object'


class ObjectCreate(CreateView):
    template_name = 'object_create.html'
    form_class = AddObjectForm


class ObjectUpdate(UpdateView):
    template_name = 'object_create.html'
    form_class = AddObjectForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return EstateObject.objects.get(pk=id)


class ObjectDelete(DeleteView):
    template_name = 'object_delete.html'
    queryset = EstateObject.objects.all()
    success_url = reverse_lazy('objects_list')