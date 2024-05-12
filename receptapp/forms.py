from django import forms
from .models import Recipe, Category, RecipeBook


class CreateRecipeForm(forms.ModelForm):
    title = forms.CharField(label="Название рецепта", label_suffix='',
                            widget=forms.TextInput
                            (attrs={'class': 'form-control',
                                    'placeholder': 'Введите название рецепта'}))
    description = forms.CharField(label="Описание рецепта", label_suffix='',
                                  widget=forms.Textarea
                                  (attrs={'class': 'text-area',
                                          'placeholder': 'Описание рецепта'})
                                  )

    cooking_steps = forms.CharField(label="Шаги приготовления", label_suffix='',
                                    widget=forms.Textarea
                                    (attrs={'class': 'text-area',
                                            'placeholder': 'Шаги приготовления рецепта'})
                                    )

    cooking_time = forms.CharField(label="Время приготоволения", label_suffix='',
                                   widget=forms.TextInput
                                   (attrs={'class': 'form-control',
                                           'placeholder': 'часы:минут:секунды'}))

    image_recipe = forms.ImageField(label="Изображение блюда", label_suffix='',
                                    widget=forms.FileInput(
                                        attrs={'class': 'image-field'}
                                    ))

    class Meta:
        model = Recipe
        fields = ['title',
                  'description',
                  'cooking_steps',
                  'cooking_time',
                  'image_recipe', ]


class CategoryForm(forms.ModelForm):
    title_category = forms.ChoiceField(choices=[('v', 'Второе блюдо'),
                                                ('p', 'Первое блюдо'),
                                                ('h', 'Холодные закуски'),
                                                ('d', 'Десерты'),
                                                ('s', 'Суп'),
                                                ('f', 'Рыбное блюдо'),
                                                ('m', 'Мангал'),
                                                ('g', 'Гарнир'),
                                                ('n', 'Напиток'),
                                                ('sw', 'Сдобное блюдо'),],
                                       label="Категория рецепта", label_suffix='')
    type = forms.CharField(label="Тип блюда", label_suffix='',
                           widget=forms.TextInput
                           (attrs={'class': 'form-control',
                                   'placeholder': 'мясное'}))
    complexity = forms.IntegerField(label="Сложность приготовления", label_suffix='',
                                    min_value=0, max_value=10,
                                    widget=forms.NumberInput
                                    ({'class': 'form-control',
                                      'placeholder': 'по шкале от 0 до 10'}))

    class Meta:
        model = Category
        fields = ['title_category',
                  'type',
                  'complexity', ]


class RecipeBookForm(forms.ModelForm):
    class Meta:
        model = RecipeBook
        fields = ['recipe',
                  'category']


class SortRecipeForm(forms.Form):
    sort_field = forms.CharField(label="Отсортировать блюда по категории", label_suffix='',
                                 widget=forms.TextInput(
                                     {'class': 'form-control',
                                      'placeholder': 'первое блюдо'}))
