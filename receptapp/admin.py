from django.contrib import admin
from .models import Recipe, RecipeBook, Category

admin.site.register(Recipe)
admin.site.register(RecipeBook)
admin.site.register(Category)

