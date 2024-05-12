from django.shortcuts import render
from django.views import View
from .models import Recipe, RecipeBook, Category
import logging
from .forms import CreateRecipeForm, CategoryForm, RecipeBookForm, SortRecipeForm
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class RecipeView(View):

    def get(self, request):
        recipe_author = Recipe.objects.filter(author=request.user)
        return render(request, 'receptapp/my_recipe.html',
                      {'recipe_author': recipe_author})


class RecipeCreate(View):

    def get(self, request):
        form_recipe = CreateRecipeForm()
        category_form = CategoryForm()
        return render(request, 'receptapp/create_recipe.html',
                      {'form_recipe': form_recipe,
                       'category_form': category_form})

    def post(self, request):
        form_recipe = CreateRecipeForm(request.POST, request.FILES)
        category_form = CategoryForm(request.POST)
        if form_recipe.is_valid() and category_form.is_valid():
            add_category = category_form.save()

            recipe_book = RecipeBook()

            new_recipe = form_recipe.save(commit=False)
            new_recipe.author = request.user
            new_recipe.save()

            recipe_book.category = Category.objects.filter(pk=add_category.id).first()
            recipe_book.save()
            recipe_book.recipe.add(new_recipe.id)

            return render(request, 'receptapp/recipe_save.html')
        else:
            return render(request, 'receptapp/create_recipe.html',
                          {'form_recipe': form_recipe})


class RecipeUpdate(View):

    def get(self, request, recipe_id):
        update_recipe = Recipe.objects.get(pk=recipe_id)
        new_form = CreateRecipeForm(initial=dict(
            title=update_recipe.title,
            description=update_recipe.description,
            cooking_steps=update_recipe.cooking_steps,
            cooking_time=update_recipe.cooking_time,
            image_recipe=update_recipe.image_recipe,
        ))
        return render(request, 'receptapp/update_recipe.html',
                      {'new_form': new_form})

    def post(self, request, recipe_id):

        form = CreateRecipeForm(request.POST, request.FILES)
        recipe = Recipe.objects.filter(pk=recipe_id).first()

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            cooking_steps = form.cleaned_data['cooking_steps']
            image_recipe = form.cleaned_data['image_recipe']

            if recipe is not None:
                recipe.title = title
                recipe.description = description
                recipe.cooking_steps = cooking_steps
                recipe.image_recipe = image_recipe
                recipe.save()
                logger.info(f'Изменён {recipe}')
                return render(request, 'receptapp/recipe_save.html')
        else:
            return render(request, 'receptapp/update_recipe.html',
                          {'new_form': form})


class RecipeDelete(View):
    def get(self, request, recipe_id):
        recipe = Recipe.objects.filter(pk=recipe_id).first()
        if recipe is not None:
            recipe.delete()
            logger.info(f'Рецепт удалён {recipe}')
            return render(request, 'receptapp/del_recipe.html')


class RecipeSingleView(View):

    def get(self, request, recipe_id):
        recipe = Recipe.objects.filter(pk=recipe_id).filter()
        return render(request, 'receptapp/single_recipe.html',
                      {'recipe': recipe[0]})


class ViewRecipeBook(View):

    def get(self, request):
        sort_recipe = SortRecipeForm()
        recipe_book = RecipeBook.objects.all()
        recipe_all = {}
        for recipe in recipe_book:
            if recipe.recipe.all().first() is not None:
                recipe_all[recipe] = [recipe.recipe.all().first()]

        return render(request, 'receptapp/book_recipe.html'
                      , {'recipe_book': recipe_all,
                         'form': sort_recipe})

    def post(self, request):
        sort_recipe = SortRecipeForm(request.POST)
        if sort_recipe.is_valid():
            recipe_all = RecipeBook.objects.all()
            sort_recipe_book = {}
            successful_search = False
            for recipe in recipe_all:
                if (recipe.category.title_category == sort_recipe.cleaned_data.get("sort_field")
                        and recipe.recipe.all().first() is not None):
                    sort_recipe_book[recipe] = [recipe.recipe.all().first()]

            if len(sort_recipe_book) > 1:
                successful_search = True

            return render(request, 'receptapp/book_recipe.html'
                          , {'recipe_book': sort_recipe_book,
                             'form': sort_recipe,
                             'successful_search': successful_search})
