# Generated by Django 3.1.14 on 2023-03-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20230320_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammodel',
            name='foto',
            field=models.ImageField(default=1, upload_to='image/'),
            preserve_default=False,
        ),
    ]