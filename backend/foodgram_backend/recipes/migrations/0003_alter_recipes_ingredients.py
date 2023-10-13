# flake8: noqa
# Generated by Django 3.2.3 on 2023-10-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20231012_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipe_ingredients', through='recipes.RecipeIngredients', to='recipes.Ingredients', verbose_name='Ингридиенты.'),
        ),
    ]
