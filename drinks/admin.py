from django.contrib import admin

from .models import Drink, Category

# Register your models here.
class DrinkAdmin(admin.ModelAdmin):
    pass

class DrinkCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Drink, DrinkAdmin)
admin.site.register(Category, DrinkCategoryAdmin)
