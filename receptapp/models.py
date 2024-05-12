from django.contrib.auth.models import User
from django.db import models
import datetime


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.TimeField(verbose_name='hh:mm:ss')
    image_recipe = models.ImageField(upload_to=f'image_recipe',
                                     default=None,
                                     blank=False,
                                     null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'Рецепт: {self.title} '
                f'Краткое описание: {self.description}'
                f'Автор блюда: {self.author}')


class Category(models.Model):

    title_category = models.CharField(max_length=150,)
    type = models.CharField(max_length=100,)
    complexity = models.IntegerField()

    def __str__(self):
        return (f'Категория блюда:{self.title_category} '
                f'Вид блюда:{self.type} '
                f'Сложность приготовления блюда {self.complexity}')


class RecipeBook(models.Model):
    recipe = models.ManyToManyField(Recipe,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Категория рецепта {self.category}'
