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

class categorialistadoview(SuperUsuarioMixin, ListView):
    model = Categoria
    template_name = 'listadocategoria.html'


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
                for i in Categoria.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias' 
        context['crear_url'] = reverse_lazy('libro:categoria_crear')
        context['entity'] = 'Categoria'
        context['listado_url'] = reverse_lazy('libro:categorialistadoview')
        return context


class categotiaCreateView(SuperUsuarioMixin, CreateView):
    model = Categoria
    form_class = categoriaForm
    template_name = 'crear.html'
    success_url = reverse_lazy('libro:categorialistadoview')

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
        context['title'] = 'Crear una Categoria' 
        context['entity'] = 'Categoria'
        context['listado_url'] = reverse_lazy('libro:categorialistadoview')
        context['action'] = 'add'
        return context


class categoriaUpdateView(SuperUsuarioMixin, UpdateView):
    model = Categoria
    form_class = categoriaForm
    template_name = 'crear.html'
    success_url = reverse_lazy('libro:categorialistadoview')

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
        context['title'] = 'Editar una Categoria'
        context['entity'] = 'Categoria'
        context['listado_url'] = reverse_lazy('libro:categorialistadoview')
        context['action'] = 'edit'
        return context


class categoriaDeleteView(SuperUsuarioMixin, DeleteView):
    model = Categoria
    template_name = 'eliminar.html'
    success_url = reverse_lazy('libro:categorialistadoview')

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
        context['title'] = 'Eliminar una Categoria'
        context['entity'] = 'Categoria'
        context['listado_url'] = reverse_lazy('libro:categorialistadoview')
        return context
