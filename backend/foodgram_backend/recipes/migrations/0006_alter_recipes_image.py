# flake8: noqa
# Generated by Django 3.2.3 on 2023-10-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipes_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='recipes/images/', verbose_name='Картинка рицепта.'),
        ),
    ]