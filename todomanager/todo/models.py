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

<<<<<<< HEAD
    DateDebut = models.DateField(
        verbose_name="Date Debut"
    )

    DateFin = models.DateField(
        verbose_name="Date Fin"
=======
    DateDebut = models.DateTimeField(
        verbose_name="DateDebut"
    )

    DateFin = models.DateTimeField(
        verbose_name="DateFin"
>>>>>>> c97636a583ce97ffe82635943f6e7de3e6882b5e
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

class Task(models.Model):
    status_choices = (
        (None, '---'),
    )
    name = models.CharField(
        max_length=60,
        verbose_name="Nom"
    )
    # assigned_to = models.ForeignKey(
    #     Member,
    #     verbose_name="Assigné à",
    #     related_name="tasks_assigned",
    #     null=True,
    #     blank=True
    # )
    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )
    due_date = models.DateTimeField(
        verbose_name="Fin prévue le",
        null=True,
        blank=True,
        default=timezone.now() + timedelta(1)
    )
    completed = models.BooleanField(
        verbose_name="Tache terminée ? ",
        default=False,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default=None,
        null=True,
        blank=True
    )
    # list = models.ForeignKey(
    #     Group,
    #     verbose_name="Liste",
    #     related_name="tasks"
    # )

    class Meta:
        app_label = "todo"
        # ordering = ['-created_at']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return '/'+str(self.id)+'/'
        return reverse_lazy('todo:tasks:retrieve', kwargs={'pk': self.id})