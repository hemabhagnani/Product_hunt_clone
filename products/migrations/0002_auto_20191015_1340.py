# Generated by Django 2.0.2 on 2019-10-15 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='icon',
            new_name='Icon',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='Image',
        ),
    ]
