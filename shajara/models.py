from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    father = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='father_children')
    mother = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='mother_children')

    def __str__(self):
        return self.name
