# Generated by Django 4.1.3 on 2022-11-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postit_api', '0005_postlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/', verbose_name='image'),
        ),
    ]
