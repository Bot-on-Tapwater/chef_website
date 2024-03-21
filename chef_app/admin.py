from django.contrib import admin

from .models import Chefs, Customer, Testimonial, Service

admin.site.register(Chefs)
admin.site.register(Customer)
admin.site.register(Testimonial)
admin.site.register(Service)

# Register your models here.
