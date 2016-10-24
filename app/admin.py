from django.contrib import admin

from .models import (
    Route,
    Service,
    Station,
    Ticket,
    Train,
    Wagon,
    WagonPlace,
    WagonServiceClass,
    WagonType,
    WagonCategory,
)

admin.site.register(Route)
admin.site.register(Service)
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Wagon)
admin.site.register(WagonPlace)
admin.site.register(WagonServiceClass)
admin.site.register(WagonType)
admin.site.register(WagonCategory)
admin.site.register(Ticket)
