from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



# Create your models here.
    #class Client(models.Model):
    # user = models.OneToOneField(
    #     User,
    #     related_name="member"
    # )

class Client(models.Model):

    name = models.CharField(
        max_length=60,
        verbose_name="Nom"
    )
    surname = models.CharField(
        max_length=60,
        verbose_name="Prénom"
    )
    phone = models.CharField(
        max_length=60,
        verbose_name="phone"
    )
    mail = models.CharField(
        max_length=60,
        verbose_name="mail"
    )
    
    # class Meta:
    #     app_label = "todo"
    #     ordering = ['-created_at']

    def __str__(self):
        return str(self.name)

    # def get_absolute_url(self):
    #     return reverse_lazy('todo:tasks:retrieve', kwargs={'pk': self.id})
    


class Chambre(models.Model):
    
    TYPE_CHAMBRE = (
        ('0','Chambre: 1 place'),
        ('1','Chambre: 2 places '),
        ('2','Chambre: 3 places '),
        ('3','Chambre: 4 places '),
        ('4','Chambre: 5 places '),
        ('5','Chambre: 6 places '),
        ('6','Chambre: 7 places ')
    )
    description = models.TextField(
        max_length=60,
        verbose_name="Description Chambre"
    )

    def get_description(self):
        return self.description.replace('\r\n', '\\n')

    roomnumber = models.IntegerField(
        verbose_name="Numero Chambre"
    )

    etage = models.IntegerField(
        verbose_name="Etage"
    )


    def __str__(self):
        return str(self.roomnumber)

class Hotel(models.Model):

    hotelname = models.CharField(
        max_length=60,
        verbose_name="Nomhotel"
    )

    def __str__(self):
        return str(self.user.username)

class Reservation(models.Model):

    DateDebut = models.DateField(
        verbose_name="Date Debut"
    )

    DateFin = models.DateField(
        verbose_name="Date Fin"
    )

    client = models.ForeignKey(
        Client,
        verbose_name="client"
    )

    chambre = models.ForeignKey(
        Chambre,
        verbose_name="chambre"
    )

    def __str__(self):
        return str(self.client)
