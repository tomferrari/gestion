from django.db import models

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
    description = TextField()
    num_Chambre = models.CharField(
        max_length=50,
        verbose_name="Numero chambre",
        blank=True,
        default="/",
        # validators=[
        #     RegexValidator(
        #         regex = '[^[0-9]{10}/00010$]|/',
        #         message='Doit etre de la forme : \"XX...XX/00010\" ou \"/\"',
        #         code='invalid_num_com'
        #         )
        #     ]
        )
    def get_description(self):
        return self.description.replace('\r\n', '\\n')

<<<<<<< HEAD

=======
    roomnumber = models.IntegerField(
        max_length=60,
        verbose_name="NumeroChambre"
    )

    etage = models.IntegerField(
        max_length=60,
        verbose_name="Etage"
    )


    def __str__(self):
        return str(self.user.username)

class Hotel(models.Model):

    hotelname = models.CharField(
        max_length=60,
        verbose_name="Nomhotel"
    )

    def __str__(self):
        return str(self.user.username)

class Reservation(models.Model):

    DateDebut = models.IntegerField(
        max_length=60,
        verbose_name="DateDebut"
    )

    DateFin = models.IntegerField(
        max_length=60,
        verbose_name="DateFin"
    )

    settings = models.ForeignKey(
        'Setting',
        null=True,
        blank=True,
        verbose_name="Paramêtres"
    )

    def __str__(self):
        return str(self.user.username)
>>>>>>> d0b02d1e66ba5bc199d869d8773e5fe7f90144fa
