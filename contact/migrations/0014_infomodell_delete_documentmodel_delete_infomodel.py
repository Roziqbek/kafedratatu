# Generated by Django 4.2.1 on 2023-05-29 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_documentmodel_remove_infomodel_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoModell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image/')),
                ('name', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=1000)),
                ('rate', models.CharField(max_length=50)),
                ('pdf', models.FileField(upload_to='pdf')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.teachermodel')),
            ],
        ),
        migrations.DeleteModel(
            name='DocumentModel',
        ),
        migrations.DeleteModel(
            name='InfoModel',
        ),
    ]
