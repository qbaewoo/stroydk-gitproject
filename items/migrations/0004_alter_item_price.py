# Generated by Django 4.0.5 on 2022-06-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_description_alter_item_item_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, verbose_name='Цена'),
        ),
    ]
