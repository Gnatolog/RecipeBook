from django.urls import path
from . import views

urlpatterns = [
    path('create-recipe/', views.RecipeCreate.as_view(), name='create_recipe'),
    path('my-recipe/', views.RecipeView.as_view(), name='my_recipe'),
    path('update-recipe/<int:recipe_id>',
         views.RecipeUpdate.as_view(),
         name='recipe_update'),
    path('del-recipe/<int:recipe_id>',
         views.RecipeDelete.as_view(),
         name='recipe_del'),
    path('show-recipe/<int:recipe_id>',
         views.RecipeSingleView.as_view(),
         name='recipe_show_single'),
    path('show-recipe-book',
         views.ViewRecipeBook.as_view(),
         name='recipe_book_show'),
]