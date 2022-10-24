from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from apps.libro.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from apps.libro.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.usuario.mixins import *

class idiomalistadoview(SuperUsuarioMixin,ListView):
    model = Idioma
    template_name = 'listadoidioma.html'

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Idioma.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Idiomas'
        context['crear_url'] = reverse_lazy('libro:idioma_crear')
        context['entity'] = 'Idiomas'
        context['listado_url'] = reverse_lazy('libro:idiomalistadoview')

        return context


class idiomaCreateView(SuperUsuarioMixin, CreateView):
    model = Idioma
    form_class = idiomaForm
    template_name = 'crear.html'
    success_url = reverse_lazy('libro:idiomalistadoview')

    #@method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un Idioma'
        context['entity'] = 'Idioma'
        context['listado_url'] = reverse_lazy('libro:idiomalistadoview')
        context['action'] = 'add'
        return context
    

class idiomaUpdateView(SuperUsuarioMixin, UpdateView):
    model = Idioma
    form_class = idiomaForm
    template_name = 'crear.html'
    success_url = reverse_lazy('libro:idiomalistadoview')

    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un Idioma'
        context['entity'] = 'Idioma'
        context['listado_url'] = reverse_lazy('libro:idiomalistadoview')
        context['action'] = 'edit'
        return context


class idiomaDeleteView(SuperUsuarioMixin, DeleteView):
    model = Idioma
    template_name = 'eliminar.html'
    success_url = reverse_lazy('libro:idiomalistadoview')

    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un Idioma'
        context['entity'] = 'Idioma'
        context['listado_url'] = reverse_lazy('libro:idiomalistadoview')
        return context
