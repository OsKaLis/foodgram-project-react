# Generated by Django 3.2.3 on 2023-10-05 08:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_alter_recipes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredients',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество.'),
        ),
    ]