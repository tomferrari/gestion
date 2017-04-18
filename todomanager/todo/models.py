from django.db import models

class Client(models.Model):

    name = models.CharField(
        max_length=60,
        verbose_name="Nom"
    )

    surname = models.CharField(
        max_length=60,
        verbose_name="Prenom"
    )

    phone = models.IntegerField(
        max_length=60,
        verbose_name="Telephone"
    )

    mail = models.CharField(
        max_length=60,
        verbose_name="Mail"
    )

    def __str__(self):
        return str(self.user.username)

class Chambre(models.Model):

    number = models.IntegerField(
        max_length=60,
        verbose_name="Numero de chambre"
    )

    type_chambre = (
        ('0','Chambre 1 places'),
        ('1','Chambre 2 places'),
        ('2','Chambre 3 places'),
        ('3','Chambre 4 places'),
        ('4','Chambre 5 places'),
        ('5','Chambre 6 places'),
    )
