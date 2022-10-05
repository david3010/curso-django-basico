# Para hacer test con el ORM y solo usar el python test.py
# import os
# pppfrom config.wsgi import *

from core.erp.models import Category, Type, Employee
from django.test import TestCase


class EmployeeTestCase(TestCase):
    def setUp(self):
        type = Type.objects.create(name='External')
        type.save()
        employee = Employee.objects.create(names='David', type_id=type.id, last_names='Gallegos Velez')
        employee.save()

    def test_is_staff(self):
        print('test1')
        category = Category.objects.create(name='Staff')
        category.save()
        employee = Employee.objects.get(names='David')
        employee.category.add(category)
        employee.save()
        self.assertEqual(employee.category.all().get(id=1).name, 'Staff')

    def test_is_external(self):
        print('test2')
        employee = Employee.objects.get(names='David')
        self.assertEqual(employee.type.name, 'External')
