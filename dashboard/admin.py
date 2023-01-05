<<<<<<< HEAD
from django.contrib import admin
from .models import Category, Order, OrderItem, ShippingAddress,Worker,Service,BlogComment,Profile
# Register your models here.
@admin.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','image','description']

@admin.register(Worker)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id','worker_name','phone','address']

@admin.register(Service)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','service_name','title','service_price','service_details','status','category','worker']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer','status']

admin.site.register(BlogComment)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(ShippingAddress)


=======
from django.contrib import admin
from .models import Category, Order, OrderItem, ShippingAddress,Worker,Service,BlogComment,Profile
# Register your models here.
@admin.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','image','description']

@admin.register(Worker)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id','worker_name','phone','address']

@admin.register(Service)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','service_name','title','service_price','service_details','status','category','worker']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer','status']

admin.site.register(BlogComment)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(ShippingAddress)


>>>>>>> 550c397da82c84627a5a585ea40baaaeb7077ad9
