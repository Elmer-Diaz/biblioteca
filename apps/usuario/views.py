from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from apps.usuario.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from apps.usuario.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.usuario.mixins import *

class ListadoUsuario(SuperUsuarioMixin,ListView):
    model = Usuario
    template_name = 'listado_usuarios.html'
    
    # def get_queryset(self):
    #     return Usuario.objects.filter(usuario_activo=True)
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
                for i in Usuario.objects.filter(usuario_activo=True):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['crear_url'] = reverse_lazy('usuario:Registrar_usuario')
        context['entity'] = 'Usuario'
        context['listado_url'] = reverse_lazy('usuario:listar_usuarios')
        return context


class RegistarUsuario(SuperUsuarioMixin, CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'crear_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuarios')

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
        context['title'] = 'Crear un Usuario'
        context['entity'] = 'Usuario'
        context['listado_url'] = reverse_lazy('usuario:listar_usuarios')
        context['action'] = 'add'
        return context


class EditarUsuario(SuperUsuarioMixin, UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'crear_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuarios')

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
        context['title'] = 'Editar un Usuario'
        context['entity'] = 'Usuario'
        context['listado_url'] = reverse_lazy('usuario:listar_usuarios')
        context['action'] = 'edit'
        return context


class EliminarUsuario(SuperUsuarioMixin, DeleteView):
    model = Usuario
    template_name = 'eliminar.html'
    success_url = reverse_lazy('usuario:listar_usuarios')

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
        context['title'] = 'Eliminar un Usuario'
        context['entity'] = 'Usuario'
        context['listado_url'] = reverse_lazy('usuario:listar_usuarios')
        return context
