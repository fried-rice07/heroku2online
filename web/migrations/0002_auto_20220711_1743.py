# Generated by Django 3.2.5 on 2022-07-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='avatar.png', null=True, upload_to='uploads'),
        ),
    ]
