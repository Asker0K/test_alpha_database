from django.contrib import admin

from . models import Product, Pc, Laptop, Printer

admin.site.register(Product)
admin.site.register(Pc)
admin.site.register(Laptop)
admin.site.register(Printer)
