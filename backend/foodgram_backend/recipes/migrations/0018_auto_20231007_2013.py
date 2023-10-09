# Generated by Django 3.2.3 on 2023-10-07 17:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0017_alter_recipeingredients_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorited',
            name='id_recipe',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='favorited', to='recipes.recipes', verbose_name='Избраный рицепт.'),
        ),
        migrations.AlterField(
            model_name='favorited',
            name='id_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='favorited', to=settings.AUTH_USER_MODEL, verbose_name='Добавил в избранное.'),
        ),
        migrations.AlterField(
            model_name='recipeingredients',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество.'),
        ),
    ]
