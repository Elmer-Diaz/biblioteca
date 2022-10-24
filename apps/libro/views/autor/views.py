from django.shortcuts import render
from apps.libro.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.libro.forms import *
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.usuario.mixins import *


class autorlistadoview(SuperUsuarioMixin, ListView):
    model = Autor
    template_name = 'listadoautor.html'

    def get_queryset(self):
        return Autor.objects.order_by('id')
    
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
                for i in Autor.objects.all():
                    data.append(i.toJSON())
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Autor' 
        context['crear_url'] = reverse_lazy('libro:autor_crear')
        context['entity'] = 'Autor'
        context['listado_url'] = reverse_lazy('libro:autorlistadoview')
        return context


class AutorCreateView(SuperUsuarioMixin, CreateView):
    model = Autor
    form_class = autorForm
    template_name = 'crear.html'
    success_url = reverse_lazy('libro:autorlistadoview')

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
        context['title'] = 'Crear un Autor' 
        context['entity'] = 'Autor'
        context['listado_url'] = reverse_lazy('libro:autorlistadoview')
        context['action'] = 'add'
        return context


class AutorUpdateView(SuperUsuarioMixin, UpdateView):
    model = Autor
    form_class = autorForm
    template_name = 'crear.html'
    success_url = reverse_lazy('libro:autorlistadoview')

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
        context['title'] = 'Editar un Autor'
        context['entity'] = 'Autor'
        context['listado_url'] = reverse_lazy('libro:autorlistadoview')
        context['action'] = 'edit'
        return context


class AutorDeleteView(SuperUsuarioMixin, DeleteView):
    model = Autor
    template_name = 'eliminar.html'
    success_url = reverse_lazy('libro:autorlistadoview')

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
        context['title'] = 'Editar un Autor'
        context['entity'] = 'Autor'
        context['listado_url'] = reverse_lazy('libro:autorlistadoview')
        return context
