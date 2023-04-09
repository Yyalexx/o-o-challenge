from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from app import settings
from .models import EstateObject, Solution, AdditionalFields
from .forms import AddObjectForm, SolutionForm
from .filters import ObjectFilter


# Create your views here.
class ObjectsList(ListView):
    model = EstateObject
    template_name = 'objects.html'
    context_object_name = 'objects'


class ObjectDetails(DetailView):
    model = EstateObject
    template_name = 'object.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["solution"] = Solution.objects.filter(pk=self.kwargs.get('pk')).first()
        context["additional_fields"] = AdditionalFields.objects.filter(obj_id=self.kwargs.get('pk'))
        return context


class ObjectCreate(CreateView):
    template_name = 'object_create.html'
    form_class = AddObjectForm


class ObjectUpdate(UpdateView):
    template_name = 'object_create.html'
    form_class = AddObjectForm

    def get_object(self, **kwargs):
        obj_id = self.kwargs.get('pk')
        return get_object_or_404(EstateObject, pk=obj_id)


class ObjectDelete(DeleteView):
    template_name = 'object_delete.html'
    queryset = EstateObject.objects.all()
    success_url = reverse_lazy('objects_list')


class ObjectSearch(ListView):
    model = EstateObject
    template_name = 'object_search.html'
    context_object_name = 'objects'
    ordering = ['-pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ObjectFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SolutionUpdate(UpdateView):
    template_name = 'solution_create.html'
    form_class = SolutionForm

    def get_object(self, **kwargs):
        obj_id = self.kwargs.get('pk')
        return get_object_or_404(Solution, pk=obj_id)

    def get_success_url(self, **kwargs):
        obj_id = self.kwargs.get('pk')
        url = f'{settings.SITE_URL}/estate_objects/{obj_id}'
        return url
