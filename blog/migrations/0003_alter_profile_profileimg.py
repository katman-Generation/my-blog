# Generated by Django 3.2.23 on 2024-01-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='taaa.jpg', upload_to='profile_images'),
        ),
    ]
