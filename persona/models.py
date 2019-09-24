from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Persona(models.Model):
    ROL = (
      ('D', 'Doctor'),
      ('E', 'Estudiante'),
      ('O', 'Otro'),
   )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rol = models.CharField(max_length=50,choices=ROL,default='D',blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    predicciones = models.IntegerField(blank=True, null=True)
    
    def create_profile(sender,**kwargs):
        if kwargs['created']:
            persona_profile = Persona.objects.create(user=kwargs['instance'])
    
    post_save.connect(create_profile,sender=User)