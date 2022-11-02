from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, apellidos, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo')

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, nombres, apellidos, password):
        usuario = self.create_user(
            email,
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            password = password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario





class Usuario(AbstractBaseUser, PermissionsMixin):
    #se pueden agregar mas atributos
    username = models.CharField(
        'Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electronico',
                              max_length=254, unique=True)
    nombres = models.CharField(
        'Nombres', max_length=200, blank=True, null=True)
    apellidos = models.CharField(
        'Apellidos', max_length=200, blank=True, null=True)
    imagen = models.ImageField(
        'Imagen de perfil', upload_to='perfil/', max_length=200, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres}, {self.apellidos}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador


