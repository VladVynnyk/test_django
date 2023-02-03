from django.contrib import admin
from .models import Product, Category
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(Product)
admin.site.register(Category)

# For displaying orders with fields 
class listAllOrders(admin.ModelAdmin):
    list_display = ('user', 'get_email','name', 'price', 'category')
    search_fields = ('category__name', 'price')

    @admin.display(ordering='user__email', description='Email')
    def get_email(self, obj):
        return obj.user.email

admin.site.register(Product, listAllOrders)