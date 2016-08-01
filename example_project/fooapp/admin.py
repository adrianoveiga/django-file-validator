from django.contrib import admin
from .models import FooModel

# Register your models here.

class AdminFooModel(admin.ModelAdmin):
    list_display = ('description', 'image', 'big_image', 'small_image' )


admin.site.register(FooModel, AdminFooModel)