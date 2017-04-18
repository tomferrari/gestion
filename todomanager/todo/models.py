from django.db import models

# Create your models here.
class Client(models.Model):
    # user = models.OneToOneField(
    #     User,
    #     related_name="member"
    # )
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
    
    class Meta:
        app_label = "todo"
        ordering = ['-created_at']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('todo:tasks:retrieve', kwargs={'pk': self.id})
    
