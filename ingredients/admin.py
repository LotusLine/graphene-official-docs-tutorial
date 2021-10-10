from django.contrib import admin
from .models import Category, Ingredient


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class IngredientManager(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'notes')




admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient,IngredientManager )
