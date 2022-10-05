from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'
        db_table = 'tipo'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        db_table = 'categoria'
        ordering = ['id']


class Employee(models.Model):
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=0)
    names = models.CharField(max_length=200, verbose_name='Nombres')
    last_names = models.CharField(max_length=200, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True)
    joined_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    age = models.PositiveIntegerField(verbose_name='Edad', default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        db_table = 'empleado'
        ordering = ['id']
