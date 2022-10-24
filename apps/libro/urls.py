from django.urls import path
from apps.libro.views.categoria.views import *
from apps.libro.views.autor.views import *
from apps.libro.views.editorial.views import *
from apps.libro.views.libro.views import *
from apps.libro.views.idioma.views import *
# from apps.libro.views.reservas.views import *
from apps.libro.views.dashboard.views import *

app_name = 'libro'

urlpatterns = [
      path('categoria/', categorialistadoview.as_view(), name='categorialistadoview'),
      path('categoria/crear/', categotiaCreateView.as_view(), name='categoria_crear'),
      path('categoria/editar/<int:pk>/', categoriaUpdateView.as_view(), name='categoria_editar'),
      path('categoria/eliminar/<int:pk>/', categoriaDeleteView.as_view(), name='categoria_eliminar'),
      
      path('idioma/', idiomalistadoview.as_view(), name='idiomalistadoview'),
      path('idioma/crear/', idiomaCreateView.as_view(), name='idioma_crear'),
      path('idioma/editar/<int:pk>/', idiomaUpdateView.as_view(), name='idioma_editar'),
      path('idioma/eliminar/<int:pk>/', idiomaDeleteView.as_view(), name='idioma_eliminar'),
      
      path('autor/', autorlistadoview.as_view(), name='autorlistadoview'),
      path('autor/crear/', AutorCreateView.as_view(), name='autor_crear'),
      path('autor/editar/<int:pk>/', AutorUpdateView.as_view(), name='autor_editar'),
      path('autor/eliminar/<int:pk>/', AutorDeleteView.as_view(), name='autor_eliminar'),
      
      path('editorial/', editoriallistadoview.as_view(), name='editoriallistadoview'),
      path('editorial/crear/', editorialCreateView.as_view(), name='editorial_crear'),
      path('editorial/editar/<int:pk>/', editorialUpdateView.as_view(), name='editorial_editar'),
      path('editorial/eliminar/<int:pk>/', editorialDeleteView.as_view(), name='editorial_eliminar'),
     
      path('libro/', librolistadoview.as_view(), name='librolistadoview'),
      path('libro/librosdisponibles', ListadoLibrosDisponibles.as_view(), name='librosdisponiblesview'),
      path('libro/detalle-libro/<int:pk>/',DetalleLibroDiponible.as_view(), name = 'detalle_libro'),
      path('libro/crear/', libroCreateView.as_view(), name='libro_crear'),
      path('libro/editar/<int:pk>/', libroUpdateView.as_view(), name='libro_editar'),
      path('libro/eliminar/<int:pk>/', libroDeleteView.as_view(), name='libro_eliminar'),
      
      path('reservar-libro/', RegistrarReserva.as_view(), name='reservar_Libro'),
      


      #home
      path('dashboard/', DashboardView.as_view(), name='dashboard'),

     
]