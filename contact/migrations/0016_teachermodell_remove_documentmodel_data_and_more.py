# Generated by Django 4.2.1 on 2023-05-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0015_documentmodel_infomodel_delete_infomodell'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image/')),
                ('name', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=50)),
                ('teacher23', models.CharField(choices=[('katta oqituvchi', 'oqituvchi'), ('dotsent', 'dotsent'), ('professor', 'professor'), ('assistent', 'assistent')], max_length=214)),
            ],
        ),
        migrations.RemoveField(
            model_name='documentmodel',
            name='data',
        ),
        migrations.RemoveField(
            model_name='infomodel',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='TeacherModel',
        ),
    ]
