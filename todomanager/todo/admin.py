from django.contrib import admin
from todo.models import Client, Chambre, Reservation
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'phone',
        'mail'
    )

class ChambreAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'roomnumber',
        'etage'
    )

class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'DateDebut',
        'DateFin',
        'client',
        'chambre'
    )
# admin.site.register(Task, TaskAdmin)
admin.site.register(Chambre, ChambreAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Reservation, ReservationAdmin)