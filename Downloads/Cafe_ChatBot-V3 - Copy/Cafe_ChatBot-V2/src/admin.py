from django.contrib import admin
from .models import Order, Kitchen_Order

# Register your models here.
admin.site.register(Order)
admin.site.register(Kitchen_Order)

admin.site.site_header  =  "Pizzas n Burgers Kitchen"  
admin.site.site_title  =  "Pizzas n Burgers Kitchen"
admin.site.index_title  =  "Pizzas n Burgers Order Table"
