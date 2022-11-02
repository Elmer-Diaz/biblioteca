from django.db import models
from django.forms import model_to_dict

from django.db.models.signals import post_save, pre_save
from biblioteca.settings import MEDIA_URL, STATIC_URL
from datetime import timedelta
from apps.usuario.models import Usuario


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre Completo', max_length = 200, blank = False, null=False, unique=True)
    nacionalidad = models.CharField('Nacionalidad',max_length = 200, blank = False, null=False)
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'otro')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    fecha_registro = models.DateField('Fecha Registro', auto_now=True, auto_now_add=False)
    


    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['id']

class Editorial(models.Model):
    id = models.AutoField(primary_key=True)
    nombreedi = models.CharField(verbose_name='Nombre', max_length=60, unique=True, blank=False, null=False)
    fecha_registro = models.DateField('Fecha Registro', auto_now=True, auto_now_add=False)
    

    def __str__(self):
        txt = "{0} "
        return txt.format(self.nombreedi)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        ordering = ['id']

class Idioma(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True, null=True)
    fecha_registro = models.DateField('Fecha Registro', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True, null=True)
    fecha_registro = models.DateField('Fecha Registro', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=60, unique=True)
    descripcion = models.TextField('Descripción', null=True, blank=True)
    cantidad = models.PositiveIntegerField('Cantidad o Stock',default = 1)
    fechapublicacion = models.DateField('Fecha de publicacion', blank=False, null=False)
    idioma = models.ForeignKey('idioma', null=False, blank=False, on_delete=models.CASCADE)
    autor = models.ManyToManyField(Autor)
    editorial = models.ForeignKey('editorial', null=False, blank=False, on_delete= models.CASCADE)
    categoria = models.ManyToManyField(Categoria)
    imagen = models.ImageField(
        'Imagen', upload_to='libros/', max_length=255, null=True, blank=True)
    fecha_registro = models.DateField('Fecha Registro', auto_now=True, auto_now_add=False)
    #estado = models.BooleanField(default=True, verbose_name='Estado')

    def __str__(self):
        txt = "{0}"
        return txt.format(self.titulo)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    
    class Meta:

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']
    
    def obtener_autores(self):
        autores = str([autor for autor in self.autor.all().values_list('nombre', flat=True)]).replace("[", "").replace("]", "").replace("'", "")
        return autores

    def obtener_categoria(self):
        categorias = str([categoria for categoria in self.categoria.all().values_list(
            'name', flat=True)]).replace("[", "").replace("]", "").replace("'", "")
        return categorias


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    libro = models.ForeignKey(libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad_dias = models.SmallIntegerField('Cantidad de Dias a Reservar', default=7)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False )
    #fecha_vencimiento = models.DateField('Fecha de vencimiento de la reserva', auto_now=False, auto_now_add=False, null=True, blank=True)
    estado = models.BooleanField(default=True, verbose_name='Estado')
    entregada = models.BooleanField(default=False, verbose_name='entregada')
    class Meta:

        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'Reserva de Libro {self.libro} por {self.usuario}'
    
def reducir_cantidad_libro(sender, instance, **kwargs):
    libro = instance.libro
    if libro.cantidad > 0:
        libro.cantidad = libro.cantidad - 1
        libro.save()

def validar_creacion_reserva(sender, instance, **kwargs):
    libro = instance.libro
    if libro.cantidad < 1:
        raise Exception("No puede realizar esta reserva, No hay libro Disponible")


# def agregar_fecha_vencimiento_reserva(sender, instance, **kwargs):
#     if instance.fecha_vencimiento is None or instance.fecha_vencimiento == '':
#         instance.fecha_vencimiento = instance.fecha_creacion + \
#             timedelta(days=instance.cantidad_dias)
#         instance.save()


post_save.connect(reducir_cantidad_libro, sender=Reserva)
# post_save.connect(agregar_fecha_vencimiento_reserva, sender=Reserva)
pre_save.connect(validar_creacion_reserva,sender = Reserva)



