# Generated by Django 5.0.5 on 2024-05-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptapp', '0005_alter_category_title_alter_category_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipebook',
            name='rating',
        ),
        migrations.AlterField(
            model_name='recipebook',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
