# Generated by Django 4.1.7 on 2023-05-27 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0011_infomodell_teachermodell_delete_infomodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image/')),
                ('name', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=1000)),
                ('rate', models.CharField(max_length=50)),
                ('document', models.FileField(upload_to='pdf')),
            ],
        ),
        migrations.RenameModel(
            old_name='TeacherModell',
            new_name='TeacherModel',
        ),
        migrations.DeleteModel(
            name='InfoModell',
        ),
        migrations.AddField(
            model_name='infomodel',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.teachermodel'),
        ),
    ]
