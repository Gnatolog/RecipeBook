# Generated by Django 5.0.5 on 2024-05-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptapp', '0002_category_alter_recipe_cooking_time_recipebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipebook',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
