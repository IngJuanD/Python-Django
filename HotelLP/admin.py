from django.contrib import admin

# Register your models here.
from HotelLP.models import Cliente, Contacto, Habitacion, Plan, Reserva

class ClienteAdmin(admin.ModelAdmin):
    list_display=("identificacion_cl","nombre_cl","apellido_cl")
    search_fields=("identificacion_cl","nombre_cl","apellido_cl")

class PlanAdmin(admin.ModelAdmin):
    list_display=("id_plan","nombre_plan","precio")
    search_fields=("id_plan","nombre_plan","precio")

class HabitacionAdmin(admin.ModelAdmin):
    list_display=("id_hb","capacidad","descripcion_hb")
    search_fields=("id_hb","capacidad")

class ReservaAdmin(admin.ModelAdmin):
    list_display=("id_reserva","fecha_inicio","fecha_fin","identificacion_cl")
    search_fields=("id_reserva","fecha_inicio","fecha_fin")


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Plan,PlanAdmin)
admin.site.register(Habitacion,HabitacionAdmin)
admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Contacto)
