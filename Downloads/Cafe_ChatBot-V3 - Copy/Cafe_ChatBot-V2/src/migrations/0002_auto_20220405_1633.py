# Generated by Django 2.2.2 on 2022-04-05 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Items',
            new_name='items',
        ),
    ]
