# Generated by Django 3.1.14 on 2023-03-22 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='name',
            new_name='full_name',
        ),
    ]
