from django.shortcuts import render
from .forms import UserForms
from django.contrib.auth.decorators import login_required
import logging
from receptapp.models import RecipeBook
import random

logger = logging.getLogger(__name__)


@login_required
def start_page(request):
    logger.info('Пользователь вошёл на страницу')
    recipe_book = RecipeBook.objects.all()
    recipe_all = {}
    while len(recipe_book) != len(recipe_all) != 5:
        recipe = recipe_book[random.randrange(0, len(recipe_book))]
        if recipe not in recipe_all.keys():
            if recipe.recipe.all().first() is not None:
                recipe_all[recipe] = [recipe.recipe.all().first()]

    return render(request, 'userapp/start_page.html',
                  {'recipe_book': recipe_all})



def register(request):
    if request.method == 'POST':
        user_form = UserForms(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            logger.info(f'{new_user.username} зарегистрировался')
            return render(request,
                          'userapp/template/register_done.html',
                          {'new_user': new_user})

    else:
        user_form = UserForms()

    return render(request,
                  'userapp/template/register.html',
                  {'user_form': user_form})
