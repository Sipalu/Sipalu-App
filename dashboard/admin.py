from django.contrib import admin
from .models import Category, Order, OrderItem, ShippingAddress,Worker,Service,BlogComment,Profile
# Register your models here.
@admin.register(Category)

# CRUD operation for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','image','description']

# CRUD operation for Worker

@admin.register(Worker)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id','worker_name','phone','address']

# CRUD operation for Services

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


