# Generated by Django 3.2.3 on 2023-09-19 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('id_ingredient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_ingredient', to='recipes.ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_recipe', models.CharField(max_length=200, verbose_name='Название рицепта')),
                ('image', models.ImageField(default=None, null=True, upload_to='recipes/images/')),
                ('text', models.TextField(blank=True, default='')),
                ('cooking_time', models.IntegerField()),
                ('id_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_author', to=settings.AUTH_USER_MODEL)),
                ('ingredients', models.ManyToManyField(through='recipes.RecipeIngredients', to='recipes.Ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='TagsRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_tr_recept', to='recipes.recipes')),
                ('id_teg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_tr_teg', to='recipes.tags')),
            ],
        ),
        migrations.AddField(
            model_name='recipes',
            name='tags',
            field=models.ManyToManyField(through='recipes.TagsRecipes', to='recipes.Tags'),
        ),
        migrations.AddField(
            model_name='recipeingredients',
            name='id_recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_recept', to='recipes.recipes'),
        ),
    ]
