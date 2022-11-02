from django.shortcuts import render, redirect, HttpResponse
from apps.libro.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from apps.libro.forms import *
from django.http import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.usuario.mixins import *
from django.urls import reverse


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'



class librolistadoview(SuperUsuarioMixin, ListView):
    model = libro
    template_name = 'listadolibro.html'

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Libros' 
        context['crear_url'] = reverse_lazy('libro:libro_crear')
        context['entity'] = 'Libros'
        context['listado_url'] = reverse_lazy('libro:librolistadoview')
        return context
    

class libroCreateView(SuperUsuarioMixin, CreateView):
    model = libro
    form_class = libroForm
    template_name = 'crear.html'
    success_url = reverse_lazy('libro:librolistadoview')

    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    @method_decorator(login_required)
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
        context['title'] = 'Crear un Libro'
        context['entity'] = 'Libros'
        context['listado_url'] = reverse_lazy('libro:librolistadoview')
        context['action'] = 'add'
        return context


class libroUpdateView(SuperUsuarioMixin, UpdateView):
    model = libro
    form_class = libroForm
    template_name = 'crear.html'
    success_url = reverse_lazy('libro:librolistadoview')

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
        context['title'] = 'Editar un Libro'
        context['entity'] = 'Libros'
        context['listado_url'] = reverse_lazy('libro:librolistadoview')
        context['action'] = 'edit'
        return context


class libroDeleteView(SuperUsuarioMixin, DeleteView):
    model = libro
    template_name = 'eliminar.html'
    success_url = reverse_lazy('libro:librolistadoview')

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
        context['title'] = 'Elminar un Libro'
        context['entity'] = 'Libros'
        context['listado_url'] = reverse_lazy('libro:librolistadoview')
        return context


class ListadoLibrosDisponibles(LoginRequiredMixin,ListView):
    model = libro
    paginate_by = 6
    template_name = 'librosdisponibles.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(cantidad__gte=1)
        return queryset


class DetalleLibroDiponible(LoginRequiredMixin,DetailView):
    model = libro
    template_name = 'detalleslibro.html'

    def get(self, request, *agrs, **kwargs):
        if self.get_object().cantidad > 0:
            return render(request, self.template_name, {'object': self.get_object()})
        return redirect('libro:librosdisponiblesview')


class ResevaCreateView(SuperUsuarioMixin, CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'crear.html'
    success_url = reverse_lazy('libro:listadoreservas')

    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(login_required)
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
        context['title'] = 'Crear una Reserva'
        context['entity'] = 'Reservas'
        context['listado_url'] = reverse_lazy('libro:listadoreservas')
        context['action'] = 'add'
        return context


#para administradores
class listadoreservas(SuperUsuarioMixin, ListView):
    model = Reserva
    template_name = 'listadoreservas.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(entregada=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Reservados Activas'
        context['crear_url'] = reverse_lazy('libro:reservas_crear')
        context['entity'] = 'Reservas'
        context['listado_url'] = reverse_lazy('libro:listadoreservas')
        return context


# class listadoreservasentregadas(SuperUsuarioMixin, ListView):
#     model = Reserva
#     template_name = 'listadoreservasconcretadas.html'

#     @method_decorator(csrf_exempt)
#     #@method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self):
#         queryset = self.model.objects.filter(entregada=True)
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Listado de Reservas Concretadas'
#         #context['crear_url'] = reverse_lazy('libro:reservacrear')
#         context['entity'] = 'Reservas'
#         context['listado_url'] = reverse_lazy('libro:listadoreservas')
#         return context





#para usuarios
class ListadoLibrosReservados(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'libros_reservados.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(
            estado=True, usuario=self.request.user)
        return queryset


class ListadoLibrosReservadosVencidos(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'libros_reservados_vencidos.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(
            estado=False, usuario=self.request.user)
        return queryset



class RegistrarReserva(LoginRequiredMixin, CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy('libro:librosdisponiblesview')
    


    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            Libro = libro.objects.filter(id = request.POST.get('libro')).first()
            usuario = Usuario.objects.filter(id = request.POST.get('usuario')).first()
            if libro and usuario:
                nueva_reserva = self.model(
                    libro = Libro,
                    usuario = usuario
                )
                nueva_reserva.save()

        return HttpResponseRedirect(reverse('libro:librosdisponiblesview'))
        

